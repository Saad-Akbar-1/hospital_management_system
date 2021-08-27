from django.urls import path
from rest_framework.authtoken import views as restviews

from lab import views

urlpatterns = [
    path('lab/report/', views.ReportList.as_view(), name='report-list'),
    path('lab/report/<int:pk>/', views.ReportDetail.as_view(), name='report-detail'),
    path('lab/report/<int:pk>/<format>',
         views.ReportDetail.as_view(), name='report-detail'),
]

urlpatterns += [
    path('lab/api-auth-token/', restviews.obtain_auth_token)
]

