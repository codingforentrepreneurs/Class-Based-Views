from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.base import TemplateView, TemplateResponseMixin, ContextMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.utils.decorators import method_decorator


from .forms import BookForm
from .models import Book


#CREATE

#RETREIVE

#UPDATE

#DELETE





# def book_detail(request, slug):
# 	book = Book.objects.get(slug=slug)
# 	return render()


class BookCreateView(CreateView):
	template_name = "forms.html"
	form_class = BookForm
	#success_url = "/"
	def form_valid(self, form):
		form.instance.added_by = self.request.user
		#form.instance.last_edited_by = self.request.user
		return super(BookCreateView, self).form_valid(form)

	def get_success_url(self):
		return reverse("book_list")


class BookDetail(DetailView):
	model = Book

class BookListView(ListView):
	model = Book
	# def get_queryset(self, *args, **kwargs):
	# 	qs = super(BookListView, self).get_queryset(*args, **kwargs)
	# 	return qs




class LoginRequiredMixin(object):
	# @classmethod
	# def as_view(cls, **kwargs):
	# 	view = super(LoginRequiredMixin, cls).as_view(**kwargs)
	# 	return login_required(view)

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class DashboardTemplateView(TemplateView):
	template_name = "about.html"

	def get_context_data(self, *args, **kwargs):
		context = super(DashboardTemplateView, self).get_context_data(*args, **kwargs)
		context["title"] = "This is about us"
		return context



class MyView(ContextMixin, TemplateResponseMixin, LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		context["title"] = "Some other title"
		return self.render_to_response(context)

	# @method_decorator(login_required)
	# def dispatch(self, request, *args, **kwargs):
	# 	return super(MyView, self).dispatch(request, *args, **kwargs)