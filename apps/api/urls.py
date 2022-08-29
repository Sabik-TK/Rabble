from django.urls import path
from apps.account.views import activate
from .router import router

urlpatterns=[
    #Account Activatiom
    path('activate/<uidb64>/<token>/',activate, name= 'activate'),
]

urlpatterns += router.urls