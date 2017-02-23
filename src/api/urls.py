from django.conf.urls import include, url
from django.views.generic import RedirectView
from rest_framework.reverse import reverse_lazy

urlpatterns = [
    url(r'^$', RedirectView.as_view(url=reverse_lazy('api:v1:api-root'), permanent=False)),
    url(r'^v1/', include('api.v1.urls', namespace='v1')),
]
