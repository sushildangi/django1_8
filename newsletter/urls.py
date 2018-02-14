from django.conf.urls import url
from .views import home, contact
from django1_8.views import about

app_name = 'newsletter'

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^about/$', about, name='about'),
]
