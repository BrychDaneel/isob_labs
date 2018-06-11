from django.views.generic.edit import UpdateView
from main.models.news import News
from django.urls import reverse_lazy

class UpdateNewView(UpdateView):
    model = News
    fields = ['title', 'image', 'short_text', 'text']
    success_url = reverse_lazy('main')
    template_name = 'update.html'
