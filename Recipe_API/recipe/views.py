from django.db.models import Model
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from recipe.models import Recipe
from recipe.serializers import RecipeSerializer
from rest_framework import status

# Create your views here.
class RecipeListCreate(APIView):
    def get(self,request):
        r=Recipe.objects.all()
        s_ins = RecipeSerializer(r,many=True)
        return Response(data=s_ins.data,status=status.HTTP_200_OK)

    def post(self,request):
        s_ins = RecipeSerializer(data=request.data)
        if s_ins.is_valid():
            s_ins.save()
            return Response(s_ins.data,status=status.HTTP_201_CREATED)
        else:
            return Response(s_ins.errors,status=status.HTTP_400_BAD_REQUEST)

class RecipeRetrieveUpdateDelete(APIView):

    def get(self,request,id):
        r=get_object_or_404(Recipe,id=id)
        s_ins = RecipeSerializer(r)
        return Response(data=s_ins.data,status=status.HTTP_200_OK)

    def put(self,request,id):
        r=get_object_or_404(Recipe,id=id)
        s_ins = RecipeSerializer(r,request.data)
        if s_ins.is_valid():
            s_ins.save()
            return Response(s_ins.data)
        else:
            return Response(s_ins.errors,status=status.HTTP_404_NOT_FOUND)

    def patch(self,request,id):
        r = get_object_or_404(Recipe, id=id)
        s_ins = RecipeSerializer(r, request.data,partial=True)
        if s_ins.is_valid():
            s_ins.save()
            return Response(s_ins.data)
        else:
            return Response(s_ins.errors,status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,id):
        r=get_object_or_404(Recipe,id=id)
        r.delete()
        return Response({"message":"Data Deleted Successfully"})