from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,PermissionsMixin)
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as _


class AccountManager(BaseUserManager):

    def create_user(self,email,password=None,mobile=None,**other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email,mobile=mobile,**other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password, mobile=None,**other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email,password,mobile, **other_fields)

class Account(AbstractBaseUser, PermissionsMixin):

    email      = models.EmailField(_('email address'), unique=True)
    mobile     = models.CharField(max_length=15,null=True,blank=True)
    is_active  = models.BooleanField(default=True)
    is_staff   = models.BooleanField(default=False)
    created    = models.DateTimeField(auto_now_add=True)
    updated    = models.DateTimeField(auto_now=True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile']

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"

    def email_user(self, subject, message):
        send_mail(
            subject,
            message,
            'stethoscope@gmail.com',
            [self.email],
            fail_silently=False,
        )

    def __str__(self):
        return self.email