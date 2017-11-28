from django.conf.urls import url
from . import views


app_name = 'puzzle'

urlpatterns = [
    # /puzzle/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /puzzle/79/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    url(r'^add/$', views.CreatePuzzleView.as_view(), name='add-puzzle'),

    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
]
