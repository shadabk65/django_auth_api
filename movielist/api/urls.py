from django.urls import path
from movielist.api.views import MovieListView, MovieListDetail, OTTplatformView, OTTplatformDetail, MovieReviewView, MovieReviewDetail
urlpatterns = [
    path('movielist/', MovieListView.as_view(), name= 'movie-list'),
    path('movielist/<int:pk>/', MovieListDetail.as_view(), name= 'movie-detail'),
    
    path('platform/', OTTplatformView.as_view(), name= 'OTT-list'),
    path('platform/<int:pk>/', OTTplatformDetail.as_view(), name= 'OTT-detail'),

    path('<int:pk>/review/', MovieReviewView.as_view(), name= 'Review-list'),
    path('review/<int:pk>/', MovieReviewDetail.as_view(), name= 'Review-Detail'),

]