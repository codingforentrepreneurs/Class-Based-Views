from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from django.views.generic import View
from django.views.generic.base import TemplateView, TemplateResponseMixin, ContextMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, ModelFormMixin
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


class MultipleObjectMixin(object):
	def get_object(self, queryset=None, *args, **kwargs):
		slug = self.kwargs.get("slug")
		if slug:
			try:
				obj = self.model.objects.get(slug=slug)
			except self.model.MultipleObjectsReturned:
				obj = self.get_queryset().first()
			except:
				raise Http404
			return obj
		raise Http404


class BookDeleteView(DeleteView):
	model = Book

	def get_success_url(self):
		return reverse("book_list")



class BookCreateView(SuccessMessageMixin, CreateView):
	template_name = "forms.html"
	form_class = BookForm
	success_message = "%(title)s has been created at %(created_at)s"
	#success_url = "/"
	def form_valid(self, form):
		form.instance.added_by = self.request.user
		#form.instance.last_edited_by = self.request.user
		valid_form = super(BookCreateView, self).form_valid(form)
		#messages.success(self.request, "Book created!")
		# send signals
		return valid_form

	def get_success_url(self):
		return reverse("book_list")

	def get_success_message(self, cleaned_data):
		return self.success_message % dict(
			cleaned_data,
			created_at=self.object.timestamp,
		)


class BookUpdateView(MultipleObjectMixin, UpdateView):
	model = Book
	#fields = ["title", "description"]
	form_class = BookForm
	template_name = "forms.html"


class BookDetail(SuccessMessageMixin, ModelFormMixin, MultipleObjectMixin, DetailView):
	model = Book
	form_class = BookForm
	success_message = "%(title)s has been updated."

	def get_context_data(self, *args, **kwargs):
		context = super(BookDetail, self).get_context_data(*args, **kwargs)
		context["form"] = self.get_form()
		context["btn_title"] = "Update Book"
		return context

	def post(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			self.object = self.get_object()
			form = self.get_form()
			if form.is_valid():
				return self.form_valid(form)
			else:
				return self.form_invalid(form)

	def get_success_url(self):
		return reverse("book_list")


	# def dispatch(self, request, *args, **kwargs):
	# 	messages.success(self.request, "Book viewed!")
	# 	return super(BookDetail, self).dispatch(request, *args, **kwargs)


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