from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet  # Make sure this import is correct

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
