from django.conf.urls import url
from basic_app import views

# TEMPALTE TAGGING
app_name = 'basic_app'

urlpatterns = [
    url(r'^relative/$', views.relative, name = 'relatie'),
    url(r'^other/$', views.other, name = 'other')

]
