# -*- coding: utf-8 -*-
from api.response import JSONResponse, JSONResponseNotFound
from data.models import Cartoon
from datetime import datetime


def get_request_param(request, key, default_value=None):
    value = default_value

    if key in request.POST:
        value = request.POST[key]
    elif key in request.GET:
        value = request.GET[key]

    return value


def convert_datetime_object(datetime_string, datetime_format):
    if datetime_string is None or len(datetime_string) == 0:
        return None

    value = None
    try:
        value = datetime.strptime(datetime_string, datetime_format)
    finally:
        return value


# Create your views here.
def search(request):
    # リクエストから必要なパラメータを取得
    title = get_request_param(request, 'title')
    idols = get_request_param(request, 'idols')
    start_at = convert_datetime_object(get_request_param(request, 'start_at'), '%Y-%m-%d')
    end_at = convert_datetime_object(get_request_param(request, 'end_at'), '%Y-%m-%d')
    offset = int(get_request_param(request, 'offset', '0'))
    if offset < 0:
        offset = 0
    limit = int(get_request_param(request, 'limit', '10'))
    if limit < 0:
        limit = 10

    # ハッシュリスト形式に変換
    response_data = {'count': 0, 'results': []}
    try:
        cartoons = Cartoon.get_list(title, idols, start_at, end_at)
        response_data['count'] = cartoons.count()
        for cartoon in cartoons[offset:offset + limit]:
            response_data['results'].append(cartoon.get_dict())
    finally:
        return JSONResponse(response_data)