from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.autosListView.as_view(), name='autos-list'),
    path('show/<int:pk>/', views.autosDetailView.as_view(), name='autos-detail'),
    path('add/', views.autosCreateView.as_view(), name='autos-create'),

]
