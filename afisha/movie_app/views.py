from django.shortcuts import render
from django.views import generic
from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .serializers import *
from .models import *

# Create your views here.


class DirectorViewSet(viewsets.mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

@api_view(['GET'])
def main_view(request, slug):
    if slug == 'movies':
        item = Movie.objects.all()
        serializer = MovieSerializer(item, many=True)
    elif slug == 'directors':
        item = Director.objects.all()
        serializer = DirectorSerializer(item, many=True)
    elif slug == 'reviews':
        item = Review.objects.all()
        serializer = ReviewSerializer(item, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def main_detail_view(request, slug, id):
    if slug == 'movies':
        item = Movie.objects.filter(id=id)
        serializer = MovieSerializer(item, many=True)
    elif slug == 'directors':
        item = Director.objects.filter(id=id)
        serializer = DirectorSerializer(item, many=True)
    elif slug == 'reviews':
        item = Review.objects.filter(id=id)
        serializer = ReviewSerializer(item, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def movies_and_reviews(request):
    movie = Movie.objects.all()
    serializer = MoviesAndReviews(movie, many=True)
    return Response(data=serializer.data)




















