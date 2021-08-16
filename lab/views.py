"""The main views for REST framweork"""
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from lab.models import Reports
from lab.serializers import ReportSerializer

# from lab.permissions import IsOwnerOrReadOnly


@api_view(['GET'])
def api_root(request, format=None):
    """The main index"""
    return Response({
    #    'users': reverse('user-list', request=request, format=format),
        'reports': reverse('report-list', request=request, format=format)


    })


class ReportList(generics.ListCreateAPIView):
    """ListView for reports"""
    queryset = Reports.objects.all()
    serializer_class = ReportSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    #                       IsOwnerOrReadOnly]


class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    """Detail View for reports."""
    queryset = Reports.objects.all()
    serializer_class = ReportSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# class UserList(generics.ListAPIView):
#     """List View for users"""
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     """Detail View for user"""
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
