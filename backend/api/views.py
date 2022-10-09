from djoser.views import UserViewSet
from rest_framework import viewsets

from users.models import User
from .serializers import RecipesListSerializer, UserSerializer


from .serializers import TagSerializer
from recipes.models import Tag, Recipe


class UsersViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class RecipesViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipesListSerializer
