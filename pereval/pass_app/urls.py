from django.urls import include, path
from rest_framework import routers

from pass_app import views

router = routers.DefaultRouter()
router.register(r'pereval', views.PerevalViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('drf/', include('rest_framework.urls', namespace='rest_framework')),
]
