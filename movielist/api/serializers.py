from rest_framework import serializers
from movielist.models import MovieList, OttPlatform, MovieReview


class MovieReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieReview
        exclude = ('movielist',) 

class MovieListSerializer(serializers.ModelSerializer):

    reviews = MovieReviewSerializer(many=True, read_only=True)

    class Meta:
        model = MovieList
        fields = "__all__"


class OttPlatformSerializer(serializers.ModelSerializer):

    movielist = MovieListSerializer(many=True, read_only=True)

    class Meta:
        model = OttPlatform
        fields = "__all__"