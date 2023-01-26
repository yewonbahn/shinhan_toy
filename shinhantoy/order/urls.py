from django.urls import path
from . import views

urlpatterns = [
    path("/<int:pk>", views.OrderDetailView.as_view()),
    path("/<int:pk>/comment", views.CommentListView.as_view()),
    path("/comment", views.CommentUserView.as_view()),  
    path("", views.OrderListView.as_view()),
]