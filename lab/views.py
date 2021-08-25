"""The main views for REST framweork"""
from django.contrib.auth import mixins
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from lab.models import Reports
from lab.serializers import ReportSerializer


class TokenLoginRequiredMixin(mixins.LoginRequiredMixin):

    """A login required mixin that allows token authentication."""

    def dispatch(self, request, *args, **kwargs):
        """If token was provided, ignore authenticated status."""
        http_auth = request.META.get("HTTP_AUTHORIZATION")
        token_key = http_auth.split()[1]
        if http_auth and "Token" in http_auth:
            token_obj = Token.objects.get(key=token_key)
            if(token_obj):
                request.user = User.objects.get(auth_token=token_key)

        elif not request.user.is_authenticated:
            return self.handle_no_permission()

        return super(mixins.LoginRequiredMixin, self).dispatch(
            request, *args, **kwargs)


class ReportList(TokenLoginRequiredMixin, APIView):
    """ListView for Reports"""
    serializer_class = ReportSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    login_url = "http://localhost:8000/api-auth/login/"

    def get(self, request):
        """get the list of Reports"""
        reports = Reports.objects.all()
        serializer = ReportSerializer(
            reports, context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Add a new report to the list."""
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


class ReportDetail(TokenLoginRequiredMixin, APIView):
    """
    Retrieve, update or delete a report instance.
    """
    queryset = Reports.objects.all()
    serializer_class = ReportSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [AllowAny]

    def get_object(self, pk):
        """get report or send a 404."""
        try:
            return Reports.objects.get(pk=pk)
        except Reports.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """get details of a particular report"""
        report = self.get_object(pk)
        serializer = ReportSerializer(report, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        """Update the report"""
        report = self.get_object(pk)
        serializer = ReportSerializer(
            report, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete a particular report."""
        report = self.get_object(pk)
        report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
