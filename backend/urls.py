from django.contrib import admin
from django.urls import path, include,re_path
from ML.views import index ,displayOptions
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index),
    path('options',displayOptions),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root':  settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)