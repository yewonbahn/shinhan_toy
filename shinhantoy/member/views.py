from rest_framework import mixins, generics,status
from rest_framework.views import APIView
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password,check_password
from .models import Member
from .serializers import (MemberSerializer)

class MemberRegisterView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
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


class MemberChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self,request,*args,**kwargs):
       
       #request.user 
        current = request.data.get("current")
        password1 = request.data.get("password1")
        password2 = request.data.get("password2")

        if password1 != password2:
            return Response({
                "detail":"Wrong new passwords",
            },status=status.HTTP_400_BAD_REQUEST)

        if not check_password(current,request.user.password):
            return Response({
                'datail':'Wrong password',
            },status=status.HTTP_400_BAD_REQUEST)

        request.user.password=make_password(password1)
        request.user.save()

        return Response(status=status.HTTP_201_CREATED)

