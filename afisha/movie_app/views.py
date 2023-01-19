from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *

# Create your views here.


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




















