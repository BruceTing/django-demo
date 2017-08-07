from django.conf.urls import url

from . import views

app_name = 'demoapp'
urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^index1/', views.index1, name='index1'),
    url(r'^save_user/', views.save_user, name='save_user'),
    url(r'^save_data/', views.save_data, name='save_data'),
    url(r'^list/', views.list, name='list'),
    url(r'^test/', views.test, name='test')
]
