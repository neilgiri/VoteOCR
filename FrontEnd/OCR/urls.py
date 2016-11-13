from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ImageSubmit, name='VoterForm'),
    url(r'VoterForm', views.VoterForm, name='VoterForm'),
    url(r'Thanks', views.Thanks, name='Thanks'),
]
