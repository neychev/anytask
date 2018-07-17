from django.conf.urls import url

from anyrb import views

urlpatterns = [
    url(r'^update/(?P<review_id>\d+)$', views.message_from_rb),
]
