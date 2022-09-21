import logging
import math
from datetime import datetime

from rest_framework import pagination
from rest_framework.response import Response

logger = logging.getLogger("util.common.custom_pagination")

class Pagination(pagination.PageNumberPagination):
    def __init__(self):
        super(Pagination, self).__init__()
        self.page = 1
        self.page_size = 100
        self.page_size_query_param = 'page_size'
        self.start_time = datetime.now()
        self.end_time = datetime.now()


class YamiPagination(pagination.PageNumberPagination):
    def __init__(self):
        self.page = 1
        self.page_size = 100
        self.page_size_query_param = 'recordsPerPage'

    def get_paginated_response(self, key, data, username, inquiry_id, error_code=None, error_message=None):
        total_records = self.page.paginator.count
        records_per_page = int(self.request.GET.get('recordsPerPage', self.page_size))
        total_pages = math.ceil(total_records / records_per_page)
        return Response({
                'userName': username,
                'inquiryId': inquiry_id,
                'totalRecords': total_records,
                'totalPages': total_pages,
                'page': int(self.request.GET.get('page', 1)),
                'recordsPerPage': records_per_page,
                key: data,
                'errorCode': error_code,
                'errorMessage': error_message
        })



