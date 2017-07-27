from django.conf.urls import url
from . import views

app_name = 'app1'

urlpatterns = [

    url(r'^home/$',views.home,name='home'),
    url(r'^login/$',views.login,name='login'),

]