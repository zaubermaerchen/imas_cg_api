# -*- coding: utf-8 -*-
from rest_framework import generics
from datetime import datetime
from .serializer import SearchSerializer, Costar, CostarSerializer
from .pagination import SearchLimitOffsetPagination
from data.models import Cartoon, IdolName


def convert_datetime_object(datetime_string, datetime_format):
    if datetime_string is None or len(datetime_string) == 0:
        return None

    value = None
    try:
        value = datetime.strptime(datetime_string, datetime_format)
    finally:
        return value


class SearchView(generics.ListAPIView):
    serializer_class = SearchSerializer
    pagination_class = SearchLimitOffsetPagination

    def get_queryset(self):
        # リクエストから必要なパラメータを取得
        title = self.request.query_params.get('title')
        characters = self.request.query_params.getlist('character')
        start_at = convert_datetime_object(self.request.query_params.get('start_at'), '%Y-%m-%d')
        end_at = convert_datetime_object(self.request.query_params.get('end_at'), '%Y-%m-%d')

        return Cartoon.get_list(title, characters, start_at, end_at)


class CostarView(generics.ListAPIView):
    serializer_class = CostarSerializer

    def get_queryset(self, *args, **kwargs):
        name = self.kwargs.get('name')

        # 名前チェック
        try:
            IdolName.objects.get(pk=name)
        except IdolName.DoesNotExist:
            return []

        costars = []
        for k, v in Cartoon.get_costars(name).items():
            costars.append(Costar(k, v))
        return costars



