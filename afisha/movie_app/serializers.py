from rest_framework import serializers
from .models import *


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text movie stars'.split()


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'title description duration director'.split()


class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = 'name movies_count'.split()


class ShortReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text stars'.split()


class MoviesAndReviews(serializers.ModelSerializer):
    movies_reviews = ShortReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = 'title movies_reviews average_rate' .split()

