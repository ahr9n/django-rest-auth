from rest_framework.pagination import LimitOffsetPagination


class CustomPagination(LimitOffsetPagination):
    limit_query_param = "_limit"
    offset_query_param = "_start"
