from django.views.generic.list import ListView

from django.contrib.auth.models import User

class UsersView(ListView):
    template_name = 'users.html'
    model = User
    context_object_name = 'users' 
