from .models import Company,Industry
from .serializers import CompanySerializer,IndustrySerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class CompanyViewSet(ModelViewSet):
 
    queryset           = Company.objects.all().order_by('id')
    serializer_class   = CompanySerializer
    permission_classes = [IsAuthenticated]


    filter_backends    = [DjangoFilterBackend,SearchFilter,OrderingFilter]

    filterset_fields   = ['city','industry__name','company_name']
    search_fields      = ['company_name','industry__name']
    ordering_fields    = ['company_name','id']


class IndustryViewSet(ModelViewSet):

    queryset           = Industry.objects.all().order_by('id')
    serializer_class   = IndustrySerializer
    permission_classes = [IsAuthenticated]

    filter_backends    = [SearchFilter,OrderingFilter]

    search_fields      = ['name']
    ordering_fields    = ['name', 'id']

    