from rest_framework.pagination import PageNumberPagination


class MyPagePagination(PageNumberPagination):
    page_size = 2