from django.conf.urls import patterns, include, url
# -*- encoding: utf-8 -*-
# Descomente las siguientes dos líneas para que el admin:
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',

 url(r'^$','principal.views.lista_recetas'),
 url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
 
    # Ejemplos:
    # url(r'^$', 'recetario.views.home', name='home'),
    # url(r'^recetario/', include('recetario.foo.urls')),

    # Descomente la línea admin / doc continuación para habilitar la documentación de administración:
 url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Elimine el comentario de la siguiente línea para habilitar el administrador:
 url(r'^admin/', include(admin.site.urls)),
)