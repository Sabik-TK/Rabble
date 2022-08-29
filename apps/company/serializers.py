from . models import Industry,Company
from rest_framework import serializers


class IndustrySerializer(serializers.ModelSerializer):

    companies = serializers.StringRelatedField(many=True,read_only=True)

    class Meta:
        model = Industry
        fields =['id','name','companies']


class CompanySerializer(serializers.ModelSerializer):

    employees = serializers.StringRelatedField(many=True,read_only=True)

    class Meta:
        model = Company
        fields = ['id','company_name','photo','city','user','industry','employees']
        extra_kwargs = {'user': {'write_only': True}}

    def to_representation(self, instance):
        rep = super(CompanySerializer, self).to_representation(instance)
        rep['industry'] = instance.industry.name
        return rep