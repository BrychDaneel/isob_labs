from django.forms import ModelForm
from main.models import Coments

class ComentForm(ModelForm):
    class Meta:
        model = Coments
        fields = ['text']
