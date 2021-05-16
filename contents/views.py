from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class HomeView(TemplateView):


    # login_required와 동시에 settings에서 LOGIN_URL추가 
    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kargs):
        return super(HomeView, self).dispatch(request, *args, **kargs)

    template_name = "home.html"


class NonUserTemplateView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_anonymous:
            return redirect('contents_home')
        return super(NonUserTemplateView, self).dispatch(request, *args, **kwargs)


class LoginView(NonUserTemplateView):
    template_name = 'login.html'


class RegisterView(NonUserTemplateView):
    template_name = 'register.html'

