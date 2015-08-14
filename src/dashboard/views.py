from django.shortcuts import render

# Create your views here.

from django.views.generic.base import TemplateView


class DashboardTemplateView(TemplateView):
	template_name = "about.html"

	def get_context_data(self, *args, **kwargs):
		context = super(DashboardTemplateView, self).get_context_data(*args, **kwargs)
		context["title"] = "This is about us"
		return context