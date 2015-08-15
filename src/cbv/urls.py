from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from django.views.generic.base import TemplateView

from dashboard.views import DashboardTemplateView, MyView,\
							 BookDetail, BookListView, BookCreateView,\
							 BookUpdateView, BookDeleteView

urlpatterns = [
    # Examples:
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
    #url(r'^about/$', 'cbv.views.about', name='about'),
    url(r'^book/create/$', BookCreateView.as_view(), name='book_create'),
    url(r'^book/$', BookListView.as_view(), name='book_list'),
    url(r'^book/(?P<slug>[-\w]+)/$', BookDetail.as_view(), name='book_detail'),
    url(r'^book/(?P<slug>[-\w]+)/delete/$', BookDeleteView.as_view(), name='book_delete'),
    url(r'^book/(?P<slug>[-\w]+)/update/$', BookUpdateView.as_view(), name='book_update'),
    url(r'^someview/$', MyView.as_view(template_name='about.html'), name='someview'),
    url(r'^about/$', DashboardTemplateView.as_view(), name='about'),
    url(r'^team/$', DashboardTemplateView.as_view(template_name='team.html'), name='team'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)