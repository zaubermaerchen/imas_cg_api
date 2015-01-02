# -*- coding: utf-8 -*-
import simplejson
from django.http import HttpResponse, HttpResponseNotFound

from data.models import Skill, SkillValue


# Create your views here.
def get_list(request):
    # スキルリストを取得
    try:
        skill_list = Skill.objects.filter(skill_id__gte=1)
    except Skill.DoesNotExist:
        response = HttpResponseNotFound(content_type='application/json')
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
        response['Access-Control-Max-Age'] = '1000'
        response['Access-Control-Allow-Headers'] = '*'
        return response

    # ハッシュリスト形式に変換
    hash_list = {}
    for skill in skill_list:
        hash_object = skill.convert_hash()
        hash_object['skill_value_list'] = SkillValue.get_value_list(skill.skill_value_id)
        hash_list[skill.skill_id] = hash_object

    # JSON形式に変換
    json = simplejson.dumps(hash_list, sort_keys=True)

    # create HTTP response
    response = HttpResponse(json, content_type='application/json')
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
    response['Access-Control-Max-Age'] = '1000'
    response['Access-Control-Allow-Headers'] = '*'

    return response