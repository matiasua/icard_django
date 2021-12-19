from django.contrib.auth.models import Permission
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from users.models import User
from users.api.serializers import UserSerializer


class UserApiViewSet(ModelViewSet):
    # quien puede utilizar los endpoint de UserApiViewSet
    permission_classes = [IsAdminUser]
    
    serializer_class = UserSerializer

    # a que modelo vamos a atacar
    queryset = User.objects.all()