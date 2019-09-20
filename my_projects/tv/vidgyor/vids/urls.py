from django.conf.urls import url 

from . import views

urlpatterns = [
        #url('',views.index, name='index'),
        #url('upload/$',views.showvideo, name='showvideo'),
        url('search/$',views.showlist, name='showlist'),
        url('search/edit$',views.edit, name='edit'),

         #url(r'^login/$', auth_views.login, name='login'),
         #url(r'^logout/$', auth_views.logout, name='logout'),

        ]
