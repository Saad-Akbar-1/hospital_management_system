'''Configure urls for patient app here'''
from django.shortcuts import redirect
from django.urls import path
from django.urls.base import reverse
from django.views.generic.base import RedirectView
from patient import views # pylint: disable=import-error
from patient.views import signup_view



app_name = 'patient'
urlpatterns = [
    # ex: /patient/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /patient/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /patient/5/delete
    path('<int:pk>/delete', views.DeleteView.as_view(), name='delete'),
    # ex: /patient/5/patient/5
    path('<int:pk>/patient/<int:a>', views.DetailView.as_view(), name='detail3'),
    # ex: /patient/signup
    path('signup/', signup_view, name="signup"),
    # ex: /patient/signup/4/detail
    path('signup/<int:pk>/detail',views.DetailView.as_view(), name = 'detail2'),
    # ex: /patient/5/patient_update_form
    path('<int:pk>/patient_update_form', views.PatientUpdateView.as_view(), name = 'update')
]
