from django.views.generic.list import ListView

from main.models import News

class MainView(ListView):
    template_name = 'main.html'
    model = News
    context_object_name = 'news'
