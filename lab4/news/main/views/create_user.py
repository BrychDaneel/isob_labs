from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import Group
from django.contrib.auth import logout

from main.forms import RegisterForm

from main.models import EmailConfirm


EMAIL_SUBJECT = 'Подтвердение почты'
EMAIL_TEXT = '{}'
DEFAULT_GROUP = 'User'

class CreateUserView(FormView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('main')

    def form_valid(self, form, request):
        user = form.save(commit=False)
        user.is_active = False
        confirm = EmailConfirm()

        link = reverse('email.confirm', kwargs={'token' : confirm.token})
        url = request.build_absolute_uri(link)
        user.email_user(
                        EMAIL_SUBJECT,
                        EMAIL_TEXT.format(url),
                        from_email=settings.EMAIL_HOST_USER
                       )
        user.save()
        confirm.user = user
        group = Group.objects.get(name=DEFAULT_GROUP)
        user.groups.add(group)
        confirm.save()
        return super(CreateUserView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form, request)
        else:
            return self.form_invalid(form)

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(CreateUserView, self).get(self, request, *args, **kwargs)
