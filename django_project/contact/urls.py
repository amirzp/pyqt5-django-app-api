from .views import ContactView, UserView
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views

router = routers.DefaultRouter()
router.register('list', ContactView)
router.register('user', UserView)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),
]
