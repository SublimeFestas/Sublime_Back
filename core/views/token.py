from rest_framework_simplejwt.views import TokenObtainPairView
from core.serializers import TokenSerializer

class TokenViewSet(TokenObtainPairView):
    serializer_class = TokenSerializer
