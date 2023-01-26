from django.urls import path
from . import views

urlpatterns = [
    path("/<int:pk>", views.OrderDetailView.as_view()),
    path("/<int:order_id>/comment", views.CommentListView.as_view()),
    path("", views.OrderListView.as_view()),
]