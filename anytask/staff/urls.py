from django.conf.urls import url

from staff import views

urlpatterns = [
    url(r'^$', views.staff_page, name='staff.views.staff_page'),
    url(r'^ajax_change_status$', views.ajax_change_status),
    url(r'^ajax_save_ids', views.ajax_save_ids),
    url(r'/gradebook/$', views.get_gradebook),
    url(r'/gradebook/(?P<statuses>\w+)$', views.gradebook_page),
    url(r'/gradebook_page', views.gradebook_page)
]
