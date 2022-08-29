from rest_framework import viewsets
from rest_framework.permissions import AllowAny

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

    queryset         = Profile.objects.all().order_by('id')
    serializer_class = ProfileSerializer

class EducationViewSet(viewsets.ModelViewSet):

    queryset         = Education.objects.all().order_by('id')
    serializer_class = EducationSerializer

class ExperienceViewSet(viewsets.ModelViewSet):

    queryset         = Experience.objects.all().order_by('id')
    serializer_class = ExperienceSerializer


class SkillViewSet(viewsets.ModelViewSet):

    permission_classes = [AllowAny]
    queryset         = Skill.objects.all().order_by('id')
    serializer_class = SkillSerializer

class SkilledUsersViewSet(viewsets.ModelViewSet):

    queryset         = SkilledUsers.objects.all().order_by('id')
    serializer_class = SkilledUsersSerializer