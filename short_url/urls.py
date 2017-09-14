from rest_framework_nested.routers import SimpleRouter, NestedSimpleRouter
from django.conf.urls import url, include

from .views import UrlViewSet, ShortUrlViewSet

router = SimpleRouter()
router.register(r'urls', UrlViewSet)
router.register(r'shorts', ShortUrlViewSet)

app_name = 'short_url'
urlpatterns = [
    url(r'^', include(router.urls)),
]
