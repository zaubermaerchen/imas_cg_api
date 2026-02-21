# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.expressions import RawSQL
from django.utils import timezone
import collections

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
    value1 = models.FloatField(default=0)
    value2 = models.FloatField(default=0)
    value3 = models.FloatField(default=0)
    value4 = models.FloatField(default=0)
    value5 = models.FloatField(default=0)
    value6 = models.FloatField(default=0)
    value7 = models.FloatField(default=0)
    value8 = models.FloatField(default=0)
    value9 = models.FloatField(default=0)
    value10 = models.FloatField(default=0)
    value11 = models.FloatField(default=0)
    value12 = models.FloatField(default=0)

    class Meta:
        db_table = 'skill_value'
        ordering = ['id']

    def __str__(self):
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
    skill_value = models.ForeignKey(SkillValue, default=0, on_delete=models.PROTECT)
    comment = models.CharField(max_length=256)

    class Meta:
        db_table = 'skill'
        ordering = ['skill_id']

    def __str__(self):
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
    name = models.CharField(max_length=256)
    type = models.IntegerField(choices=TYPE_CHOICES, default=0)
    rarity = models.IntegerField(choices=RARITY_CHOICES, default=0)
    cost = models.IntegerField(default=1)
    offense = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    max_offense = models.IntegerField(default=0)
    max_defense = models.IntegerField(default=0)
    skill_name = models.CharField(max_length=256, blank=True, default='')
    skill = models.ForeignKey(Skill, related_name='skill', default=0, on_delete=models.PROTECT)
    skill2 = models.ForeignKey(Skill, related_name='skill2', default=0, on_delete=models.PROTECT)
    hash = models.CharField(max_length=32)

    class Meta:
        db_table = 'idol'
        ordering = ['idol_id']
        indexes = [
            models.Index(fields=['type', 'rarity'])
        ]

    @classmethod
    def get_list(cls, name=None, idol_type=None, rarity=None):
        idols = cls.objects.all()

        if name is not None and len(name) > 0:
            param = '*D+ ' + name
            idols = idols.annotate(
                name_match=RawSQL('MATCH(name) AGAINST (%s IN BOOLEAN MODE)', [param])
            ).filter(name_match__gt=0)

        if idol_type is not None:
            if isinstance(idol_type, list):
                if len(idol_type) > 0:
                    idols = idols.filter(type__in=idol_type)
            else:
                idols = idols.filter(type=idol_type)

        if rarity is not None:
            if isinstance(rarity, list):
                if len(rarity) > 0:
                    idols = idols.filter(rarity__in=rarity)
            else:
                idols = idols.filter(rarity=rarity)

        return idols


# アイドル名管理テーブル
class IdolName(BaseModel):
    name = models.CharField(max_length=255, primary_key=True)

    class Meta:
        db_table = 'idol_name'


# 劇場管理テーブル
class Cartoon(BaseModel):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=256, default='')
    date = models.DateField(default=timezone.now)
    idols = models.TextField(blank=True)
    comment = models.CharField(max_length=256, blank=True, default='')
    thumbnail_hash = models.CharField(max_length=32)

    class Meta:
        db_table = 'cartoon'
        ordering = ['id']

    @classmethod
    def get_list(cls, title=None, idols=None, start_at=None, end_at=None):
        cartoons = cls.objects.all()

        if title is not None and len(title) > 0:
            param = '*D+ ' + title
            cartoons = cartoons.annotate(
                title_match=RawSQL('MATCH(title) AGAINST (%s IN BOOLEAN MODE)', [param])
            ).filter(title_match__gt=0)

        if idols is not None and len(idols) > 0:
            param = '+' + ' +'.join(idols)
            cartoons = cartoons.annotate(
                idols_match=RawSQL('MATCH(idols) AGAINST (%s IN BOOLEAN MODE)', [param])
            ).filter(idols_match__gt=0)

        if start_at is not None:
            cartoons = cartoons.filter(date__gte=start_at)

        if end_at is not None:
            cartoons = cartoons.filter(date__lte=end_at)

        return cartoons

    @classmethod
    def get_costars(cls, name):
        idols = []
        cartoons = cls.get_list(idols=[name])
        for cartoon in cartoons:
            idols.extend(cartoon.idols.split())

        results = dict(collections.Counter(idols))
        del results[name]
        return results

