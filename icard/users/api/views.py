from django.contrib.auth.models import Permission
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.hashers import make_password

from users.models import User
from users.api.serializers import UserSerializer


class UserApiViewSet(ModelViewSet):
    # quien puede utilizar los endpoint de UserApiViewSet
    permission_classes = [IsAdminUser]

    serializer_class = UserSerializer

    # a que modelo vamos a atacar
    queryset = User.objects.all()

    # nos permite registrar un usuario y encriptar la contrasena.
    def create(self, request, *args, **kwargs):
      # Obtiene la contraseña, la encripta
        request.data['password'] = make_password(request.data['password'])
        return super().create(request, *args, **kwargs)

  # Nos permite actualizar la password y encriptarla ya creado el usuario.
    def partial_update(self, request, *args, **kwargs):
        password = request.data['password']

        if password:
            request.data['password'] = make_password(password)
        else:
          request.data['password'] = request.user.password
        return super().update(request, *args, **kwargs)