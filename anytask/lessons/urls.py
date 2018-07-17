from django.conf.urls import url

from lessons import views

urlpatterns = [
    url(r'^create/(?P<course_id>\d+)$', views.schedule_create_page),
    url(r'^edit/(?P<lesson_id>\d+)$', views.schedule_edit_page),
]
