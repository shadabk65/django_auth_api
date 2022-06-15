from django.contrib import admin
from movielist.models import MovieList, OttPlatform, MovieReview
# Register your models here.

admin.site.register(MovieList)
admin.site.register(OttPlatform)
admin.site.register(MovieReview)
