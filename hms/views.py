"""
Default index views to patient and doctor
"""
from django.shortcuts import render
from django.views import View


class MainIndex(View):
    """Basic index view"""
    template_name = 'hms/index.html'

    def get(self, request):
        """Return the index page"""
        return render(request, 'hms/index.html')
