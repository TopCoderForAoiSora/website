from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Puzzle(models.Model):
    location = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    point = models.PositiveSmallIntegerField()
    content = models.TextField(max_length=1000)
    answer = models.CharField(max_length=100)
    logo = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('puzzle:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.location + " - " + self.title + " - " + str(self.point)


class PlayerGameHistory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    score = models.PositiveSmallIntegerField()
    solved = models.ManyToManyField(Puzzle, related_name="solved", blank=True)
    toSolve = models.ManyToManyField(Puzzle, related_name="toSolve", blank=True)

    def __str__(self):
        return self.user.username + " - " + str(self.score)

