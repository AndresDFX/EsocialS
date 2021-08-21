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

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'real_effort_numbers2'
    players_per_group = 2
    num_rounds = 2
    payment_per_correct_answer = 50
    payment_per_correct_answer_2 = 50
    fixed_payment = 5000
    sumas_obligatorias_contrato = 3

class Subsession(BaseSubsession):
    def creating_session(self):
        print("Matriz del grupo: " + str(self.get_group_matrix()))
        print("Grupos: " + str(self.get_groups()))
        for player in self.get_players():
            print("Jugador id_group: " + str(player.id_in_group))
            print("Jugador id_session: " + str(player.participant.id_in_session))
        import time
        # user has 5 minutes to complete as many pages as possible
        self.session.vars['expiry'] = time.time() + 15*50   

class Group(BaseGroup):
    pass

class Player(BasePlayer):
# ******************************************************************************************************************** #
# *** Variables Etapa 1
# ******************************************************************************************************************** #    
    number_entered = models.IntegerField(label="")
    sum_of_numbers = models.IntegerField()
    correct_answers = models.IntegerField(initial=0)
    wrong_sums = models.IntegerField(initial=0)
    total_sums = models.IntegerField(initial=0)
    payment_stage_1 = models.IntegerField(initial=0)
    time_management = models.BooleanField()
    time_management_2 = models.BooleanField()
# ******************************************************************************************************************** #
# *** Variables Etapa 2
# ******************************************************************************************************************** #
    number_entered_2 = models.IntegerField(label="")
    sum_of_numbers_2 = models.IntegerField()
    correct_answers_2 = models.IntegerField(initial=0)
    wrong_sums_2 = models.IntegerField(initial=0)
    total_sums_2 = models.IntegerField(initial=0)
    payment_stage_2 = models.IntegerField(initial=0)
    pago = models.IntegerField(initial=0)
# ******************************************************************************************************************** #
# *** Preguntas de Control: 1
# ******************************************************************************************************************** #
    control_question_1 = models.BooleanField(
        label="¿Estaré emparejado con la misma persona en toda la Etapa 1?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ],
        widget = widgets.RadioSelect,
    )

    control_question_2 = models.IntegerField(
        label="Si en la ronda 1, mi compañero(a) y yo logramos 20 sumas correctas, cada uno ganará:",
        choices = [
            [1, "1000"],
            [2, "2000"],
            [3, "3000"],
        ],
        widget = widgets.RadioSelect,
    )
# ******************************************************************************************************************** #
# *** Preguntas de Control: 2
# ******************************************************************************************************************** #
    control_question_3 = models.IntegerField(
        label="T-T y T-NT: En la Etapa 2 usted estará emparejado con:",
        choices = [
            [1, "Nadie, es un juego individual"],
            [2, "Con la misma persona de la Etapa 1"],
            [3, "Con una persona distinta a la de la Etapa 1"],
        ],
        widget = widgets.RadioSelect,
    )

    control_question_4 = models.IntegerField(
        label="¿De dónde salen los $2500 que se le entregan al jugador Y al inicio de la Etapa 1?",
        choices = [
            [1, "Se los entregan las personas que administran esta actividad"],
            [2, "El jugador Y no recibe $2500, sino el jugador X. Ese dinero viene de las ganancias acumuladas del jugador Y"],
            [3, "De las ganancias acumuladas del jugador X."],
            [4, "Todos los jugadores reciben $2500 al iniciar la Etapa 2. No solamente el jugador Y."],
        ],
        widget = widgets.RadioSelect,
    )

    control_question_5 = models.IntegerField(
        label="¿Para qué sirve el contrato?",
        choices = [
            [1, "Para que el jugador X se asegure de que el jugador Y le transfiera los $2500 del salario"],
            [2, "Para que el jugador Y se asegure de que el jugador X realizará un esfuerzo mínimo de 50 sumas en la Etapa 2."],
        ],
        widget = widgets.RadioSelect,
    )

    control_question_6 = models.IntegerField(
        label="Si el jugador Y NO paga por el contrato y el jugador X realiza 100 sumas correctas y 0 incorrectas en todas las rondas, ¿cuánto ganarán los jugadores en la Etapa 2?",
        choices = [
            [1, "Jugador Y = -2500 + (100 sumas x $100) = -2500 + 10000 = 7500. Jugador X = 2500 – (100 sumas x $20) = 2500 – 2000 = 500"],
            [2, "Jugador Y = -2500 + (100 sumas x $30) = -2500 + 3000 = 500. Jugador X = 2500 - (100 sumas x $100) = 2500 –10000 = -7500"],
            [3, "Jugador Y = -2500 + 5000 = 2500. Jugador X = 2500 – 5000 = -2500"],
        ],
        widget = widgets.RadioSelect,
    )

    control_question_7 = models.IntegerField(
        label="Si el jugador Y SÍ paga los $2500 del contrato y el jugador X realiza 10 sumas correctas y 0 incorrectas en todas las rondas, ¿cuánto ganarán los jugadores en la Etapa 2?",
        choices = [
            [1, "Jugador Y = -2500 + (10 sumas x $100) - 2500) = -2500 + 1000 – 2500  = -4000. Jugador X = 2500 – (10 sumas x $20) = 2500 – 200 = 2300"],
            [2, "Jugador Y = -2500 + (10 sumas x $100) - 2500) = -2500 + 1000 – 2500  = -4000. Jugador X = 2500 – (10 sumas x $20) + 2500 = 2500 – 200 + 2500 = 4800"],
            [3, "Jugador Y = -2500 + 5000 – 2500 = 0. Jugador X = 2500 – 5000 = -2500"],
        ],
        widget = widgets.RadioSelect,
    )
