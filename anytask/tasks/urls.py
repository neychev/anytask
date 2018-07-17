from django.conf.urls import url

from tasks import views

urlpatterns = [
    url(r'^create/(?P<course_id>\d+)$', views.task_create_page),
    url(r'^import/(?P<course_id>\d+)$', views.task_import_page),
    url(r'^contest_import/(?P<course_id>\d+)$', views.contest_import_page),
    url(r'^edit/(?P<task_id>\d+)$', views.task_edit_page),
    url(r'^get_contest_problems', views.get_contest_problems),
    url(r'^contest_task_import', views.contest_task_import),
    url(r'^popup/(?P<task_id>\d+)$', views.get_task_text_popup),
]
