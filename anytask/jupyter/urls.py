from django.conf.urls import url

from jupyter import views

urlpatterns = [
        url(r'^assignments$', views.update_jupyter_task),
]
