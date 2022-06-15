from rest_framework import generics 
from movielist.models import MovieList, OttPlatform, MovieReview
from movielist.api.serializers import MovieListSerializer, OttPlatformSerializer, MovieReviewSerializer


class MovieReviewView(generics.ListCreateAPIView):
	queryset = MovieReview.objects.all()
	serializer_class = MovieReviewSerializer

class MovieReviewDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = MovieReview.objects.all()
	serializer_class = MovieReviewSerializer


class OTTplatformView(generics.ListCreateAPIView):
	queryset = OttPlatform.objects.all()
	serializer_class =OttPlatformSerializer

class OTTplatformDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = OttPlatform.objects.all()
	serializer_class = OttPlatform 


class MovieListView(generics.ListCreateAPIView):
	queryset = MovieList.objects.all()
	serializer_class =  MovieListSerializer

class MovieListDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = MovieList.objects.all()
	serializer_class = MovieListSerializer
