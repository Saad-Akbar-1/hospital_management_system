'''Configure urls for patient app here'''
from django.urls import path
from patient import views

app_name = 'patient'
urlpatterns = [
    # ex: /patients/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /patients/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
