"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView
from rest_framework import routers

from powerrangers.allies.views import AllyModelViewSet
from powerrangers.civilians.views import CivilianModelViewSet
from powerrangers.monsters.views import MonsterModelViewSet
from powerrangers.rangers.views import RangerModelViewSet
from powerrangers.series.views import EpisodeModelViewSet, SeasonModelViewSet, SeriesModelViewSet
from powerrangers.villains.views import VillainModelViewSet
from powerrangers.weapons.views import WeaponModelViewSet
from powerrangers.zords.views import ZordModelViewSet

urlpatterns = [
    path('schema', SpectacularAPIView.as_view(), name='schema'),
    path('docs', SpectacularRedocView.as_view(url_name='schema'), name='docs'),
    path('admin/', admin.site.urls),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico'))
]

router = routers.DefaultRouter(trailing_slash=False)
router.register('allies', AllyModelViewSet, basename='allies')
router.register('civilians', CivilianModelViewSet, basename='civilians')
router.register('episodes', EpisodeModelViewSet, basename='episodes')
router.register('monsters', MonsterModelViewSet, basename='monsters')
router.register('rangers', RangerModelViewSet, basename='rangers')
router.register('seasons', SeasonModelViewSet, basename='seasons')
router.register('series', SeriesModelViewSet, basename='series')
router.register('series/(?P<series_pk>[^/.]+)/seasons', SeasonModelViewSet, basename='series-seasons')
router.register('villains', VillainModelViewSet, basename='villains')
router.register('weapons', WeaponModelViewSet, basename='weapons')
router.register('zords', ZordModelViewSet, basename='zords')

urlpatterns += router.urls
