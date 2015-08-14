from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.base import TemplateView, TemplateResponseMixin, ContextMixin


class DashboardTemplateView(TemplateView):
	template_name = "about.html"

	def get_context_data(self, *args, **kwargs):
		context = super(DashboardTemplateView, self).get_context_data(*args, **kwargs)
		context["title"] = "This is about us"
		return context



class MyView(ContextMixin, TemplateResponseMixin, View):
	def get(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		context["title"] = "Some other title"
		return self.render_to_response(context)