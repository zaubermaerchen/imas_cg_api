# coding: utf-8
from rest_framework import serializers
from data.models import Cartoon


class SearchSerializer(serializers.ModelSerializer):
    characters = serializers.SerializerMethodField(read_only=True)
    idols = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Cartoon
        fields = [
            'id',
            'title',
            'date',
            'characters',
            'idols',
            'comment',
            'thumbnail_hash',
        ]

    @staticmethod
    def get_characters(obj):
        return obj.idols.split()

    @staticmethod
    def get_idols(obj):
        return obj.idols.split()


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
