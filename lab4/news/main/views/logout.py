from django.views.generic.base import View
from django.contrib.auth import logout
from django.shortcuts import redirect


class CustomLogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('main')
