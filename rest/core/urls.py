from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = 'core'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),


]
