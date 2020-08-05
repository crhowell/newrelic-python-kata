from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views


urlpatterns = [
    #url(r'^$', TemplateView.as_view(template_name='base.html')),
    #url(r'^$', TemplateView.as_view(template_name='home.html')),
    
    # includes each of the katas into the root
    path('', include('employees.urls')),
    path('', include('factorial.urls')),
    path('', include('weather.urls')),
    path('admin/', admin.site.urls),
    path('', views.home),
    # Examples:
    # url(r'^newrelic_python_kata/', include('newrelic_python_kata.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
