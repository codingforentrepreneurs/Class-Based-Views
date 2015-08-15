from django import forms
from django.utils.text import slugify

from .models import Book


class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = [
			'title',
			'description',
		]

	def clean_title(self):
		title = self.cleaned_data["title"]
		slug = slugify(title)
		try:
			book = Book.objects.get(slug=slug)
			raise forms.ValidationError("Title Already Exists. Please try a different one.")
		except Book.DoesNotExist:
			return title
		except:
			raise forms.ValidationError("Title Already Exists. Please try a different one.")
