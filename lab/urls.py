from django.urls import include, path

from lab import views

urlpatterns = [
    path('lab/', views.api_root,name='index'),
    path('lab/report', views.ReportList.as_view(),name='report-list'),
    path('lab/report/<int:pk>/', views.ReportDetail.as_view(),name='report-detail'),
    path('lab/users/', views.UserList.as_view(),name='user-list'),
    path('lab/users/<int:pk>/', views.UserDetail.as_view(),name='user-detail'),
]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
