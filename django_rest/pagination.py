from rest_framework.pagination import LimitOffsetPagination
# , PageNumberPagination

class CustomPagination(LimitOffsetPagination):
    limit_query_param = "_limit"
    offset_query_param = "_start"

# class PageNumberWithPageSizePagination(PageNumberPagination):
#     page_size_query_param = '20'