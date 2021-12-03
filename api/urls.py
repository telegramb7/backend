from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, AnketViewSet, LikeViewSet, MatchViewSet

router = SimpleRouter()
router.register("user", UserViewSet, basename="user")
router.register("anket", AnketViewSet, basename="anket")
router.register("like", LikeViewSet, basename="like")
router.register("match", MatchViewSet, basename="match")

urlpatterns = router.urls
