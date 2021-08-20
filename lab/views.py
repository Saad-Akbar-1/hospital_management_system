"""The main views for REST framweork"""
from django.http import Http404
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from lab.models import Reports
from lab.serializers import ReportSerializer


@api_view(['GET'])
def api_root(request, format=None):
    """The main index"""
    return Response({
        'reports': reverse('report-list', request=request, format=format)

    })


class ReportList(APIView):
    """ListView for reports"""
    serializer_class = ReportSerializer

    def get(self, request):
        reports = Reports.objects.all()
        serializer = ReportSerializer(
            reports, context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = {
            'reporttype': request.data.get('reporttype'),
            'report': request.data.get('report'),
            'concerned_doctor': request.data.get('concerned_doctor')
        }

        serializer = ReportSerializer(
            data=data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReportDetail(generics.RetrieveUpdateDestroyAPIView, APIView):
    """
    Retrieve, update or delete a report instance.
    """
    queryset = Reports.objects.all()
    serializer_class = ReportSerializer

    def get_object(self, pk):
        try:
            return Reports.objects.get(pk=pk)
        except Reports.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        report = self.get_object(pk)
        serializer = ReportSerializer(report, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        report = self.get_object(pk)
        serializer = ReportSerializer(
            report, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        report = self.get_object(pk)
        report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
