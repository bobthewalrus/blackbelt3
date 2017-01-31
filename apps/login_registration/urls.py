from django.conf.urls import url
from views import index, loginvalidate, registervalidate, success, logout, addpoke
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^loginvalidate$', loginvalidate, name='loginvalidate'),
    url(r'^registervalidate$', registervalidate, name='registervalidate'),
    url(r'^success$', success, name='success'),
    url(r'^logout$', logout, name='logout'),
    url(r'^addpoke/(?P<id>\d+)', addpoke, name='addpoke')
]
