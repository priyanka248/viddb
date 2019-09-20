"""vidgyor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView # new
from django.conf import settings
from django.conf.urls.static import static
#from django.urls import include, path

urlpatterns = [
    url(r'^vids/', include('vids.urls')),
   # url(r'^login/$', auth_views.login, name='login'),
    #url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
    #url('', TemplateView.as_view(template_name='home.html'), name='home'), # new
    #url('edit.html',TemplateView.as_view(template_name='edit.html'), name='edit')


]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
