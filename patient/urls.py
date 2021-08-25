'''Configure urls for patient app here'''
from django.urls import path

from patient import views

app_name = 'patient'
urlpatterns = [
    # ex: /patient/
    path('', views.PatientList.as_view(), name='patient-list'),
    # ex: /patient/5/
    path('<int:pk>/', views.PatientDetail.as_view(), name='patient-detail'),    
]
