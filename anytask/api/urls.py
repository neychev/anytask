from django.conf.urls import url

from api import views

urlpatterns = [
    url(r'^v1/course/(?P<course_id>\d+)/statuses$', views.get_issue_statuses),
    url(r'^v1/course/(?P<course_id>\d+)/issues$', views.get_issues),
    url(r'^v1/issue/(?P<issue_id>\d+)/add_comment$', views.add_comment),
    url(r'^v1/issue/(?P<issue_id>\d+)$', views.get_or_post_issue),
    url(r'^v1/check_user$', views.check_user),
]
