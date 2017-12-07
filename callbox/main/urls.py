from rest_framework.routers import DefaultRouter
from .viewsets import AdvertsViewSet, UsersViewSet

router = DefaultRouter()
router.register('adverts', AdvertsViewSet, base_name='advert')
router.register('users', UsersViewSet, base_name='user')

urlpatterns = router.urls

