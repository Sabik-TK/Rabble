from . models import Job,Application,JobSkill
from rest_framework import serializers


class ApplicationSerializer(serializers.ModelSerializer):

    position = serializers.ReadOnlyField(source='job.title')
    company  = serializers.ReadOnlyField(source='job.company.company_name')
    name     = serializers.ReadOnlyField(source= 'user.full_name')
    email    = serializers.ReadOnlyField(source= 'user.user.email')
    phone    = serializers.ReadOnlyField(source= 'user.user.mobile')


    class Meta:
        model = Application
        fields ='__all__'
    
class JobSkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobSkill
        fields ='__all__'
        
    def to_representation(self, instance):
        rep = super(JobSkillSerializer, self).to_representation(instance)
        rep['job'] = f'{instance.job.company.company_name} - {instance.job.title}' 
        rep['skill'] = instance.skill.name
        return rep

class JobSerializer(serializers.ModelSerializer):

    preferred_skills = serializers.StringRelatedField(many=True,read_only=True)
    applicants       = serializers.StringRelatedField(many=True,read_only=True)

    class Meta:
        model = Job
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(JobSerializer, self).to_representation(instance)
        rep['company'] = instance.company.company_name
        return rep
   