# -*- coding: utf-8 -*-
from api.response import JSONResponse, JSONResponseNotFound
from data.models import Idol


def get_request_param(request, key):
    value = None
    
    if key in request.POST:
        value = request.POST[key]
    elif key in request.GET:
        value = request.GET[key]
        
    return value
    

# Create your views here.
def get_list(request):
    # リクエストから必要なパラメータを取得
    idol_type = get_request_param(request, 'type')
    rarity = get_request_param(request, 'rarity')
    fields = None
    if get_request_param(request, 'fields') is not None:
        fields = get_request_param(request, 'fields').split(' ')
        fields.append("idol_id")

    # アイドルリストを取得
    try:
        idol_list = Idol.get_list(idol_type=idol_type, rarity=rarity)
    except Idol.DoesNotExist:
        return JSONResponseNotFound()

    # ハッシュリスト形式に変換
    response_data = {}
    for idol in idol_list:
        data = idol.get_dict()
        if fields is not None:
            data = {k: v for k, v in data.items() if k in fields}
        response_data[idol.idol_id] = data

    return JSONResponse(response_data)