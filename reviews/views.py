from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import View

from .models import Review, ReviewRating


class ReviewCreateView(PermissionRequiredMixin, LoginRequiredMixin, View):
    permission_required = 'reviews.add_review'
    template_name = 'offers/form.html'
    form_class = Revi

    def get(self, request, sitter_id, *args, **kwargs):
        get_object_or_404(settings.AUTH_USER_MODEL, pk=sitter_id)
        form = self.form_class()
        context = {
            'form': form,
            'sitter_id': sitter_id,
        }
        return render(request, self.template_name, context)

    def post(self, request, sitter_id, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            offer = form.cleaned_data
            offer.client = request.user
            offer.sitter = get_object_or_404(settings.AUTH_USER_MODEL, pk=sitter_id)
            offer.save()

            # Apply permissions
            assign_perm('offers.change_offer', offer.client, offer)

            return redirect(self.success_url)

        context = {
            'form': form,
            'sitter_id': sitter_id,
        }
        return render(request, self.template_name, context)


class ReviewRatingCreateView(PermissionRequiredMixin, LoginRequiredMixin, View):
    permission_required = 'reviews.add_reviewrating'