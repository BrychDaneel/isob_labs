from django.views.generic.base import TemplateView

from main.models import EmailConfirm


class EmailConfirmView(TemplateView):

    template_name = 'email_confirm.html'

    def get_context_data(self, token, **kwargs):
        context = super().get_context_data(**kwargs)

        confirm = EmailConfirm.objects.filter(token=token)
        exst = confirm.exists()
        context['valid'] = exst

        if exst:
            confirm = confirm.get()
            user = confirm.user
            user.is_active = True
            confirm.delete()
            user.save()

        return context
