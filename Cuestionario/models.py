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

# ******************************************************************************************************************** #
# ***                                                           UTILITY
# ******************************************************************************************************************** #

def make_radio_button(label, choices, fieldtype):
    return models.fieldtype(
        choices=choices,
        label=label,
        widget=widgets.RadioSelect,
    )

def makefield_urn_decision(choices):
    return models.StringField(
        choices=choices
    )

def makefield_string(label, choices):
    return models.StringField(
        label=label,
        choices=choices,
        widget=widgets.RadioSelect
    )

def makefield_integer():
    return models.IntegerField(initial=0)

# ******************************************************************************************************************** #
# ***                                                           CHOICES
# ******************************************************************************************************************** #

#################### STAGE 1 #######################
choices_urn = [
    ['Y', 'Urna Y'], 
    ['Z', 'Urna Z']
]

choices_gen_instructions1 = [
    [1, '(2+2)*5/2'], 
    [0, '((1+2+3+4+5+6)/7)+7'],
    [0, '((50*10)/2)-200'],
    [0, 'Ninguna de las anteriores']
]

choices_gen_instructions2 = [
    [1,'2 UM'], 
    [2,'0 UM'],
    [3,'8 UM'],
    [4,'Ninguna de las anteriores']
]

choices_gen_instructions3 = [
    [1,'8 UM'], 
    [2,'10 UM'],
    [3,'6 UM'],
    [4,'Ninguna de las anteriores']
]

choices_gen_instructions4 = [
    [1,'144 UM'], 
    [2,'112 UM'],
    [3,'126 UM'],
    [4,'Ninguna de las anteriores']
]

choices_gen_instructions5 = [
    [1,'$2,500'], 
    [2,'$1,680'],
    [3,'$2,800'],
    [4,'Ninguna de las anteriores']
]

# ******************************************************************************************************************** #
# ***                                                       CLASS APPLICATION
# ******************************************************************************************************************** #
class Constants(BaseConstants):
    name_in_url = 'Cuestionario'
    players_per_group = None
    num_rounds = 100
    endowment = c(1)
    minY1 = 0
    minZ1 = 2
    maxY1 = 10
    maxZ1 = 8

class Subsession(BaseSubsession):
    pass
    
#ToDo: agregar funcion para que las variables de pagos del player vayan actualizando la variable de pagos propia de otree
class Player(BasePlayer):

    payment_total = makefield_integer()

# ******************************************************************************************************************** #
# *** STAGE 1
# ******************************************************************************************************************** #
    payment_phase_1 = makefield_integer()
    payment_phase_2 = makefield_integer()
    payment_phase_3 = makefield_integer()
    payment_phase_4 = makefield_integer()
    payment_stage_1 = makefield_integer()
    decision_phase_1 = makefield_urn_decision()
    decision_phase_2 = makefield_urn_decision()
    decision_phase_3 = makefield_urn_decision()
    decision_phase_4 = makefield_urn_decision()
    answer_correct_stage1 = makefield_integer()

    ########## Phase 1 #############
    question_1_gen_instructions = makefield_string(
        '1. ¿Cuál es el valor mínimo de UM que puede salir de la Urna Z?',
        choices_gen_instructions2
    )

    question_2_gen_instructions = makefield_string(
        '2. ¿Cuál es el valor mínimo de UM que puede salir de la Urna Y?',
        choices_gen_instructions2
    )

    question_3_gen_instructions = makefield_string(
        '3. ¿Cuál es el valor máximo de UM que puede salir de la Urna Y?',
        choices_gen_instructions3
    )

    question_4_gen_instructions = makefield_string(
        '4. Si para las rondas 6-10 usted escoge la urna Z y sale al azar una moneda de valor 7 UM, ¿cuántas UM ganará en la ronda 8 si logra 18 respuestas correctas?',
        choices_gen_instructions4
    )

    question_5_gen_instructions = makefield_string(
        '5. Suponga que para las rondas 11-15 usted escoge la urna Y y sale al azar una moneda de valor 3 UM. ¿cuánto dinero ganaría si obtuvo 21 respuestas correctas? ',
        choices_gen_instructions5
    )

# ******************************************************************************************************************** #
# *** STAGE 2
# ******************************************************************************************************************** #
    payment_stage_2 = makefield_integer()
    answer_correct_stage2 = makefield_integer()



