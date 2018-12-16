# -*- coding: utf-8 -*-
from rest_framework import generics
from .serializer import ListSerializer
from data.models import Skill, SkillValue
from api.response import JSONResponse, JSONResponseNotFound


class ListView(generics.ListAPIView):
    queryset = Skill.objects.filter(skill_id__gte=1)
    serializer_class = ListSerializer


# Create your views here.
def get_list(request):
    # スキルリストを取得
    try:
        skill_list = Skill.objects.filter(skill_id__gte=1)
    except Skill.DoesNotExist:
        return JSONResponseNotFound()

    # ハッシュリスト形式に変換
    response_data = {}
    for skill in skill_list:
        data = skill.get_dict()
        data['skill_value_list'] = SkillValue.get_value_list(skill.skill_value_id)
        response_data[skill.skill_id] = data

    return JSONResponse(response_data)