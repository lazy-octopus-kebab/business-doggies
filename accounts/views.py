from django.views.generic import ListView, View
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from allauth.account.views import LoginView, SignupView

from reviews.forms import ReviewForm
from pets.forms import PetForm
from offers.forms import MakeOfferForm

from .models import User
from .forms import UserSignUpForm, UserLoginForm


class ClientSignUpView(SignupView):
    """View for registering a User as a Client"""
    form_class = UserSignUpForm
    template_name = 'accounts/signup_client.html'
    initial = {'user_type': form_class.USER_CLIENT}


class SitterSignUpView(SignupView):
    """View for registering a User as a Sitter"""
    form_class = UserSignUpForm
    template_name = 'accounts/signup_sitter.html'
    initial = {'user_type': form_class.USER_SITTER}


class UserLoginView(LoginView):
    """User Authentication View"""
    form_class = UserLoginForm
    template_name = 'accounts/login.html'


class UserProfileView(LoginRequiredMixin, View):
    """View of the User profile"""
    form_review_class = ReviewForm
    form_pet_class = PetForm
    form_offer_class = MakeOfferForm

    template_name = 'accounts/profile.html'

    def get(self, request, **kwargs):
        user = get_object_or_404(
            User,
            pk=kwargs.get('pk', request.user.pk)
        )

        context = {
            'profile': user,
        }

        if user.is_client:
            context['form_review'] = self.form_review_class()
            context['form_pet'] = self.form_pet_class()
        elif user.is_sitter:
            context['form_review'] = self.form_review_class()
            context['form_offer'] = self.form_offer_class()

        return render(request, self.template_name, context)


class SitterListView(LoginRequiredMixin, ListView):
    model = User
    context_object_name = 'sitters'
    paginate_by = 5

    def get_queryset(self):
        queryset = self.model.objects.filter(is_sitter=True)
        return queryset

