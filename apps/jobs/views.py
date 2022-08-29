from .models import Application,Job,JobSkill
from .serializers import ApplicationSerializer,JobSerializer,JobSkillSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class JobViewSet(ModelViewSet):

    permission_classes = [AllowAny]
    queryset         = Job.objects.all().order_by('id')
    serializer_class = JobSerializer

class JobSkillViewSet(ModelViewSet):

    # permission_classes = [AllowAny]
    queryset         = JobSkill.objects.all().order_by('id')
    serializer_class = JobSkillSerializer


class ApplicationViewSet(ModelViewSet):

    # permission_classes = [AllowAny]
    queryset         = Application.objects.all().order_by('id')
    serializer_class = ApplicationSerializer
    