# ******************************************************************************************************************** #
# *** Validaciones
# ******************************************************************************************************************** #

    def control_question_1_error_message(self, value):
        if value != True:
            return 'Esta respuesta es incorrecta. Por favor, lea las instrucciones e intente de nuevo.'

    def control_question_2_error_message(self, value):
        if value != 1:
            return 'Recuerde que ganarán $50 por cada respuesta correcta que hayan dado juntos.'

    def control_question_3_error_message(self, value):
        print(value)
        if value != 2:
            return 'Recuerde que usted será emparejado con la misma persona de la Etapa 1.'

    def control_question_4_error_message(self, value):
        if value != 2:
            return 'Por favor, lea nuevamente las instrucciones'         

    def control_question_5_error_message(self, value):
        if value != 2:
            return 'Por favor, lea nuevamente las instrucciones' 

    def control_question_6_error_message(self, value):
        if value != 1:
            return 'Por favor, lea nuevamente las instrucciones' 

    def control_question_7_error_message(self, value):
        if value != 3:
            return 'Por favor, lea nuevamente las instrucciones'

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
# ******************************************************************************************************************** #
# *** Variables Contrato
# ******************************************************************************************************************** #
    pay_contract = models.BooleanField(
        label = "",
         choices = [
            [True, "Sí"],
            [False, "No"],
        ],
        widget = widgets.RadioSelect,
        blank = True
    )
    believe_pay_contract = models.BooleanField(
        label = "",
         choices = [
            [True, "Sí"],
            [False, "No"],
        ],
        widget = widgets.RadioSelect,
        blank = True
    )
    suggested_sums = models.IntegerField(blank = True, label="")

# ******************************************************************************************************************** #
# *** Acceder al otro jugador
# ******************************************************************************************************************** #
    def other_player(self):
        #self.get_others_in_group() -> Vector[<Player  2>, <Player  3>, <Player  4>]
        return self.get_others_in_group()[0]

    def prueba(self):
        all_players = self.in_all_rounds()
        correct_answers = 0
        combined_payoff = 0
        combined_payoff_others = 0
        wrong_sums = 0
        total_sums = 0
        opponent_id = self.other_player().id_in_group
        for player in all_players:
            combined_payoff += player.payoff
            correct_answers += player.correct_answers
            wrong_sums += player.wrong_sums
            total_sums += player.total_sums
        return {
            'combined_payoff' : math.trunc(combined_payoff),
            'correct_answers': correct_answers,
            'opponent_id': opponent_id,
            'wrong_sums': wrong_sums,
            'total_sums': total_sums
        }

  