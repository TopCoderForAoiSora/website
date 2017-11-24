from django.db import models
from django.core.urlresolvers import reverse


class Puzzle(models.Model):
    location = models.IntegerField()
    title = models.CharField(max_length=100)
    point = models.IntegerField()
    content = models.CharField(max_length=1000)
    answer = models.CharField(max_length=100)
    logo = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('puzzle:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.location) + " - " + self.title + " - " + str(self.point)
