from .views import ContactView
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('list', ContactView)

urlpatterns = [
    path('v1/', include(router.urls)),
]