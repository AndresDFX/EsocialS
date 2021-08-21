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

import math
doc = """
Gift_exhange game.
"""


class Constants(BaseConstants):
    name_in_url = 'prisoner'
    players_per_group = 2
    num_rounds = 3

    instructions_template = 'prisoner/instructions.html'

    # payoff if 1 player defects and the other cooperates""",
    betray_payoff = 30000
    betrayed_payoff = 0

    # payoff if both players cooperate or both defect
    both_cooperate_payoff = 20000
    both_defect_payoff = 10000


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def set_payoffs(self):
        for p in self.get_players():
            p.set_payoff()


class Player(BasePlayer):
    decision = models.StringField(
        choices=[['Coopera', 'Coopera'], ['Traiciona', 'Traiciona']],
        doc="""Decisión del jugador""",
        widget=widgets.RadioSelect,
    )
 # ******************************************************************************************************************** #
# *** Variables Consentimiento
# ******************************************************************************************************************** #
    num_temporal = models.IntegerField(label= "Por favor, ingrese el numero de identificación temporal que le llegó en el correo de invitación")
    accepts_data = models.BooleanField(
        label = "¿Autoriza el uso de los datos recolectados para futuros estudios?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ],
        default=True)
    accepts_terms = models.BooleanField()

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        payoff_matrix = dict(
            Coopera=dict(
                Coopera=Constants.both_cooperate_payoff,
                Traiciona=Constants.betrayed_payoff,
            ),
            Traiciona=dict(
                Coopera=Constants.betray_payoff,
                Traiciona=Constants.both_defect_payoff
            ),
        )

        self.payoff = payoff_matrix[self.decision][self.other_player().decision]
