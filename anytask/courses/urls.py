from django.conf.urls import url, include

import views
from courses.pythontask import get_task, cancel_task

urlpatterns = [
    url(r'^(?P<course_id>\d+)$', views.course_page, name='courses.views.course_page'),
    url(r'^(?P<course_id>\d+)/seminar/(?P<task_id>\d+)$', views.seminar_page),
    url(r'^(?P<course_id>\d+)/queue$', views.queue_page, name='courses.views.queue_page'),
    url(r'^(?P<course_id>\d+)/gradebook/$', views.gradebook, name='courses.views.gradebook'),
    url(r'^(?P<course_id>\d+)/gradebook/seminar/(?P<task_id>\d+)/$', views.gradebook),
    url(r'^(?P<course_id>\d+)/gradebook/group/(?P<group_id>\d+)/$', views.gradebook),
    url(r'^(?P<course_id>\d+)/gradebook/seminar/(?P<task_id>\d+)/group/(?P<group_id>\d+)$', views.gradebook),
    url(r'^year/(?P<year>\d+)', views.courses_list),
    url(r'^edit_course_information', views.edit_course_information),
    url(r'^set_spectial_course_attend', views.set_spectial_course_attend),
    url(r'^(?P<course_id>\d+)/settings$', views.course_settings, name='courses.views.course_settings'),
    url(r'^change_visibility_hidden_tasks$', views.change_visibility_hidden_tasks, name='courses.views.change_visibility_hidden_tasks'),
    url(r'^change_visibility_academ_users$', views.change_visibility_academ_users),
    url(r'^set_course_mark$', views.set_course_mark),
    url(r'^set_task_mark$', views.set_task_mark),
    url(r'^change_table_tasks_pos', views.change_table_tasks_pos),
    url(r'^ajax_update_contest_tasks/$', views.ajax_update_contest_tasks),
    url(r'^ajax_rejudge_contest_tasks/$', views.ajax_rejudge_contest_tasks),
    url(r'^pythontask/get_task/(?P<course_id>\d+)/(?P<task_id>\d+)$', get_task),
    url(r'^pythontask/cancel_task/(?P<course_id>\d+)/(?P<task_id>\d+)$', cancel_task),
    url(r'^(?P<course_id>\d+)/attendance$', views.attendance_page),
    url(r'^(?P<course_id>\d+)/attendance/group/(?P<group_id>\d+)/$', views.attendance_page),
    url(r'^lesson_visited$', views.lesson_visited),
    url(r'^lesson_delete$', views.lesson_delete),
    url(r'^(?P<course_id>\d+)/statistic$', views.view_statistic),
    url(r'^ajax_get_queue$', views.ajax_get_queue),
]
