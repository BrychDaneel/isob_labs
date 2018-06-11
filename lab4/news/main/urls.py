from django.conf.urls import url

from django.contrib.auth.decorators import permission_required
from django.urls import reverse_lazy

from main.views import MainView
from main.views import NewDetailView
from main.views import CreateNewView
from main.views import DeleteNewView
from main.views import UpdateNewView
from main.views import CreateUserView
from main.views import DeleteComentView
from main.views import UsersView
from main.views import EmailConfirmView
from main.views import CustomLoginView
from main.views import CustomLogoutView


login_url = reverse_lazy('login')


urlpatterns = [
    url(r'^$', MainView.as_view(), name='main'),

    url(r'^new/(?P<pk>\d+)/$', NewDetailView.as_view(), name='detail'),

    url(r'^new/add', 
        permission_required('main.add_news', login_url=login_url)(CreateNewView.as_view()),
        name='new.add'),

    url(r'^new/(?P<pk>\d+)/delete/$', 
        permission_required('main.delete_news', login_url=login_url)(DeleteNewView.as_view()), name='new.delete'),

    url(r'^new/(?P<pk>\d+)/update/$', 
        permission_required('main.change_news', login_url=login_url)(UpdateNewView.as_view()),
        name='new.update'),

    url(r'^login/$', CustomLoginView.as_view(), name='login'),

    url(r'^logout/$', CustomLogoutView.as_view(), name='logout'),

    url(r'^register/$', CreateUserView.as_view(), name='register'),

    url(
        r'^comments/delete/(?P<pk>\d+)$',
        permission_required('main.delete_coments', login_url=login_url)(DeleteComentView.as_view()),
        name='coment.delete'
       ),

    url(r'^users/$', UsersView.as_view(), name='users'),

    url(r'^users/confirm/(?P<token>'
        r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
        r')$',
        EmailConfirmView.as_view(),
        name='email.confirm'),
]
