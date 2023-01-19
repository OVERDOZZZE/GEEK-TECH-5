from django.db import models

# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    @property
    def movies_count(self):
        return len(self.movies.all())


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.DurationField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return self.title

    @property
    def average_rate(self):
        count = self.movies_reviews.count()
        if count == 0:
            return f'No reviews yet'
        total = 0
        for i in self.movies_reviews.all():
            total += i.stars
        return total/count


CHOISES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)


class Review(models.Model):
    text = models.TextField(max_length=1000)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movies_reviews')
    stars = models.IntegerField(choices=CHOISES, default=0)

    def __str__(self):
        return self.text








