from django.db import models
from apps.account.models import Account

# Create your models here.
class Industry(models.Model):
    name =  models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

class Company(models.Model):

    user             = models.ForeignKey(Account, on_delete=models.CASCADE)
    company_name     = models.CharField(max_length=150,unique=True)
    industry         = models.ForeignKey(Industry, on_delete=models.CASCADE, related_name='companies')
    photo            = models.ImageField(upload_to='company_photo', null=True, blank=True)
    city             = models.CharField(max_length=20 ,null=True,blank=True)

    def __str__(self):
        return self.company_name
    
    