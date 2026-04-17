from rest_framework import viewsets

from api.serializers import TestSerializer
from .models import Test
# Create your views here.

class TestView(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

