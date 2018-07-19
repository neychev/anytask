from django.conf.urls import url

from users import views

urlpatterns = [
    url(r'^my_tasks/$', views.my_tasks, name='users.views.my_tasks'),
    url(r'^add_user_to_group/$', views.add_user_to_group),
    url(r'^ya_oauth_request/(?P<type_of_oauth>\w+)$', views.ya_oauth_request),
    url(r'^ya_oauth_response/(?P<type_of_oauth>\w+)$', views.ya_oauth_response),
    url(r'^ya_oauth_disable/(?P<type_of_oauth>\w+)$', views.ya_oauth_disable),
    url(r'^ya_oauth_forbidden/(?P<type_of_oauth>\w+)$', views.ya_oauth_forbidden),
    url(r'^ya_oauth_changed/$', views.ya_oauth_changed),
    url(r'^(?P<username>.*)/courses', views.user_courses, name='users.views.user_courses'),
    url(r'^activate_invite$', views.activate_invite),
    url(r'^settings$', views.profile_settings, name='users.views.profile_settings'),
    url(r'^(?P<username>.*)/profile_history', views.profile_history, name="users.views.profile_history"),
    url(r'^(?P<username>.*)/set_user_statuses', views.set_user_statuses),
    url(r'^ajax_edit_user_info$', views.ajax_edit_user_info)
]
