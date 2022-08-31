from .models import Application,Job,JobSkill
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter,OrderingFilter

from .serializers import (
     ApplicationSerializer,
     JobSkillSerializer,
     JobSerializer,
    )

from django_filters.rest_framework import (
    DjangoFilterBackend,
    )


class JobViewSet(ModelViewSet):

    permission_classes = [IsAuthenticated]
    queryset           = Job.objects.all().order_by('id')
    serializer_class   = JobSerializer

    filter_backends    = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    
    def get_filterset_kwargs(self):
        return {

        }
    filterset_fields = [
        'company__company_name',
        'company__industry',
        'employment_type',
        'company',
        'status',
        'title',
        'city',
        ]

    search_fields = [
        'company__company_name',
        'company__industry',
        'title',
        ]

    ordering_fields = [
        'created',
        'salary',
        ]

class JobSkillViewSet(ModelViewSet):

    permission_classes = [IsAuthenticated]
    queryset           = JobSkill.objects.all().order_by('id')
    serializer_class   = JobSkillSerializer


class ApplicationViewSet(ModelViewSet):

    permission_classes = [IsAuthenticated]
    queryset           = Application.objects.all().order_by('id')
    serializer_class   = ApplicationSerializer

    filter_backends    = [DjangoFilterBackend,OrderingFilter]

    filterset_fields   = ['job','user','status']
    ordering_fields    = ['created', 'id']
    