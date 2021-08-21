from django.forms import ModelForm

from experimiento_1.models import Player


class MoneyDecisionForm(ModelForm):

    class Meta:
        model = Player
        fields = ['money_decision', 'percentage_saved']