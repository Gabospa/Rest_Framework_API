from django.conf.urls import url
from catalog import views

urlpatterns = [
    url(r'^album$', views.album_list),
    url(r'^album/(?P<pk>[0-9]+)$', views.album_detail)
]