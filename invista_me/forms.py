from django.forms import ModelForm
from .models import Investimento

class InvestimentoForm(ModelForm):
    class Meta:
        model = Investimento
        fields = '__all__' #para exibir todos os campos
        # fields = ['nome', 'valor'] #caso queira selecionar os valores