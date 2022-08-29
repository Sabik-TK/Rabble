from rest_framework import viewsets
from .models import Account
from .serializers import AccountSerializer
from rest_framework.response import Response
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.decorators import action
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,BasePermission

# Create your views here.
class IsCreationOrIsAuthenticated(BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            if view.action == 'create':
                return True
            else:
                return False
        else:
            return True



class UserViewSet(viewsets.ModelViewSet):
    
    queryset           = Account.objects.all().order_by('id')
    serializer_class   = AccountSerializer
    permission_classes = [IsCreationOrIsAuthenticated]


    

    @action(detail=True, methods=['get'])
    def activate_user(self,request,pk=None):
        user = self.get_object()
        current_site = get_current_site(request)
        mail_subject = 'Please activate your account'
        message = render_to_string('email/verification_email.html', {     
                 'user'  : user,
                 'domain': current_site,
                 'uid'   : urlsafe_base64_encode(force_bytes(user.pk)),
                 'token' : default_token_generator.make_token(user),
             })
        to_email  = user
        send_mail = EmailMessage(mail_subject, message, to=[to_email]) 
        send_mail.send()
        user.is_active = False
        user.save()
        serializer = AccountSerializer(user)
        data = {
            'Message' : 'An activation mail is sended to to your email address : %s ' %user,
            'user'    :  serializer.data 
        }

        return Response(data)


    @action(detail=True, methods=['get'])
    def deactivate_user(self,request,pk=None):
        user = self.get_object()
        user.is_active = False
        user.save()
        serializer = AccountSerializer(user)
        return Response({
            'Message': 'Account is deactivated',
            'user'   :  serializer.data  })


@api_view(['GET'])
@permission_classes([AllowAny])
def activate(request, uidb64, token):
    if request.method == 'GET':
        try:
            uid   = urlsafe_base64_decode(uidb64).decode()
            user  = Account._default_manager.get(pk=uid)

        except(TypeError,ValueError,OverflowError, Account.DoesNotExist):
            user  = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            serializer = AccountSerializer(user)
            return Response({
            'Message': 'Account is now activated',
            'user'   :  serializer.data  })
        else:
            serializer = AccountSerializer(user)
            return Response({'Message': 'invalid credentials',})
