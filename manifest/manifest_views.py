import logging
from os import stat
from tokenize import Triple
import traceback
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import APIView
from django.shortcuts import get_object_or_404
from django.utils import timezone


from manifest.manifest_filters import XxyhImsWsManifestHdrFilterSet, XxyhImsWsManifestLnsFilterSet
from manifest.models.MANIFEST import XxyhImsWsManifestHdr, XxyhImsWsManifestLns, XxyhJobs
from manifest.manifest_serializers import XxyhImsWsManifestHdrSerializer, XxyhImsWsManifestHdrSerializerOnly, XxyhImsWsManifestLnsSerializer
from utils.pagination import YamiPagination
from utils.db_utils.common import get_curr_time_unix
from drf_apis.log_config import LOG_SETTINGS
from logging.config import dictConfig
from pprint import pprint as pp

dictConfig(LOG_SETTINGS)
logger = logging.getLogger('ims.yami.manifest_views')

# Create your views here.

class ManifestHdrLnsGetView(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):

    queryset = XxyhImsWsManifestHdr.objects.all()
    serializer_class = XxyhImsWsManifestHdrSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = XxyhImsWsManifestHdrFilterSet

    def list(self, request, *args, **kwargs):

        short_id = request.META.get('HTTP_SHORTID')
        if not short_id:
            user_name = request.GET.get('userName', None)
        else:
            user_name = short_id.upper()

        inquiry_id = request.GET.get('inquiryId', None)
        if not inquiry_id:
            inquiry_id = get_curr_time_unix()
        queryset = self.filter_queryset(self.get_queryset())
        paginator = YamiPagination()
        page = paginator.paginate_queryset(queryset, request)
        serializer = self.get_serializer(page, many=True)
        return paginator.get_paginated_response('maniest_hdr', serializer.data, user_name, inquiry_id)

    def retrieve(self, request, *args, **kwargs):

        manifest_hdr = self.get_object()
        serializer = self.serializer_class(instance=manifest_hdr)

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )


class ManifestHdrGetView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):

    queryset = XxyhImsWsManifestHdr.objects.all()
    serializer_class = XxyhImsWsManifestHdrSerializerOnly
    filter_backends = (DjangoFilterBackend,)
    filterset_class = XxyhImsWsManifestHdrFilterSet

    def list(self, request, *args, **kwargs):

        short_id = request.META.get('HTTP_SHORTID')
        if not short_id:
            user_name = request.GET.get('userName', None)
        else:
            user_name = short_id.upper()

        inquiry_id = request.GET.get('inquiryId', None)
        if not inquiry_id:
            inquiry_id = get_curr_time_unix()
        queryset = self.filter_queryset(self.get_queryset())
        paginator = YamiPagination()
        page = paginator.paginate_queryset(queryset, request)
        serializer = self.get_serializer(page, many=True)
        return paginator.get_paginated_response('maniest_hdr', serializer.data, user_name, inquiry_id)


class ManifestLnsGetView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    
    queryset = XxyhImsWsManifestLns.objects.all()
    serializer_class = XxyhImsWsManifestLnsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = XxyhImsWsManifestLnsFilterSet
    def list(self, request, *args, **kwargs):

        short_id = request.META.get('HTTP_SHORTID')
        if not short_id:
            user_name = request.GET.get('userName', None)
        else:
            user_name = short_id.upper()

        inquiry_id = request.GET.get('inquiryId', None)
        if not inquiry_id:
            inquiry_id = get_curr_time_unix()
        queryset = self.filter_queryset(self.get_queryset())
        paginator = YamiPagination()
        page = paginator.paginate_queryset(queryset, request)
        serializer = self.get_serializer(page, many=True)
        return paginator.get_paginated_response('maniest_lns', serializer.data, user_name, inquiry_id)


