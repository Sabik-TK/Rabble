from django.db import models
from apps.company.models import Company
from apps.userprofile.models import Profile
from apps.userprofile.models import Skill

# Create your models here.
class Job(models.Model):

    TYPES = (
        ('Full-time','Full-time'),
        ('Part-time','Part-time'),
        ('Internship','Internship'),
        ('Trainee','Trainee')
    )

    HIRING_STATUS = (
        ('Hiring','Hiring'),
        ('Stopped','Stopped')
    )

    company         = models.ForeignKey(Company, on_delete=models.CASCADE)
    title           = models.CharField(max_length=150)
    employment_type = models.CharField(max_length=10, choices=TYPES)
    description     = models.TextField(blank=True, null=True)
    city            = models.CharField(max_length=100)
    salary      = models.IntegerField(null=True)
    status          = models.CharField(default='Hiring',choices=HIRING_STATUS, max_length=10)
    created         = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.company.company_name} - {self.title}'

class JobSkill(models.Model):

    job   = models.ForeignKey(Job,on_delete=models.CASCADE, related_name='preferred_skills')
    skill = models.ForeignKey(Skill,on_delete=models.CASCADE)

    class Meta:
        ordering = ['job','skill']
        unique_together = ('job', 'skill',)

    def __str__(self):
        return self.skill.name

class Application(models.Model):

    STATUS_CHOICES = (
        ('Applied','Applied'),
        ('Viewed','Viewed'),
        ('Rejected','Rejected'),
        ('Selected','Selected')
    )

    job     = models.ForeignKey(Job,on_delete=models.CASCADE, related_name='applicants')
    user    = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status  = models.CharField(default='Applied',max_length=10, choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['job','user']
        unique_together = ('job', 'user',)

    def __str__(self):
        return self.user.user.email


