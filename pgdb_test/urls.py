from django.urls import path, include
from .views import CustomerViewSet
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'customer', CustomerViewSet, basename='customer')

urlpatterns = [
    path('api/', include(router.urls))
]
