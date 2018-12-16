# coding: utf-8
from rest_framework import serializers
from data.models import Skill, SkillValue


class ListSerializer(serializers.ModelSerializer):
    skill_value_list = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Skill
        fields = [
            'skill_id',
            'target_unit',
            'target_member',
            'target_type',
            'target_num',
            'target_param',
            'skill_value_id',
            'skill_value_list',
            'comment'
        ]

    @staticmethod
    def get_skill_value_list(obj):
        return SkillValue.get_value_list(obj.skill_value_id)


class Costar(object):
    def __init__(self, name, count):
        self.name = name
        self.count = count


class CostarSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    count = serializers.IntegerField()

    def create(self, validated_data):
        return Costar(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.count = validated_data.get('count', instance.count)
        return instance
