from .models import Company,Industry
from .serializers import CompanySerializer,IndustrySerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

# Create your views here.
class CompanyViewSet(ModelViewSet):

    permission_classes = [AllowAny]
    queryset         = Company.objects.all().order_by('id')
    serializer_class = CompanySerializer


class IndustryViewSet(ModelViewSet):

    permission_classes = [AllowAny]
    queryset         = Industry.objects.all().order_by('id')
    serializer_class = IndustrySerializer
    