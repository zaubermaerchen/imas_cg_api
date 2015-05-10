# -*- coding: utf-8 -*-
from api.response import JSONResponse, JSONResponseNotFound
from data.models import IdolName


# Create your views here.
def get_list(request):
    try:
        idol_names = IdolName.objects.all()
    except IdolName.DoesNotExist:
        return JSONResponseNotFound()

    response_data = {'names': []}
    for idol_name in idol_names:
        response_data['names'].append(idol_name.name)

    return JSONResponse(response_data)