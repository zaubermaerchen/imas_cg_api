# -*- coding: utf-8 -*-
from api.response import JSONResponse, JSONResponseNotFound
from data.models import Skill, SkillValue


# Create your views here.
def get_list(request):
    # スキルリストを取得
    try:
        skill_list = Skill.objects.filter(skill_id__gte=1)
    except Skill.DoesNotExist:
        return JSONResponseNotFound()

    # ハッシュリスト形式に変換
    hash_list = {}
    for skill in skill_list:
        hash_object = skill.convert_hash()
        hash_object['skill_value_list'] = SkillValue.get_value_list(skill.skill_value_id)
        hash_list[skill.skill_id] = hash_object

    return JSONResponse(hash_list)