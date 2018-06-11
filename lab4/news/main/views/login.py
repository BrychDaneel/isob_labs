from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse


class CustomLoginView(LoginView):

    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(CustomLoginView, self).get(self, request, *args, **kwargs)

    def get_success_url(self):
        return reverse('main')
