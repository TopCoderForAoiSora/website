from django.contrib import admin
from .models import Puzzle, PlayerGameHistory
from django.contrib.admin.templatetags.admin_list import admin_list_filter

class PuzzleAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'point', 'content', 'answer')
    list_filter = ['point']
    search_fields = ['title', 'content']


admin.site.register(Puzzle, PuzzleAdmin)


class PlayerGameHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'score')
    list_filter = ['score']
    search_fields = ['user__username']


admin.site.register(PlayerGameHistory, PlayerGameHistoryAdmin)