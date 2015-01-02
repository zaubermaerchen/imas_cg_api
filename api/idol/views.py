# -*- coding: utf-8 -*-
from api.response import JSONResponse, JSONResponseNotFound
from data.models import Idol


# Create your views here.
def get_list(request):
    # リクエストから必要なパラメータを取得
    idol_type = None
    rarity = None
    fields = None
    if 'type' in request.REQUEST:
        idol_type = request.REQUEST['type']
    if 'rarity' in request.REQUEST:
        rarity = request.REQUEST['rarity']
    if 'fields' in request.REQUEST:
        fields = request.REQUEST['fields'].split(' ')
        fields.append("idol_id")

    # アイドルリストを取得
    try:
        idol_list = Idol.get_list(idol_type=idol_type, rarity=rarity)
    except Idol.DoesNotExist:
        return JSONResponseNotFound()

    # ハッシュリスト形式に変換
    hash_list = {}
    for idol in idol_list:
        hash_list[idol.idol_id] = idol.convert_hash(fields)

    return JSONResponse(hash_list)