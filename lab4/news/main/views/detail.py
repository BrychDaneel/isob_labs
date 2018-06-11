from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from datetime import timedelta
from datetime import datetime

from main.models import News
from main.models import Coments
from main.forms import ComentForm


COMMENT_TIME = timedelta(seconds=30)

class NewDetailView(DetailView):
    template_name = 'new.html'
    model = News
    context_object_name = 'new'
    login_url = reverse_lazy('login')

    form = None

    def get_context_data(self, **kwards):
        context = super(NewDetailView, self).get_context_data(**kwards)
        context['coment_form'] = self.form if self.form else ComentForm()
        context['coments'] = Coments.objects.filter(new=self.get_object())
        return context

    def post(self, request, *args, **kwargs):

        if not request.user.has_perm('main.add_coments'):
            return redirect(self.login_url)

        coment_form = ComentForm(request.POST)

        if not coment_form.is_valid():
            self.form = coment_form
            return super(NewDetailView, self).get(request, *args, **kwargs)

        coment = coment_form.save(commit=False)
        coment.user = request.user
        coment.new = self.get_object()

        if Coments.objects.filter(user=coment.user,
                                  pubtime__gte=datetime.now()-COMMENT_TIME
                                 ).exists():
            self.form = coment_form
            self.form.add_error('text', 
                                "Нельзя отправлять комментарии чаще 30 секунд"
                                )
            return super(NewDetailView, self).get(request, *args, **kwargs)

        coment.save()

        return super(NewDetailView, self).get(request, *args, **kwargs)
