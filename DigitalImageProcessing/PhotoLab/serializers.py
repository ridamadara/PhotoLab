from rest_framework import serializers
from .models import User
from .models import Client


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
    image = serializers.ImageField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['url', 'username', 'email', 'is_staff']
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        # fields = ['url', 'username', 'email', 'is_staff']
        fields = '__all__'
