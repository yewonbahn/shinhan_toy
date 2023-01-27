from rest_framework import serializers
from .models import Order,Comment

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
class CommentSerializer(serializers.ModelSerializer):
    order_id = serializers.SerializerMethodField()
    member_username = serializers.SerializerMethodField()
    tstamp = serializers.DateTimeField(
        read_only=True,format='%Y-%m-%d %H:%M:%S'
    )

    def get_order_id(self,obj):
        return obj.order.id
    def get_member_username(self,obj):
        return obj.member.username
    class Meta:
        model = Comment
        fields = "__all__"

class CommentCreateSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        request = self.context['request']
        if request.user.is_authenticated:
            attrs['member']=request.user
        else:
            raise serializers.ValidationError("member is required")

        print(request.user)
        return attrs
    class Meta:
        model = Comment
        fields = "__all__"
        extra_kwargs={'member':{'required':False}}

class CommentDeleteSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        request = self.context['request']
        if request.user.is_authenticated:
            attrs['member']=request.user
        else:
            raise serializers.ValidationError("member is required")

        print(request.user)
        return attrs
    class Meta:
        model = Comment
        fields = "__all__"
        extra_kwargs={'member':{'required':False}}
