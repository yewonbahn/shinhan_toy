from django.contrib import admin
from .models import Order,Comment
# Register your models here.
@admin.register(Order)
class MemberAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
