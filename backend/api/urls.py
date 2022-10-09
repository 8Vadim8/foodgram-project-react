from django.urls import include, path
from rest_framework import routers

from .views import RecipesViewSet, TagViewSet, UsersViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('users', UsersViewSet, basename='users')
router.register('tags', TagViewSet, basename='tags')
router.register('recipes', RecipesViewSet, basename='recipes')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
