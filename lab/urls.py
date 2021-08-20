from django.urls import include, path

from lab import views

from rest_framework import routers

router = routers.SimpleRouter()


urlpatterns = [
    path('lab/', views.api_root,name='index'),
    path('lab/report', views.ReportList.as_view(),name='report-list'),
    path('lab/report/<int:pk>/', views.ReportDetail.as_view(),name='report-detail'),
    path('lab/report/<int:pk>/<format>', views.ReportDetail.as_view(),name='report-detail'),
]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
urlpatterns += router.urls
