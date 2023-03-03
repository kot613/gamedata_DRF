from django.urls import path, include
from rest_framework import routers

from .views import GlobalSalesUpdateView, GameViewSet

router = routers.DefaultRouter()
router.register(r'games', GameViewSet)


urlpatterns = [
    path('games/<int:pk>/sales/', GlobalSalesUpdateView.as_view()),
    path('', include(router.urls)),

]
