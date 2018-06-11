from django.views.generic.edit import DeleteView
from main.models import Coments
from django.urls import reverse

class DeleteComentView(DeleteView):
    model = Coments
    template_name = 'coments_confirm_delete.html'
    context_object_name = 'coment'

    def get_success_url(self):
        pk = self.get_object().new.pk
        return reverse('detail', kwargs={'pk' : pk})
