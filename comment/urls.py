from django.urls import path, re_path, include
from .views import like_button

app_name="comment"

urlpatterns=[
    re_path(r'^$',like_button, name='like'),
 ]