import time
from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.exceptions import ValidationError

from .models import User
from .serializers import (UserReadSerializer, UserCreateSerializer,
                          UserUpdateSerializer)


class UserCreateViewSet(ViewSet):
    """Вьюсет авторизации пользователя."""

    serializer_class = UserCreateSerializer

    @action(detail=False, methods=['post'])
    def authorization(self, request):
        """Регистрация и отправка кода авторизации."""

        phone_number = request.data.get('phone_number')
        if not phone_number:
            raise ValidationError({'error': 'Phone number is required'})
        try:
            current_user = User.objects.get(phone_number=phone_number)
            time.sleep(2)
            return Response({'message': f'Code sent to {phone_number}'},
                            status=status.HTTP_200_OK)
        except User.DoesNotExist:
            serializer = UserCreateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def confirm_code(self, request):
        """Подтверждение кода авторизации."""

        phone_number = request.data.get('phone_number')
        code = request.data.get('code')
        try:
            current_user = User.objects.get(phone_number=phone_number)
            if len(code) == 4:
                current_user.code = code
                current_user.save()
                serializer = UserUpdateSerializer(current_user)
                return Response(serializer.data,
                                status=status.HTTP_200_OK)
            return Response({'error': 'Invalid code!'},
                            status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'error': 'User not found'},
                            status=status.HTTP_404_NOT_FOUND)


class UserViewSet(ModelViewSet):
    """Вьюсет пользователя."""

    queryset = User.objects.all()
    serializer_class = UserReadSerializer

    @action(detail=True, methods=['post'])
    def confirm_invitation(self, request, pk=None):
        """Подтверждение пригласительного кода."""

        user = self.get_object()
        if user.friend_invite_code is not None:
            return Response({'error': 'Invite code already activated'},
                            status=status.HTTP_400_BAD_REQUEST)
        friend_invite_code = request.data.get('friend_invite_code')
        try:
            friend = User.objects.get(user_invite_code=friend_invite_code)
            if friend == user:
                return Response({'error': 'Cannot subscribe to yourself'},
                                status=status.HTTP_400_BAD_REQUEST)
            if (user.friend_invite_code is None
               and friend.user_invite_code == friend_invite_code):
                user.friend_invite_code = friend.user_invite_code
                user.save()
                serializer = self.get_serializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'error': 'Invite code already used'},
                            status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            Response({'error': 'Invite code already used'},
                     status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'error': 'Invalid invite code'},
                            status=status.HTTP_400_BAD_REQUEST)
