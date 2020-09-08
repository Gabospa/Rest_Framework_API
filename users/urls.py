from django.urls import path
from django.conf.urls import url
from users import views


urlpatterns = [
    path('user/', views.person_list, name = 'person_list'),
    url(r'^user/(?P<pk>[0-9]+)$', views.person_detail, name= 'person_detail')
]