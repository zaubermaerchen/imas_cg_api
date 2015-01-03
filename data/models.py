# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class BaseModel(models.Model):
    class Meta:
        abstract = True

    def get_dict(self):
        dictionary = self.__dict__
        del dictionary['_state']
        return dictionary


# スキル補正値管理テーブル
class SkillValue(BaseModel):
    id = models.IntegerField(primary_key=True)
    value1 = models.IntegerField(default=0)
    value2 = models.IntegerField(default=0)
    value3 = models.IntegerField(default=0)
    value4 = models.IntegerField(default=0)
    value5 = models.IntegerField(default=0)
    value6 = models.IntegerField(default=0)
    value7 = models.IntegerField(default=0)
    value8 = models.IntegerField(default=0)
    value9 = models.IntegerField(default=0)
    value10 = models.IntegerField(default=0)
    value11 = models.IntegerField(default=0)
    value12 = models.IntegerField(default=0)

    class Meta:
        db_table = 'skill_value'
        ordering = ['id']

    def __unicode__(self):
        return str(self.value1) + '%-' + str(self.value10) + '%'

    @classmethod
    def get_value_list(cls, skill_value_id):
        try:
            obj = cls.objects.get(pk=skill_value_id)
        except cls.DoesNotExist:
            obj = None

        # 配列に変換
        value_list = []
        for i in range(1, 13):
            value = 0
            if obj is not None:
                value = obj.__dict__['value' + str(i)]
            value_list.append(value)

        return value_list


# スキル情報管理テーブル
class Skill(BaseModel):
    TARGET_UNIT_CHOICES = (
        (0, 'Own'),
        (1, 'Rival'),
    )
    TARGET_MEMBER_CHOICES = (
        (0, 'Self'),
        (1, 'Front'),
        (2, 'Back'),
        (3, 'Front/Back'),
    )
    TARGET_TYPE_CHOICES = (
        (1, 'Cute'),
        (2, 'Cool'),
        (4, 'Passion'),
        (3, 'Cute/Cool'),
        (5, 'Cute/Passion'),
        (6, 'Cool/Passion'),
        (7, 'All'),
    )
    TARGET_PARAM_CHOICES = (
        (0, 'All'),
        (1, 'Offense'),
        (2, 'Defense'),
    )

    skill_id = models.IntegerField(db_column='id', primary_key=True)
    target_unit = models.IntegerField(choices=TARGET_UNIT_CHOICES, default=0)
    target_member = models.IntegerField(choices=TARGET_MEMBER_CHOICES, default=0)
    target_type = models.IntegerField(choices=TARGET_TYPE_CHOICES, default=1)
    target_num = models.IntegerField(default=-1)
    target_param = models.IntegerField(choices=TARGET_PARAM_CHOICES, default=0)
    skill_value = models.ForeignKey(SkillValue, default=0)
    comment = models.CharField(max_length=1024)

    class Meta:
        db_table = 'skill'
        ordering = ['skill_id']

    def __unicode__(self):
        return self.comment


# アイドル情報管理テーブル
class Idol(BaseModel):
    TYPE_CHOICES = (
        (0, 'Cute'),
        (1, 'Cool'),
        (2, 'Passion'),
    )
    RARITY_CHOICES = (
        (0, 'N'),
        (1, 'N+'),
        (2, 'R'),
        (3, 'R+'),
        (4, 'SR'),
        (5, 'SR+'),
    )

    idol_id = models.IntegerField(db_column='id', primary_key=True)
    name = models.CharField(max_length=1024)
    type = models.IntegerField(choices=TYPE_CHOICES, default=0)
    rarity = models.IntegerField(choices=RARITY_CHOICES, default=0)
    cost = models.IntegerField(default=1)
    offense = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    max_offense = models.IntegerField(default=0)
    max_defense = models.IntegerField(default=0)
    skill_name = models.CharField(max_length=1024, blank=True, default="")
    skill = models.ForeignKey(Skill, related_name="skill", default=0)
    hash = models.CharField(max_length=32)

    class Meta:
        db_table = 'idol'
        ordering = ['idol_id']
        index_together = [
            ['type', 'rarity']
        ]

    @classmethod
    def get_list(cls, idol_type=None, rarity=None):
        idol_list = cls.objects.all()

        if idol_type is not None:
            idol_list = idol_list.filter(type=idol_type)

        if rarity is not None:
            idol_list = idol_list.filter(rarity=rarity)

        return idol_list
