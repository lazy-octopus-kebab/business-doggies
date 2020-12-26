from django.views.generic import FormView, ListView, View
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseNotFound
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login

from reviews.forms import ReviewForm
from pets.forms import PetForm
from offers.forms import MakeOfferForm

from .forms import ClientSignUpForm, SitterSignUpForm, UserAuthenticationForm
from .models import User


class ClientSignUpView(FormView):
    template_name = 'accounts/signup_client.html'
    form_class = ClientSignUpForm
    success_url = reverse_lazy('accounts:login')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)

        form = self.form_class()
        context = {
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
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


class SitterSignUpView(ClientSignUpView):
    template_name = 'accounts/signup_sitter.html'
    form_class = SitterSignUpForm


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('accounts:profile')
    authentication_form = UserAuthenticationForm
    redirect_authenticated_user=True


class UserProfileView(LoginRequiredMixin, View):
    form_review_class = ReviewForm
    form_pet_class = PetForm
    from_offer_class = MakeOfferForm

    template_client_name = 'accounts/profile_client.html'
    template_sitter_name = 'accounts/profile_sitter.html'

    def get(self, request, *args, **kwargs):
        form_review = self.form_review_class()
        form_pet = self.form_pet_class()
        form_offer = self.from_offer_class()
        
        if 'id' in kwargs:
            user = get_object_or_404(User, pk=kwargs['id'])
        else:
            user = request.user

        context = {
            'profile': user,
            'form_review': form_review,
            'form_pet': form_pet,
            'form_offer': form_offer,
        }

        if user.is_client:
            return render(request, self.template_client_name, context)
        elif user.is_sitter:
            return render(request, self.template_sitter_name, context)
        
        return HttpResponseNotFound(request)


class SitterListView(LoginRequiredMixin, ListView):
    model = User
    context_object_name = 'sitters'
    paginate_by = 5

    def get_queryset(self):
        queryset = self.model.objects.filter(is_sitter=True)
        return queryset
