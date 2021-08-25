from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from doctor import views

urlpatterns = [
    path('', views.DoctorList.as_view(), name='doctor-list'),
    path('<int:pk>/', views.DetailDoctor.as_view(), name='doctor-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
