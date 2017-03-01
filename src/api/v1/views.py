from collections import OrderedDict

from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView


class APIRootView(APIView):
    def get(self, request):
        return Response(OrderedDict(sorted(dict(
            allies=reverse('api:v1:ally-list', request=request),
            civilians=reverse('api:v1:civilian-list', request=request),
            monsters=reverse('api:v1:monster-list', request=request),
            rangers=reverse('api:v1:ranger-list', request=request),
            series=reverse('api:v1:series-list', request=request),
            villains=reverse('api:v1:villain-list', request=request),
            weapons=reverse('api:v1:weapon-list', request=request),
            zords=reverse('api:v1:zord-list', request=request),
        ).items(), key=lambda t: t[0])))
