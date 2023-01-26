from rest_framework import mixins, generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password
from .models import Member
from .serializers import (MemberSerializer)

class MemberRegisterView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):

    serializer_class = MemberSerializer
    # permission_classes =[IsAuthenticated]
    def get_queryset(self):
    
        members = Member.objects.all()
        return members.order_by('id')

    def get(self,request,*args,**kwargs):
        print(request.user)
        return self.list(request,args,kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,args,kwargs)