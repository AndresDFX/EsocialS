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
    name_in_url = 'testapp'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(label = "Please enter your age")
    gender = models.StringField(
        label = "Please choose your gender",
        choices = ["Male", "Female", "Other", "Prefer not to say"],
        )
    is_lef_handed = models.BooleanField(
        label = "Are you lefthanded?",
        choices = [
            [True, "Yes"],
            [False, "No"],
        ],
        )