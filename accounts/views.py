from django.views.generic import FormView, View
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseNotFound
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login

from .forms import ClientSingUpForm, SitterSingUpForm
from .models import User


class ClientSingUpView(FormView):
    template_name = 'accounts/singup_client.html'
    form_class = ClientSingUpForm
    success_url = reverse_lazy('accounts:login')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            redirect(self.success_url)

        form = self.form_class()
        context = {
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            redirect(self.success_url)

        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1'],
            )
            login(request, user)
            return redirect(self.success_url)

        context = {
            'form': form,
        }
        return render(request, self.template_name, context)


class SitterSingUpView(ClientSingUpView):
    template_name = 'accounts/singup_sitter.html'
    form_class = SitterSingUpForm


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('accounts:profile')
    redirect_authenticated_user=True


class UserProfileView(LoginRequiredMixin, View):
    template_client_name = 'accounts/profile_client.html'
    template_sitter_name = 'accounts/profile_sitter.html'

    def get(self, request, *args, **kwargs):
        if 'id' in kwargs:
            user = get_object_or_404(User, kwargs['id'])
        else:
            user = request.user

        context = {
            'user': user,
        }

        if user.is_client:
            return render(request, self.template_client_name, context)
        elif user.is_sitter:
            return render(request, self.template_sitter_name, context)
        return HttpResponseNotFound(request)

    def post(self, request, *args, **kwargs):
        return render(request, 'accounts/profile.html')