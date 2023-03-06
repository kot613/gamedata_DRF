from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Game
from .serializers import GameSerializer, GlobalSalesUpdateSerializer
from .utils import get_platforms_count, get_genres_count, GamesFilter


class GlobalSalesUpdateView(generics.RetrieveUpdateAPIView):
    """
    View to update the global_sale variable.
    Permissions - Authenticated, ReadOnly
    """
    queryset = Game.objects.all()
    serializer_class = GlobalSalesUpdateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class GameViewSet(viewsets.ModelViewSet):
    """
    ViewSet to display data.
    Permissions - AdminUser
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = GamesFilter

    def get_permissions(self):
        """
        Setting the level of access to data changes
        """
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    @action(methods=['get'], detail=False)
    def genres(self, request):
        """
        return a list of the number of games for each genre.
        permission method - GET
        """
        return Response(get_genres_count(Model=Game))

    @action(methods=['get'], detail=False)
    def platforms(self, request):
        """
        return a list of the number of games for each platform.
        permission method - GET
        """
        return Response(get_platforms_count(Model=Game))
