from django.views.generic.edit import CreateView
from main.models.news import News
from django.urls import reverse_lazy

class CreateNewView(CreateView):
    model = News
    fields = ['title', 'image', 'short_text', 'text']
    template_name = 'create.html'
    success_url = reverse_lazy('main')
