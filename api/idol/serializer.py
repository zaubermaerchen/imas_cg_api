# coding: utf-8
from rest_framework import serializers
from data.models import Idol


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idol
        fields = [
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
            'hash',
        ]
