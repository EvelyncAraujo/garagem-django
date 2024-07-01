from rest_framework.viewsets import ModelViewSet
from core.models import Acessorio
from core.serializers import AcessorioSerializer

class AcessorioViewSet (ModelViewSet):
    queryset = Acessorio.objects.order_by("descricao")  
    serializer_class = AcessorioSerializer