'''Configure urls for patient app here'''
from django.urls import path
from django.urls.base import reverse_lazy

from patient import views
from patient.views import SignupView

app_name = 'patient'
urlpatterns = [
    # ex: /patient/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /patient/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /patient/5/delete
    path('<int:pk>/delete', views.DeleteView.as_view(
        success_url=reverse_lazy('patient:index')), name='delete'),
    # ex: /patient/5/patient/5
    path('<int:pk>/patient/<int:a>', views.DetailView.as_view(), name='detail3'),
    # ex: /patient/signup
    path('signup/', SignupView.as_view(), name="signup"),
    # ex: /patient/signup/4/detail
    path('signup/<int:pk>/detail', views.DetailView.as_view(), name='detail2'),
    # ex: /patient/5/patient_update_form
    path('<int:pk>/patient_update_form',
         views.PatientUpdateView.as_view(), name='update')
]
