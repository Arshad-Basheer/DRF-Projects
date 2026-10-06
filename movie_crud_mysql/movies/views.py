from django.db.models import Model
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from movies.models import Movie

from movies.serializers import MovieSerializer
from rest_framework import status


# Create your views here.
# class MovieList(APIView):
#     def get(self,request):
#         m=Movie.objects.all()
#         s_ins = MovieSerializer(m,many=True)
#         return Response (data=s_ins.data)
#
# class MovieCreate(APIView):
#     def post(self,request):
#         s_ins = MovieSerializer(data=request.data)
#         if s_ins.is_valid():
#
#             # to get data after validation
#             # cleaned_data = s_ins.validated_data
#
#             s_ins.save()
#             return Response({"message":"Data inserted successfully"})
#         else:
#             return Response(s_ins.errors)
#
class MovieListCreate(APIView):
    def get(self,request):
        m=Movie.objects.all()
        s_ins = MovieSerializer(m,many=True)
        return Response (data=s_ins.data,status=status.HTTP_200_OK)

    def post(self,request):
        s_ins = MovieSerializer(data=request.data)
        if s_ins.is_valid():

            # to get data after validation
            # cleaned_data = s_ins.validated_data

            s_ins.save()
            return Response({"message":"Data inserted successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(s_ins.errors)

class RetrieveUpdateDelete(APIView):
    def get(self,request,i):
        m=get_object_or_404(Movie,id=i)
        s_ins = MovieSerializer(m)
        return Response(data=s_ins.data)

    def put(self,request,i):
        m=get_object_or_404(Movie,id=i)
        s_ins = MovieSerializer(m,request.data)
        if s_ins.is_valid():
            s_ins.save()
            return Response(s_ins.data)
        else:
            return Response(s_ins.errors)

    def patch(self,request,i):
        m=get_object_or_404(Movie,id=i)
        s_ins = MovieSerializer(m,request.data,partial=True)
        if s_ins.is_valid():
            s_ins.save()
            return Response(s_ins.data)
        else:
            return Response(s_ins.errors)


    def delete(self,request,i):
        m=get_object_or_404(Movie,id=i)
        m.delete()
        return Response({"message":"deleted"})