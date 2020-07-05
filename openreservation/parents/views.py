from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import render
from parents.models import User
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


class ProfileDetailView(LoginRequiredMixin, DetailView):
    def get(self, request):
        return render(request, 'parents/profile.html', {'user': self.request.user})


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('parents:user_delete_success')
    success_message = "%(full_name)s se ha borrado con éxito"

    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.id)


class ProfileDeleteSuccess(TemplateView):
    template_name = "parents/user_delete_success.html"