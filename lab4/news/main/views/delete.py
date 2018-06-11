from django.views.generic.edit import DeleteView
from main.models.news import News
from django.urls import reverse_lazy

class DeleteNewView(DeleteView):
    model = News
    success_url = reverse_lazy('main')
    template_name = 'news_confirm_delete.html'
    context_object_name = 'new'
