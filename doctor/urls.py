from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from doctor import views

app_name = 'doctor'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('signup/', views.AddDoctorView.as_view(), name='signup'),
    path('signup/<int:pk>/detail', views.DetailView.as_view(), name='signup'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:id>/update', views.UpdateDoctorView.as_view(), name='update'),
    path('<int:id>/delete', views.DeleteDoctor.as_view(), name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
