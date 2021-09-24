from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from django.views.generic.base import View
from django.shortcuts import render


User = get_user_model()


class UserHomeView(LoginRequiredMixin, View):

    def get (self, request, *args, **kwargs):

        return render(self.request,'user-pages/home.html', context=None )

    def post (self, request, *args, **kwargs):
        pass
