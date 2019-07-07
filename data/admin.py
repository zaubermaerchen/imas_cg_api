# -*- coding: utf-8 -*-
from django.contrib import admin

from data.models import Idol, Skill, SkillValue, Cartoon


# Register your models here.
class IdolAdmin(admin.ModelAdmin):
    list_display = (
        'idol_id',
        'name',
        'type',
        'rarity',
        'cost',
        'offense',
        'defense',
        'max_offense',
        'max_defense',
        'skill_name',
        'skill',
        'skill2',
    )

    fieldsets = [
        (None, {
            'fields': ['idol_id', 'name']
        }),
        ('Status', {
            'fields': ['type', 'rarity', 'cost', 'offense', 'defense', 'max_offense', 'max_defense', 'hash']
        }),
        ('Skill', {
            'fields': ['skill_name', 'skill', 'skill2']
        }),
    ]

    search_fields = ['name']

admin.site.register(Idol, IdolAdmin)


class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'skill_id',
        'comment',
        'target_unit',
        'target_member',
        'target_type',
        'target_num',
        'target_param',
        'skill_value',
    )

    fieldsets = [
        (None, {
            'fields': ['skill_id', 'comment']
        }),
        ('Effect', {
            'fields': ['target_unit', 'target_member', 'target_type', 'target_num', 'target_param', 'skill_value']
        }),
    ]

    search_fields = ['comment']

admin.site.register(Skill, SkillAdmin)


class SkillValueAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'value1',
        'value2',
        'value3',
        'value4',
        'value5',
        'value6',
        'value7',
        'value8',
        'value9',
        'value10',
        'value11',
        'value12',
    )

    fieldsets = [
        (None, {
            'fields': ['id']
        }),
        ('Param', {
            'fields': [
                'value1',
                'value2',
                'value3',
                'value4',
                'value5',
                'value6',
                'value7',
                'value8',
                'value9',
                'value10',
                'value11',
                'value12',
            ]
        }),
        ]

admin.site.register(SkillValue, SkillValueAdmin)


class CartoonAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'date',
        'idols',
        'comment',
    )
    fieldsets = [
        (None, {
            'fields': ['id', 'title', 'date', 'idols', 'thumbnail_hash', 'comment']
        })
    ]

admin.site.register(Cartoon, CartoonAdmin)