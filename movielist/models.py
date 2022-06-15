from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


MOVIE_CHOICES = (
    ("Hollywood", "Hollywood"),
    ("Bollywood", "Bollywood"),
    ("Tollywood", "tollywood"),
)




class OttPlatform(models.Model):
	name = models.CharField(max_length=20)
	about = models.CharField(max_length=50)
	website = models.URLField(max_length=100)

	def __str__(self):
		return self.name



class MovieList(models.Model):
	title = models.CharField(max_length=50)
	descriptions = models.CharField(max_length=100)
	active = models.BooleanField(default=True)
	platform = models.ForeignKey(OttPlatform, on_delete=models.CASCADE, related_name="movielist" )
	industry = models.CharField(max_length=20, choices=MOVIE_CHOICES, default='Hollywood' )
	created = models.DateTimeField(auto_now_add= True)
	

	def __str__(self):
		return self.title


class MovieReview(models.Model):
	rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
	descriptions = models.CharField(max_length=100)
	movielist = models.ForeignKey(MovieList, on_delete=models.CASCADE, related_name="reviews")
	created = models.DateTimeField(auto_now_add=True)
	update = models.DateTimeField(auto_now= True)


	def __str__(self):
		return str(self.rating)+ " | " + self.movielist.title
		