from django.contrib import admin
from .models import Puzzle, PlayerGameHistory
from django.contrib.admin.templatetags.admin_list import admin_list_filter

class PuzzleAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'point', 'content')


admin.site.register(Puzzle, PuzzleAdmin)


class PlayerGameHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'score')
    list_filter = ['score']


admin.site.register(PlayerGameHistory, PlayerGameHistoryAdmin)