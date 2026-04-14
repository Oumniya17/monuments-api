from rest_framework import viewsets
from .models import Monument
from .serializers import MonumentSerializer

from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenSerializer


class MonumentViewSet(viewsets.ModelViewSet):
    queryset = Monument.objects.all()
    serializer_class = MonumentSerializer

    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = '__all__'



@api_view(['POST'])
def register(request):
    user = User.objects.create_user(
        username=request.data['username'],
        email=request.data['email'],
        password=request.data['password']
    )
    return Response({"message": "Usuario creado"})

class CustomTokenView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer