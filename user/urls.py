from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from user import views

urlpatterns = [

    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'kompany:home'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),

]