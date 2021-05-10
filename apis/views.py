from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.db import IntegrityError

class BaseView(View):
    @staticmethod
    def response(data={}, message ="", status=200):
        results = {
            'data': data,
            'message':message,
        }

        return JsonResponse(results, status)



class UserCreateView(BaseView):
    def dispatch(self, request, *args, **kargs):
        return super(UserCreateView, self).dispatch(request,args, kargs)

    def post(self, request):
        username = request.POST.get('username', '')
        if not username:
            return self.response(message="아이디를 입력해주세요", status=400)
        password = request.POST.get('password', '')
        if not password:
            return self.response(message="패스워드를 입력해주세요", status=400)
        email = request.POST.get('email', '')
        if not email:
            return self.response(message="email을 입력해주세요", status=400)

        try:
            user = User.objects.create_user(username, email, password)
        except IntegrityError:
            return self.response(message="존재하는 아이디입니다.", status=400)

        return self.response({"user.id": user})

        