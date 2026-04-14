from rest_framework import serializers
from .models import Monument

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MonumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monument
        fields = '__all__'

# Token Personalizado
class CustomTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['email'] = user.email

        return token