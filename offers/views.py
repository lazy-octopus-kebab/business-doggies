from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.urls import reverse_lazy
from django.conf import settings


from guardian.shortcuts import assign_perm
from guardian.decorators import permission_required_or_403

from .models import Offer
from .forms import MakeOfferForm


class OfferListView(PermissionRequiredMixin, LoginRequiredMixin, View):
    permission_required = 'offers.view_offer'
    template_name = 'offers/list.html'

    def get(self, request, *args, **kwargs):
        user = self.request.user
        context = {
            'user_type': None,
            'offers': None,
        }
        if user.has_perm('offers.add_offer'):
            context['offers'] = Offer.objects.filter(client=self.request.user)
            context['user_type'] = 'client'
        elif user.has_perm('offers.change_offer'):
            context['offers'] = Offer.objects.filter(sitter=self.request.user)
            context['user_type'] = 'sitter'
        
        return render(self.request, 'offers/list.html', context)


class OfferArchiveListView(PermissionRequiredMixin, LoginRequiredMixin, View):
    permission_required = 'offers.view_offer'
    template_name = 'offers/archive.html'

    def get(self, request, *args, **kwargs):
        user = self.request.user
        context = {
            'user_type': None,
            'offers': None,
        }
        if user.has_perm('offers.add_offer'):
            context['offers'] = Offer.objects.filter(
                client=self.request.user,
                status__in=[Offer.STATUS_ACCEPTED, Offer.STATUS_DECLINED]
            )
            context['user_type'] = 'client'
        elif user.has_perm('offers.change_offer'):
            context['offers'] = Offer.objects.filter(
                sitter=self.request.user,
                status__in=[Offer.STATUS_ACCEPTED, Offer.STATUS_DECLINED]
            )
            context['user_type'] = 'sitter'
        
        return render(self.request, 'offers/list.html', context)


class MakeOfferView(PermissionRequiredMixin, LoginRequiredMixin, View):
    permission_required = 'offers.add_offer'
    template_name = 'offers/make.html'
    form_class = MakeOfferForm
    success_url = reverse_lazy('list')

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


@login_required
@permission_required_or_403('offers.change_offer')
def accept_offer_view(request, offer_id):
    offer = get_object_or_404(Offer, id=offer_id)
    if request.user.has_perm('offers.change_offer', offer):
        raise PermissionDenied
    offer.status = Offer.STATUS_ACCEPTED
    offer.save()
    redirect(reverse_lazy('list'))


@login_required
@permission_required('offers.change_offer')
def decline_offer_view(request, offer_id):
    offer = get_object_or_404(Offer, id=offer_id)
    if request.user.has_perm('offers.change_offer', offer):
        raise PermissionDenied
    offer.status = Offer.STATUS_DECLINED
    offer.save()
    redirect(reverse_lazy('list'))