class ManifestHdrLnsPostView(
    APIView
   
):
    logger.info('ManifestHdrLnsPostView Initiated.')

    def post(self, request, *args, **kwargs):
        if not request.data.get('user_name') or not request.data.get('group_name') or not request.data.get(
                'source_system'):
            output_data_obj = {
                'message': 'Required parameter missing or invalid [user_name, group_name, source_system]',
                'status': 'error'}
            return Response(output_data_obj, status=status.HTTP_400_BAD_REQUEST)
        data = request.data
        lines = data.pop('lines',[])
        manifest = data

        data['last_update_date'] = timezone.now()
        
        try:

            if 'manifest_id' in data.keys():
                manifes_obj = XxyhImsWsManifestHdr.objects.get(manifest_id=data['manifest_id'])
                manifest_sz = XxyhImsWsManifestHdrSerializer(instance=manifes_obj, data=manifest, partial=True)
                manifest_sz.is_valid(raise_exception=True)
                manifest_sz.save()
            else:
                manifest['creation_date'] = timezone.now()
                manifest_sz = XxyhImsWsManifestHdrSerializer(data=manifest)
                manifest_sz.is_valid(raise_exception=True)
                manifest_sz.save()
            # return Response(manifest_sz.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            traceback.print_exc()
            return Response({
                'message': manifest_sz.errors
            }, status=status.HTTP_400_BAD_REQUEST
            )
        for line in lines:
            line['manifest_id'] = manifest_sz.data['manifest_id']
            line['manifest_name'] = manifest_sz.data['manifest_name']
            line['last_update_date'] = timezone.now()
            if 'job_id' in line.keys():
                job = XxyhJobs.objects.get(job_id = line['job_id'])
                line['job_name'] = job.job_name
            if 'manifest_line_id' in line.keys():
                line_obj = XxyhImsWsManifestLns.objects.get(manifest_line_id=line['manifest_line_id'])
                print('sending data to serializer')
                line_sz = XxyhImsWsManifestLnsSerializer(line_obj, data=line, partial=True)      
            else:
                line['creation_date'] = timezone.now()
                line_sz = XxyhImsWsManifestLnsSerializer(data=line)
            try:
                if line_sz.is_valid(raise_exception=True):
                    line_sz.save()
            except Exception as e:
                traceback.print_exc()
                return Response({
                    'message': line_sz.errors
                }, status=status.HTTP_400_BAD_REQUEST
                )
        instance = XxyhImsWsManifestHdr.objects.get(manifest_id=manifest_sz.data['manifest_id'])
        final_obj = XxyhImsWsManifestHdrSerializer(instance)
        return Response(final_obj.data, status=status.HTTP_201_CREATED)


class ManifestHdrDelView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            manifest_id = request.data['manifest_id']

            hdr = get_object_or_404(XxyhImsWsManifestHdr, manifest_id=manifest_id)
            
            hdr.delete()
            return Response("Deleted Successfully!", status=status.HTTP_200_OK)
        except KeyError: 
            return Response({'error': "manifest_line_id is missing!"},status=status.HTTP_4)

    
    

class ManifestLnsDelView(APIView):  
    
    def post(self, request, *args, **kwargs):
        try:
            manifest_line_id = request.data['manifest_line_id']
            line = get_object_or_404(XxyhImsWsManifestLns, manifest_line_id=manifest_line_id)

            hdr = XxyhImsWsManifestHdr.objects.get(manifest_id=line.manifest_id)
            sz = XxyhImsWsManifestHdrSerializer(data=hdr)

            if len(sz.get_all_lines(hdr))> 1:
                line.delete()
                return Response("Deleted Successfully!", status=status.HTTP_200_OK)
            else: 
                output_data_obj = {
                    'message': 'Required at least one line ',
                    'status': 'error'}
                return Response(output_data_obj, status=status.HTTP_400_BAD_REQUEST)
        except KeyError: 
            return Response({'error': "manifest_line_id is missing!"},status=status.HTTP_400_BAD_REQUEST)