from django.urls import path, include
from rest_framework import routers
from . import views as team_views

router = routers.DefaultRouter()
router.register(r'trainer', team_views.TrainerViewSet)
router.register(r'team', team_views.TeamViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
