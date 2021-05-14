from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class HomeView(TemplateView):


    # login_required와 동시에 settings에서 LOGIN_URL추가 
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kargs):
        return super(HomeView, self).dispatch(request, *args, **kargs)

    template_name = "home.html"
    

class LoginView(TemplateView):
    template_name = 'login.html'
