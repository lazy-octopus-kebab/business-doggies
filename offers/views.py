from django.shortcuts import get_object_or_404, render
from django.views.generic import View, ListView
from django.urls import reverse

from .models import Offer
from .forms import MakeOfferForm


class OfferSentListView(ListView):
    """
    View with created offers 
    """
    model = Offer
    template_name = 'offers/list.html'

    def get_queryset(self, request):
        queryset = super(OfferSentListView, self).get_queryset(request)
        user_id = request.user.id
        return queryset.filter(client_id=user_id)


class OfferRecvListView(ListView):
    """
    View with received offers
    """
    model = Offer
    template_name = 'offers/list.html'

    def get_queryset(self, request):
        queryset = super(OfferRecvListView, self).get_queryset(request)
        user_id = request.user.id
        return queryset.filter(sitter_id=user_id)


class MakeOfferView(View):
    template_name = 'offers/form.html'
    form_class = MakeOfferForm

    def get(self, request, sitter_id, *args, **kwargs):
        form = self.form_class()
        context = {
            'form': form,
            'sitter_id': sitter_id,
        }
        return render(request, self.template_name, context)

    def post(self, request, sitter_id, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            pass

        context = {
            'form': form,
            'sitter_id': sitter_id,
        }
        return render(request, self.template_name, context)

    