from django.conf.urls import url

from invites import views

urlpatterns = [
    url(r'^generate_invites/$', views.generate_invites),
]
