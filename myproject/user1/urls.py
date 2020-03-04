from django.conf.urls import url
from . import views
# SET THE NAMESPACE!
#app_name = 'user1'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$',views.user_login,name='user_login'),
    url(r'^pos$',views.pos,name='pos'),
    url(r'^logout/$', views.user_logout, name='logout'),

]                                                                                                                    