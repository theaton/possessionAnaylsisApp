from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.game_log, name='Game'),
    url(r'^index/(?P<game_id>\d+)/$', views.index, name='index')
]
