from django.urls import path
from .views import UserCreateView
urlpatterns = [
    path('v1/users/create', UserCreateView.as_view(), name='api_v1_user'),

]