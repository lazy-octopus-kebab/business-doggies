from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import View
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden
from django.contrib.auth import get_user_model

from .forms import ReviewForm, ReviewRatingForm
from .models import Review, ReviewRating


class ReviewCreateView(PermissionRequiredMixin, LoginRequiredMixin, View):
    permission_required = 'reviews.add_review'
    target_permission = 'review.view_review'
    template_name = 'offers/form.html'
    form_class = ReviewForm
    success_url = reverse_lazy("accounts:profile")

    def validate(self, author, target):
        if not target.has_perm(self.target_permission) or \
               target.pk == author.pk:
            return False
        return True

    def get(self, request, pk, *args, **kwargs):
        target = get_object_or_404(get_user_model(), pk=pk)
        if not self.validate(request.user, target):
            return HttpResponseForbidden(request)
        form = self.form_class()
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.target = get_object_or_404(get_user_model(), pk=pk)

            if not self.validate(request.user, review.target):
                HttpResponseForbidden(request)

            review.save()

            return redirect(self.success_url)

        context = {
            'form': form,
        }
        return render(request, self.template_name, context)


class ReviewRatingCreateView(PermissionRequiredMixin, LoginRequiredMixin, View):
    permission_required = 'reviews.add_reviewrating'
    target_permission = 'reviews.view_reviewrating'
    form_class = ReviewRatingForm