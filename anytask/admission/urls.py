from django.conf.urls import url

from admission import views

urlpatterns = [
    url(r'^register$', views.register),
    url(r'^activate/(?P<activation_key>\w+)/', views.activate),
    # url(r'^decline/(?P<activation_key>\w+)/', views.decline),
]
