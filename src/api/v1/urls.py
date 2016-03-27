from rest_framework.routers import DefaultRouter

from api.v1.allies.views import AllyViewSet
from api.v1.civilians.views import CivilianViewSet
from api.v1.monsters.views import MonsterViewSet
from api.v1.rangers.views import RangersViewSet
from api.v1.series.views import SeriesViewSet
from api.v1.villains.views import VillainsViewSet
from api.v1.weapons.views import WeaponsViewSet
from api.v1.zords.views import ZordsViewSet

router = DefaultRouter()
router.register(r'allies', AllyViewSet, base_name='ally')
router.register(r'civilians', CivilianViewSet, base_name='civilian')
router.register(r'monsters', MonsterViewSet, base_name='monster')
router.register(r'rangers', RangersViewSet, base_name='ranger')
router.register(r'series', SeriesViewSet, base_name='series')
router.register(r'villains', VillainsViewSet, base_name='villain')
router.register(r'weapons', WeaponsViewSet, base_name='weapon')
router.register(r'zords', ZordsViewSet, base_name='zord')
urlpatterns = router.urls
