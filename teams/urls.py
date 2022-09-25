from django.urls import path, include
from rest_framework import routers
from . import views as team_views

router = routers.DefaultRouter()
router.register(r'trainer', team_views.TrainerViewSet)
router.register(r'team', team_views.TeamViewSet)

urlpatterns = [

    path('', include(router.urls)),

    # Pokemon
    path('pokemon/', team_views.PokemonList.as_view(), name='pokemon-list'),
    path('pokemon/<int:pk>/', team_views.PokemonDetail.as_view(), name='pokemon-detail'),
    path('pokemon/', team_views.PokemonCreate.as_view(), name='pokemon-create'),
    path('pokemon/<int:pk>/', team_views.PokemonUpdate.as_view(), name='pokemon-update'),
    path('pokemon/<int:pk>/', team_views.PokemonDelete.as_view(), name='pokemon-delete'),

]
