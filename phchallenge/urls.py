
from django.conf.urls import include, url
from django.contrib import admin

from phchallenge_site import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signin/$', views.sign_in),
    url(r'^log_out/$', views.log_out),
    url(r'^log_in/$', views.log_in),
    url(r'^adddata/$', views.add_data),
    url(r'^viewdata/$', views.view_data),
    url(r'^editdata/$', views.edit_data),
    url(r'^savedata/$', views.save_data),
    url(r'^$', views.add_data),
]
