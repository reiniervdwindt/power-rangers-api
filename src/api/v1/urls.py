from django.conf.urls import url

from api.v1.allies.views import AllyDetailView, AllyListView
from api.v1.civilians.views import CivilianDetailView, CivilianListView
from api.v1.monsters.views import MonsterDetailView, MonsterListView
from api.v1.rangers.views import RangerDetailView, RangerListView
from api.v1.series.views import SeriesDetailView, SeriesListView
from api.v1.views import APIRootView
from api.v1.villains.views import VillainDetailView, VillainListView
from api.v1.weapons.views import WeaponDetailView, WeaponListView
from api.v1.zords.views import ZordDetailView, ZordListView

urlpatterns = [
    url(r'^$', APIRootView.as_view(), name='api-root'),

    url(r'^allies$', AllyListView.as_view(), name='ally-list'),
    url(r'^allies/(?P<pk>\d+)$', AllyDetailView.as_view(), name='ally-detail'),

    url(r'^civilians$', CivilianListView.as_view(), name='civilian-list'),
    url(r'^civilians/(?P<pk>\d+)$', CivilianDetailView.as_view(), name='civilian-detail'),

    url(r'^monsters$', MonsterListView.as_view(), name='monster-list'),
    url(r'^monsters/(?P<pk>\d+)$', MonsterDetailView.as_view(), name='monster-detail'),

    url(r'^rangers$', RangerListView.as_view(), name='ranger-list'),
    url(r'^rangers/(?P<pk>\d+)$', RangerDetailView.as_view(), name='ranger-detail'),

    url(r'^series$', SeriesListView.as_view(), name='series-list'),
    url(r'^series/(?P<pk>\d+)$', SeriesDetailView.as_view(), name='series-detail'),

    url(r'^villains$', VillainListView.as_view(), name='villain-list'),
    url(r'^villains/(?P<pk>\d+)$', VillainDetailView.as_view(), name='villain-detail'),

    url(r'^weapons$', WeaponListView.as_view(), name='weapon-list'),
    url(r'^weapons/(?P<pk>\d+)$', WeaponDetailView.as_view(), name='weapon-detail'),

    url(r'^zords$', ZordListView.as_view(), name='zord-list'),
    url(r'^zords/(?P<pk>\d+)$', ZordDetailView.as_view(), name='zord-detail'),
]
