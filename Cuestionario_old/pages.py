from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Instrucciones(Page):
    form_model = 'player'
    form_fields = ['primera','segunda','tercera','cuarta','quinta']

class Decision(Page):
    form_model = 'player'
    form_fields = ['decision']
   
   
class Ejercicios_1(Page):
    form_model = 'player'
    form_fields = ['E1','E2','E3','E4','E5']
    timeout_seconds = 5

    
class ResultsWaitPage(Page): 
    @staticmethod
    def app_after_this_page(self):
        self.after_all_players_arrive = True


    def vars_for_template(self):
             
        if self.player.decision == True:
            
            self.player.respuestasOK = self.player.E1 + self.player.E2 + self.player.E3
            self.player.payoff = self.player.var_aleY1 * self.player.respuestasOK
            
        else:

            self.player.respuestasOK = self.player.E1 + self.player.E2 + self.player.E3
            self.player.payoff = self.player.var_aleZ1 * self.player.respuestasOK
            
            
   
                 
class Demografica(Page):
    form_model = 'player'
    form_fields = ['age', 'gender']

page_sequence = [Instrucciones,Decision,Ejercicios_1,ResultsWaitPage]
