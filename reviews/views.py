from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import View
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.http import (
    HttpResponseForbidden,
    HttpResponseNotFound,
    HttpResponseBadRequest,
    JsonResponse,
)

from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.generics import ListCreateAPIView

from .forms import ReviewForm, ReviewRatingForm
from .models import Review, ReviewRating
from .serializers import ReviewSerializer


class ReviewList(ListCreateAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    serializer_class = ReviewSerializer
    queryset = Review.objects.none()
    form_class = ReviewForm

    def get_queryset(self):
        target = self.kwargs.get('target_id')
        queryset = Review.objects.filter(target=target).order_by('-pub_date')
        return queryset

    def post(self, request, target_id):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.target = get_object_or_404(get_user_model(), pk=target_id)

            if not review.target.has_perm('review.view_review'):
                HttpResponseForbidden()

            review.save()

            serializer = self.serializer_class(review)
            return JsonResponse(serializer.data, status=201)

        return HttpResponseBadRequest()


class ReviewRatingCreateView(PermissionRequiredMixin, LoginRequiredMixin, View):
    permission_required = 'reviews.add_reviewrating'
    target_permission = 'reviews.view_reviewrating'
    form_class = ReviewRatingForm
