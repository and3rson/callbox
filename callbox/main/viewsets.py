from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from .serializers import UserSerializer, AdvertSerializer
from .models import Advert


class AdvertsViewSet(ModelViewSet):
    """
    list:
    Get all adverts.

    retrieve:
    Get one advert by ID.

    create:
    Create new advert.

    partial_update:
    Update advert by ID.

    delete:
    Delete existing advert by ID.
    """
    serializer_class = AdvertSerializer
    queryset = Advert.objects.all().order_by('-date_created')
    http_method_names = ['get', 'post', 'patch', 'delete']

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            return serializer.save(user_id=self.request.user.id)
        return serializer.save()


class UsersViewSet(ModelViewSet):
    """
    list:
    Get all users.

    retrieve:
    Get one user by ID;
    """
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('username')
    http_method_names = ['get']

