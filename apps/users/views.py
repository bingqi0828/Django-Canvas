from django.shortcuts import render
from django.contrib.auth import authenticate,login

from django.contrib.auth.backends import ModelBackend

from apps.users.forms import LoginForm
from .models import UserProfile
from django.db.models import Q
from django.views.generic.base import View
from .forms import LoginForm

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user=UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            user_name=request.POST.get('username', None)
            pass_word=request.POST.get('password', None)
            user=authenticate(username=user_name,  password=pass_word)
            if user is not None:
                login(request, user)
                return render(request, 'index.html')
            else:
                return render(request,'login.html',{'msg':'用户名或密码错误'})
        else:
            return render(request,'login.html',{'login_form':login_form})