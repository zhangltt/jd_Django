from django.conf.urls import include, url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^regist/$', views.regist),
    url(r'^api/regist_yz/$',views.regist_yz),
    url(r'^regist_handler/$',views.regist_handler),
    url(r'^login/$',views.login),
    url(r'^api/login_handler/$',views.login_handler),
    url(r'^user_center/$',views.user),
    url(r'^api/exit/$',views.exit_login),
    url(r'^address/$', views.address),
    url(r'^api/add/$', views.address_add),
    url(r'^api/update/$', views.address_update),

]