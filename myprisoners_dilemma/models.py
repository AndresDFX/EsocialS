from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'myprisoners_dilemma'
    players_per_group = 2 
    num_rounds = 2
    payoff_both_cooperate = -1 #Ambos cooperan, es decir ambos mantienen callados (1 año en prision)
    payoff_both_defect = -3 # Ambos se traicionan 
    payoff_different_defect = 0 #El que traiciona al otro sale libre
    payoff_different_cooperate = -4 #Al que traicionan y se queda en la carcel 

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    has_defected = models.BooleanField(
    choices = [
        [True, "Defect" ],
        [False, "Cooperate"],
    ],
    label = "Please choose your action"
    )
