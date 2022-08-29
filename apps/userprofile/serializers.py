from . models import Profile, Education,Experience,Skill,SkilledUsers
from rest_framework import serializers

 
class EducationSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source= 'profile.user.email')

    class Meta:
        model = Education
        fields = ['id','profile','user','title','institution','year','place']
        extra_kwargs={'profile': {'write_only': True}}
        

class ExperienceSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source= 'profile.user.email')

    class Meta:
        model = Experience
        fields = ['id','profile','user','company','designation','start_date','end_date']
        extra_kwargs={'profile': {'write_only': True}}

class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = '__all__'


class SkilledUsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = SkilledUsers
        fields = '__all__'  
    
    def to_representation(self, instance):
        rep = super(SkilledUsersSerializer, self).to_representation(instance)
        rep['user'] = instance.user.user.email
        rep['skill'] = instance.skill.name
        return rep

class ProfileSerializer(serializers.ModelSerializer):

    education       = EducationSerializer(many=True, read_only=True)
    experience      = ExperienceSerializer(many=True, read_only=True)
    skills          = serializers.StringRelatedField(many=True, read_only=True)
    email           = serializers.ReadOnlyField(source='user.email')
    
    class Meta:
        model = Profile
        fields ='__all__'

