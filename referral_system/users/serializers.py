from rest_framework.serializers import SerializerMethodField, ModelSerializer
from rest_framework.exceptions import ValidationError

from .models import User


class UserCreateSerializer(ModelSerializer):
    """Сериализатор авторизации пользователя."""

    class Meta:
        model = User
        fields = ('phone_number', 'code')


class UserReadSerializer(ModelSerializer):
    """Сериализатор просмотра профиля пользователя."""

    is_invited = SerializerMethodField()

    class Meta:
        model = User
        fields = ('phone_number', 'is_invited',
                  'friend_invite_code', 'user_invite_code')

    def get_is_invited(self, obj):
        invited_users = User.objects.filter(
            friend_invite_code=obj.user_invite_code
            )
        return [user.phone_number for user in invited_users]


class UserUpdateSerializer(ModelSerializer):
    """Сериализатор для обновления информации о пользователе."""

    class Meta:
        model = User
        fields = ('code',)
