from django.urls import re_path
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from . import views
from accounts import views as accounts_views


urlpatterns = [
    re_path(r'^login/$', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    re_path(r'^signup/$', accounts_views.signup, name='signup'),

    #Ajax signup
    re_path(r'^ajax/singup/$', views.SignUpView.as_view(), name='ajax_signup'),
    re_path(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
]