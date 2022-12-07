import base64

from django.core.files.base import ContentFile
from rest_framework import serializers, validators
from posts.models import Comment, Group, Post, Follow, User

from .exceptions import CantSubscribeToYourSelf


class Base64ImageField(serializers.ImageField):
    
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            # ...начинаем декодировать изображение из base64.
            # Сначала нужно разделить строку на части.
            format, imgstr = data.split(';base64,')  
            # И извлечь расширение файла.
            ext = format.split('/')[-1]  
            # Затем декодировать сами данные и поместить результат в файл,
            # которому дать название по шаблону.
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super().to_internal_value(data)


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        fields = ('id', 'author', 'text', 'group', 'image', 'pub_date')
        read_only_fields = ('author',)
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title', 'slug', 'description')
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        default=serializers.CurrentUserDefault(),
        read_only=True,
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
    )

    class Meta:
        fields = ('user', 'following',)
        read_only_fields = ('user',)
        model = Follow
        validators = [
            validators.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following',),
                message='Вы не можете повторно подписаться',
            )
        ]

    def validate(self, data):
        """Нельзя подписываться на себя."""
        user = self.context['request'].user
        following = data['following']

        if user == following:
            raise CantSubscribeToYourSelf(
                {'detail': 'Вы не можете подписаться на себя'})
        return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('author',)
        model = Comment
