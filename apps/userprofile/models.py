from turtle import title
from django.db import models
from apps.account.models import Account
from apps.company.models import Company

# Create your models here.

class Profile(models.Model):

    user       = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='profile')
    title      = models.CharField(max_length=150, null=True,blank=True)
    first_name = models.CharField(max_length=150, null=True,blank=True)
    last_name  = models.CharField(max_length=150, null=True,blank=True)
    photo      = models.ImageField(upload_to='profile_photo', null=True, blank=True)
    dob        = models.DateField(null=True)
    state      = models.CharField(max_length=20 ,null=True,blank=True)
    city       = models.CharField(max_length=20 ,null=True,blank=True)

    def __str__(self):
        return self.user.email

    def full_name(self):
        return f'{self.first_name} {self.last_name}'    


class Education(models.Model):

    profile     = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='education')
    title       = models.CharField(max_length=150,)
    institution = models.CharField(max_length=150, null=True)
    year        = models.DateField(null=True)
    place       = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.title

class Experience(models.Model):
    
    profile     = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='experience')
    company     = models.ForeignKey(Company,on_delete=models.SET_NULL, null=True,blank= True, related_name='employees')
    designation = models.CharField(max_length=150)
    start_date  = models.DateField(null=True, blank=True)
    end_date    = models.DateField(null=True, blank=True) 

    def __str__(self):
        return self.profile.user.email

class Skill(models.Model):
    name = models.CharField(max_length = 32, unique=True)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name


class SkilledUsers(models.Model):

    user  = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    class Meta:
        ordering = ['user','skill']
        unique_together = ('user', 'skill',)

    def __str__(self):          
        return self.skill.name
        

