from django.urls import path
from .views import HomeView, LoginView, RegisterView

urlpatterns = [
    path('', HomeView.as_view(), name="contents_home"),
    path('login/', LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register"),
]