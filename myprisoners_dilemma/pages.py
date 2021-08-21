from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Decision(Page):
    form_model = "player"
    form_fields = ["has_defected"]

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        player_1, player_2 = self.group.get_players()
        if player_1.has_defected: #P1 Traiciona
            if player_2.has_defected: #P2 También traiciona
                player_1.payoff = Constants.payoff_both_defect #Ambos se traicionan
                player_2.payoff = Constants.payoff_both_defect #Ambos se traicionan
            else: #P2 Cooperó
                player_1.payoff = Constants.payoff_different_defect #Sale libre porque lo traicionó
                player_2.payoff = Constants.payoff_different_cooperate #Toma 4 años
        else: #P1 Coopera
            if player_2.has_defected: #P2 traiciona
                player_1.payoff = Constants.payoff_different_cooperate #P1 toma 4 años
                player_2.payoff = Constants.payoff_different_defect #P2 sale libre
            else:
                player_1.payoff = Constants.payoff_both_cooperate #Ambos cooperan 1 año cada uno
                player_2.payoff = Constants.payoff_both_cooperate #Ambos cooperan 1 año cada uno
        return True
    
class Results(Page):
    pass

page_sequence = [Decision, ResultsWaitPage, Results]
