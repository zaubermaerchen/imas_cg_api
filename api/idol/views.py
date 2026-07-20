from rest_framework import generics

from data.models import Idol

from .pagination import SearchLimitOffsetPagination
from .serializer import SearchSerializer


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
