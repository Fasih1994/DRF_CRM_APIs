from rest_framework import serializers
from django.utils import timezone


from utils.drf_utils.serializers import DynamicFieldsModelSerializer
from manifest.models.MANIFEST import XxyhImsWsManifestHdr, XxyhImsWsManifestLns, XxyhJobs

class XxyhImsWsManifestLnsSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = XxyhImsWsManifestLns
        fields = '__all__'
        extra_kwargs = {
            'manifest_line_id': {
                'validators': [],
            }
        }

    def create(self, validated_data):
        instance, created = XxyhImsWsManifestLns.objects.update_or_create(**validated_data)
        return instance


class XxyhImsWsManifestHdrSerializer(DynamicFieldsModelSerializer):
    all_lines = serializers.SerializerMethodField()
    lines = XxyhImsWsManifestLnsSerializer(write_only=True, required=False, allow_null=True, many=True)

    def get_all_lines(self, instance: XxyhImsWsManifestHdr):
        lines = XxyhImsWsManifestLns.objects.filter(manifest_id=instance.manifest_id)
        return XxyhImsWsManifestLnsSerializer(lines, many=True).data

    class Meta:
        model = XxyhImsWsManifestHdr
        fields = "__all__"
        extra_fields = ['all_lines', 'lines']
        extra_kwargs = {
            'manifest_id': {
                'validators': [],
            }
        }

    def validate_manifest_name(self, value):
        if self.initial_data.get('manifest_id', None):
            print('Validating manifest id')
            print(self.initial_data.get('manifest_id', None))
            return value
        else:
            print('Validating manifest name - create mode')
            print(value)
            d = XxyhImsWsManifestHdr.objects.filter(manifest_name=value)
            if d:
                raise serializers.ValidationError("xxyh ims ws manifest hdr with this manifest name already exists.")
            return value


    # def create(self, validated_data):
    #     print("/////////////////////// CREATE")
    #     lines = validated_data.pop('lines', [])
    #     # manifest_id = validated_data.get('manifest_id', None)
    #     instance = XxyhImsWsManifestHdr.objects.create(**validated_data)
    #     instance.process_status="CREATED"
    #     for line in lines:
    #             line['manifest_id'] = instance.manifest_id
    #             line['manifest_name'] = instance.manifest_name
    #             if 'job_id' in line.keys():
    #                 job = XxyhJobs.objects.get(job_id = line['job_id'])
    #                 line['job_name'] = job.job_name
    #     # lines += self.get_all_lines(instance=instance)
    #     sz = XxyhImsWsManifestLnsSerializer(data=lines, many=True)
    #     if sz.is_valid():
    #         sz.save()
    #     else:
    #         XxyhImsWsManifestLns.objects.filter(manifest_name=instance.manifest_name).delete()
    #         XxyhImsWsManifestHdr.objects.filter(manifest_name=instance.manifest_name).delete()
    #         sz.is_valid(raise_exception=True)
    #     return instance
    
    # def update(self, validated_data):
    #     print("/////////////////////// UPDATE")
    #     lines = validated_data.pop('lines', [])
    #     data = validated_data
    #     data["last_update_date"] = timezone.now()
    #     if "lines" in data.keys():
    #         for line in data["lines"]:
    #             line['last_update_date'] = timezone.now()
    #     instance = XxyhImsWsManifestHdr.objects.update(**validated_data)
    #     instance.process_status="UPDATED"
    #     for line in lines:
    #             line['manifest_id'] = instance.manifest_id
    #             line['manifest_name'] = instance.manifest_name
    #             if 'job_id' in line.keys():
    #                 job = XxyhJobs.objects.get(job_id = line['job_id'])
    #                 line['job_name'] = job.job_name
    #     # lines += self.get_all_lines(instance=instance)
    #     sz = XxyhImsWsManifestLnsSerializer(data=lines, many=True)
    #     if sz.is_valid():
    #         sz.save()
    #     else:
    #         XxyhImsWsManifestLns.objects.filter(manifest_name=instance.manifest_name).delete()
    #         XxyhImsWsManifestHdr.objects.filter(manifest_name=instance.manifest_name).delete()
    #         sz.is_valid(raise_exception=True)
    #     return instance


class XxyhImsWsManifestHdrSerializerOnly(DynamicFieldsModelSerializer):
   
    class Meta:
        model = XxyhImsWsManifestHdr
        fields = "__all__"
    

    def validate_manifest_name(self, value):
        print('Validating manifest name')
        if self.initial_data.get('manifest_id', None):
            print(self.initial_data.get('manifest_id', None))
            return value
        else:
            print('Validating manifest name - create mode')
            d = XxyhImsWsManifestHdr.objects.filter(manifest_name=value)
            if d:
                raise serializers.ValidationError("xxyh ims ws manifest hdr with this manifest name already exists.")
            return value