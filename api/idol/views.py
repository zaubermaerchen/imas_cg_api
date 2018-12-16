# -*- coding: utf-8 -*-
from rest_framework import generics
from .serializer import SearchSerializer
from .pagination import SearchLimitOffsetPagination
from data.models import Idol
from api.response import JSONResponse, JSONResponseNotFound


def get_request_param(request, key, default_value=None):
    value = default_value

    if key in request.POST:
        value = request.POST[key]
    elif key in request.GET:
        value = request.GET[key]

    return value


def get_request_params(request, key):
    if key in request.POST:
        return request.POST.getlist(key)

    if key in request.GET:
        return request.GET.getlist(key)

    return None


class GetView(generics.RetrieveAPIView):
    queryset = Idol.objects.all()
    serializer_class = SearchSerializer


class SearchView(generics.ListAPIView):
    serializer_class = SearchSerializer
    pagination_class = SearchLimitOffsetPagination

    def get_queryset(self):
        # リクエストから必要なパラメータを取得
        name = self.request.query_params.get('name')
        idol_types = self.request.query_params.getlist('type')
        rarities = self.request.query_params.getlist('rarity')

        return Idol.get_list(name=name, idol_type=idol_types, rarity=rarities)


# Create your views here.
def get_list(request):
    # リクエストから必要なパラメータを取得
    name = get_request_param(request, 'name')
    idol_types = get_request_params(request, 'type')
    rarities = get_request_params(request, 'rarity')
    fields = get_request_params(request, 'field')
    if fields is not None:
        fields.append("idol_id")
    offset = get_request_param(request, 'offset', '0')
    offset = int(offset) if offset.isdecimal() else 0
    if not isinstance(offset, int) or offset < 0:
        offset = 0
    limit = get_request_param(request, 'limit')
    limit = int(limit) if limit is not None and limit.isdecimal() else None
    if limit is not None and limit < 0:
        limit = None

    # アイドルリストを取得
    try:
        idol_list = Idol.get_list(name=name, idol_type=idol_types, rarity=rarities)
    except Idol.DoesNotExist:
        return JSONResponseNotFound()

    # ハッシュリスト形式に変換
    response_data = {
        'count': idol_list.count(),
        'results': {},
    }
    idol_list = idol_list[offset:] if limit is None else idol_list[offset:offset+limit]
    for idol in idol_list:
        data = idol.get_dict()
        if fields is not None:
            data = {k: v for k, v in data.items() if k in fields}
        response_data['results'][idol.idol_id] = data

    return JSONResponse(response_data)
