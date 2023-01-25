from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .paginations import OrderLargePagination
from .models import Order
from .serializers import (
    OrderSerializer,)

class OrderListView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):

    serializer_class = OrderSerializer
    pagination_class = OrderLargePagination
    def get_queryset(self):
        return Order.objects.all().order_by('id')

    def get(self,request,*args,**kwargs):
        return self.list(request,args,kwargs)
