from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import View
from django.conf import settings

from guardian.shortcuts import assign_perm

from .forms import PetForm


class PetCreateView(PermissionRequiredMixin, LoginRequiredMixin, View):
    permission_required = 'pets.add_pet'
    template_name = 'pets/form.html'
    form_class = PetForm
    success_url = reverse_lazy('list')

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            pet = form.cleaned_data
            pet.owner = request.user
            pet.save()

            # Apply permissions
            assign_perm('offers.change_pet', pet.owner, pet)

            return redirect(self.success_url)

        context = {
            'form': form,
        }
        return render(request, self.template_name, context)