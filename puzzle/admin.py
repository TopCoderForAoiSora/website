from django.contrib import admin
from .models import Puzzle, PlayerGameHistory, TestManyToMany

admin.site.register(Puzzle)
admin.site.register(PlayerGameHistory)
admin.site.register(TestManyToMany)
