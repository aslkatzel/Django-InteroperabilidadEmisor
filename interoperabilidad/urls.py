"""interoperabilidad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from login.views import *
from rest_framework import routers
from api_rest import views
from rest_framework.authtoken import views as view_token

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'eventos', views.EventoViewSet)
router.register(r'revistas', views.RevistaViewSet)
router.register(r'cursos', views.CursoViewSet)
router.register(r'proyectos', views.ProyectoViewSet)
router.register(r'libros', views.LibroViewSet)
router.register(r'participantes', views.ParticipanteViewSet)
router.register(r'investigadores', views.InvestigadorViewSet)

urlpatterns = [
    # URL Administrator
    #url(r'^admin/', admin.site.urls),
    # URL Index
    url(r'^index/', admin.site.urls),
    # URLs Aplication REST
    url(r'^api_rest/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', view_token.obtain_auth_token),
    # URLs Login
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^accounts/login/', 'django.contrib.auth.views.login'),
    url(r'^logout/', logout_page),
    # URL Registry
    url(r'^registros', include('registro.urls', namespace='registros')),
]
