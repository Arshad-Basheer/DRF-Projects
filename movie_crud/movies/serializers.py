from django.db.models import Model
from rest_framework import serializers
from movies.models import Movie

# class MovieSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=30)
#     director = serializers.CharField(max_length=30)
#     language = serializers.CharField(max_length=30)
#     year = serializers.IntegerField()
#     rating = serializers.FloatField()
#     runtime = serializers.IntegerField()
#
#     def create(self, validated_data):
#         m=Movie.objects.create(**validated_data)
#         return m
#
#     def update(self, i, validated_data):
#         i.title = validated_data.get('title',i.title)
#         i.director = validated_data.get('director', i.director)
#         i.language = validated_data.get('language', i.language)
#         i.year = validated_data.get('year', i.year)
#         i.rating = validated_data.get('rating', i.rating)
#         i.runtime = validated_data.get('runtime', i.runtime)
#
#         i.save()
#
#         return i

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

        # or
        # 
        # fields = ['title','director'......]

from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','email','first_name','last_name']

    def create(self, validated_data):
        u = User.objects.create_user(**validated_data)
        return u