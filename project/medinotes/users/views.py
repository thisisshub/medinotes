from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    """Used to display the homepage of website at /."""

    template_name = 'home.html'

    def homepage(self, request, template):
        """Display the first homepage of website."""
        template = self.template_name
        return render(request, template_name=template)
