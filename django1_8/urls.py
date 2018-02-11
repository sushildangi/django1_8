from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'django1_8.views.home', name='home'),
    url(r'^', include('newsletter.urls')),
    url(r'^admin/', include(admin.site.urls)),

]
