from django.conf.urls import url
from django.contrib.auth.decorators import login_required, permission_required
from . import views


app_name = 'puzzle'

urlpatterns = [
    # /puzzle/
    url(r'^$', login_required(views.IndexView.as_view()), name='index'),

    # /puzzle/79/
    url(r'^(?P<pk>[0-9]+)/$', login_required(views.PuzzleDetailView.as_view()), name='detail'),

    url(r'^(?P<puzzle_id>[0-9]+)/update/$', views.update_user_game_history, name='update'),

    url(r'^add/$', permission_required('user.is_superuser')(views.CreatePuzzleView.as_view()), name='add-puzzle'),

    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
]
