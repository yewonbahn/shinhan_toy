from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .paginations import OrderLargePagination
from .models import Order,Comment
from .serializers import (
    OrderSerializer,
    CommentSerializer,CommentCreateSerializer)

class OrderListView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):

    serializer_class = OrderSerializer
    pagination_class = OrderLargePagination
    def get_queryset(self):
        orders = Order.objects.all().prefetch_related("comment_set")
        print(orders)
        print("0----")
        id = self.request.query_params.get('id')
        if id:
            orders = orders.filter(name__contains=id)
        return orders.order_by('id')
    def get(self,request,*args,**kwargs):
        return self.list(request,args,kwargs)

class OrderDetailView(
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView,
):
    serializer_class=OrderSerializer

    def get_queryset(self):
        return Order.objects.all().order_by('id')

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,args,kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,args,kwargs)

    def put(self,request,*args,**kwargs):
        return self.partial_update(request,args,kwargs)
class CommentListView(
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    serializer_class = CommentSerializer

    def get_queryset(self):
        order_id = self.kwargs.get('order_id')
				# 쿼리개선
        print(order_id)
        if order_id:
            return Comment.objects.filter(order_id=order_id).order_by('-id') 
        return Comment.objects.none()

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

class CommentCreateView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class = CommentCreateSerializer
    def get_queryset(self):
        return Comment.objects.all().order_by('id')
    def post(self,request,*args,**kwargs):
        return self.create(request,args,kwargs)