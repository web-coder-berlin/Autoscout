from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.postListView.as_view(), name='post-list'),
    path('show/<int:pk>/', views.postDetailView.as_view(), name='post-detail'),
    path('add/', views.postCreateView.as_view(), name='post-create'),

]
