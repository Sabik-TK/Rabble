from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import (
    Education,
    Profile,
    Experience,
    Skill,
    SkilledUsers
)

from .serializers import (
    ProfileSerializer,
    EducationSerializer,
    ExperienceSerializer,
    SkillSerializer,
    SkilledUsersSerializer
)

# Profile Views 

class ProfileViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    queryset           = Profile.objects.all().order_by('id')
    serializer_class   = ProfileSerializer

    filter_backends    = [DjangoFilterBackend,SearchFilter,OrderingFilter]

    filterset_fields   = ['title','state','city']
    search_fields      = ['first_name','full_name','title']
    ordering_fields    = ['created', 'id']

class EducationViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    queryset           = Education.objects.all().order_by('id')
    serializer_class   = EducationSerializer

class ExperienceViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    queryset           = Experience.objects.all().order_by('id')
    serializer_class   = ExperienceSerializer


class SkillViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    queryset           = Skill.objects.all().order_by('id')
    serializer_class   = SkillSerializer

class SkilledUsersViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    queryset           = SkilledUsers.objects.all().order_by('id')
    serializer_class   = SkilledUsersSerializer