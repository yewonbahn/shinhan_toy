from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .paginations import OrderLargePagination
from .models import Order,Comment
from .serializers import (
    OrderSerializer,
    CommentSerializer,CommentCreateSerializer,CommentDeleteSerializer)

class OrderListView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class = OrderSerializer
    pagination_class = OrderLargePagination
    def get_queryset(self):
        order_no = self.request.query_params.get('order_no')
        if order_no:
            orders = Order.objects.all().filter(ord_no__contains=order_no)
            return orders
        # orders = Order.objects.all().prefetch_related("comment_set")
        # id = self.request.query_params.get('id')
        # if id:
        #     orders = orders.filter(name__contains=id)
        return Order.objects.all().order_by('id')
        
    def get(self,request,*args,**kwargs):
        return self.list(request,args,kwargs)

class OrderDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView,
):

    serializer_class=OrderSerializer

    def get_queryset(self):
        return Order.objects.all().order_by('id')

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,args,kwargs)

class CommentListView(

    mixins.ListModelMixin,
    generics.GenericAPIView
):

    serializer_class = CommentSerializer

    def get_queryset(self):
        order_id = self.kwargs.get('pk')
				# 쿼리개선
        print(order_id)
        if order_id:
            return Comment.objects.filter(order_id=order_id) \
                    .select_related('member','order') \
                        .order_by('-id') 

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,args,kwargs)

class CommentUserView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentCreateSerializer
    def get_queryset(self):
        return Comment.objects.all().order_by('id')
    def post(self,request,*args,**kwargs):
        return self.create(request,args,kwargs)



class CommentDeleteView(
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(member__pk=self.request.user.id).order_by('id')

    def delete(self,request,*args,**kwargs):       
        return self.destroy(request,args,kwargs)