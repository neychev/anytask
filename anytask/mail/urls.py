from django.conf.urls import url

from mail import views

urlpatterns = [
    url(r'^$', views.mail_page, name='mail.views.mail_page'),
    url(r'^ajax_get_mailbox$', views.ajax_get_mailbox),
    url(r'^ajax_get_message$', views.ajax_get_message),
    url(r'^ajax_send_message$', views.ajax_send_message),
]
