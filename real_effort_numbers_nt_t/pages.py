from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import *
import random
import math


# ******************************************************************************************************************** #
# *** STAGE 1
# ******************************************************************************************************************** #

class Consent(Page):
    form_model = 'player'
    form_fields = ['accepts_data', 'num_temporal', 'accepts_terms']

    def is_displayed(self):
        return self.round_number == 1

#=======================================================================================================================


class GenInstructions(Page):
    def is_displayed(self):
        return self.round_number == 1

#=======================================================================================================================


class Stage1Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1

#=======================================================================================================================


class Stage1Questions(Page):
    form_model = 'player'
    form_fields = ['control_question_1', 'control_question_2']

    def is_displayed(self):
        return self.round_number == 1
#=======================================================================================================================


class Start(Page):
    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        import time
        self.participant.vars['expiry'] = time.time() + \
            Constants.num_seconds_stage_1

#=======================================================================================================================


class AddNumbers(Page):
    form_model = 'player'
    form_fields = ['number_entered']
    timeout_seconds = Constants.num_seconds_stage_1
    timer_text = 'Tiempo restante para completar la Ronda: '

    def before_next_page(self):
        self.player.total_sums = 1
        if self.player.sum_of_numbers == self.player.number_entered:
            self.player.payoff = Constants.payment_per_correct_answer
            self.player.correct_answers = 1
        else:
            self.player.wrong_sums = 1

    def is_displayed(self):
        if self.round_number > Constants.sub_rounds_stage_1:
            return False
        elif self.round_number <= Constants.num_rounds/2:
            return True

    def vars_for_template(self):
        number_1 = random.randint(1, Constants.num1_random_stage_1)
        number_2 = random.randint(number_1+1, Constants.num2_random_stage_1)
        correct_answers = 0
        combined_payoff = 0
        wrong_sums = 0
        total_sums = 0
        #Realizar la operacion (Suma o Resta)
        self.player.sum_of_numbers = number_2 - number_1
        all_players = self.player.in_all_rounds()
        me = self.player.id_in_group
        me_in_session = self.player.participant.id_in_session
        others = self.player.get_others_in_group()[0]
        opponent = self.player.other_player()
        correct_answers_opponent = 0
        opponent_id = self.player.other_player().id_in_group
        opponent_id_in_session = self.player.other_player().participant.id_in_session

        for player in all_players:
            combined_payoff += player.payoff
            correct_answers += player.correct_answers
            wrong_sums += player.wrong_sums
            total_sums += player.total_sums

        return {
            'number_1': number_1,
            'number_2': number_2,
            'combined_payoff': math.trunc(combined_payoff),
            'correct_answers': correct_answers,
            'round': self.round_number,
            'opponent_id': opponent_id,
            'wrong_sums': wrong_sums,
            'total_sums': total_sums,
            'opponent_id_in_session': opponent_id_in_session
        }
#=======================================================================================================================


class PartialResults(Page):

    def is_displayed(self):
        if self.round_number > Constants.sub_rounds_stage_1:
            return False
        elif self.round_number <= Constants.num_rounds/2:
            return True

    def vars_for_template(self):

        all_players = self.player.in_all_rounds()
        opponent_id = self.player.other_player().id_in_group
        opponent_id_in_subsession = self.player.other_player().id_in_subsession

        combined_payoff = 0
        combined_payoff_opponent = 0
        combined_payoff_team = 0
        correct_answers = 0
        correct_answers_opponent = 0
        correct_answers_team = 0
        combined_payoff_total = 0

        for player in all_players:
            combined_payoff += player.payoff
            correct_answers += player.correct_answers
            correct_answers_opponent += player.other_player().correct_answers
            combined_payoff_opponent += player.other_player().payoff

        correct_answers_team = correct_answers + correct_answers_opponent
        combined_payoff_team = combined_payoff + combined_payoff_opponent
        combined_payoff_total = combined_payoff_team

        # Si es T-T o T-NT el pago en la etapa uno es el pago del equipo más el pago fijo
        self.player.payment_stage_1 = math.trunc(combined_payoff_total)

        return {
            'combined_payoff': math.trunc(combined_payoff),
            'combined_payoff_opponent': math.trunc(combined_payoff_opponent),
            'correct_answers': correct_answers,
            'correct_answers_opponent': correct_answers_opponent,
            'round_number': self.round_number,
            'opponent_id': opponent_id,
            'opponent_id_in_subsession': opponent_id_in_subsession,
            'correct_answers_team': correct_answers_team,
            'combined_payoff_team': math.trunc(combined_payoff_team)
        }
#=======================================================================================================================


class ResultsWaitPage(WaitPage):
    def is_displayed(self):
        if self.round_number == Constants.sub_rounds_stage_1 + 1:
            return True

#=======================================================================================================================


class CombinedResults(Page):
    def is_displayed(self):
        return self.round_number == (Constants.num_rounds/2)+1

    def vars_for_template(self):
        all_players = self.player.in_all_rounds()
        all_others = self.player.get_others_in_group()[0].in_all_rounds()
        others = self.player.get_others_in_group()[0]
        combined_payoff = 0
        correct_answers = 0
        correct_answers_opponent = 0
        correct_answers_team = 0
        combined_payoff_opponent = 0
        combined_payoff_team = 0
        combined_payoff_total = 0
        opponent = self.player.other_player()
        opponent_id = self.player.other_player().id_in_group
        opponent_id_in_subsession = self.player.other_player().id_in_subsession

        for player in all_players:
            combined_payoff += player.payoff
            correct_answers += player.correct_answers
            correct_answers_opponent += player.other_player().correct_answers
            combined_payoff_opponent += player.other_player().payoff

        correct_answers_team = correct_answers + correct_answers_opponent
        combined_payoff_team = combined_payoff + combined_payoff_opponent
        combined_payoff_total = combined_payoff

        #Si es T-T o T-NT el pago en la etapa uno es el pago del equipo más el pago fijo
        self.player.payment_stage_1 = math.trunc(combined_payoff_total)
        return {
            'combined_payoff': math.trunc(combined_payoff),
            'combined_payoff_opponent': math.trunc(combined_payoff_opponent),
            'correct_answers': correct_answers,
            'correct_answers_opponent': correct_answers_opponent,
            'round_number': self.round_number,
            'opponent_id': opponent_id,
            'opponent_id_in_subsession': opponent_id_in_subsession,
            'correct_answers_team': correct_answers_team,
            'combined_payoff_team': math.trunc(combined_payoff_team),
            'combined_payoff_total': self.player.payment_stage_1
        }

# ******************************************************************************************************************** #
# *** STAGE 2
# ******************************************************************************************************************** #
class Stage2Instructions(Page):
    def is_displayed(self):
        return self.round_number == (Constants.num_rounds/2)+1

#=======================================================================================================================

class Stage2Questions(Page):
    form_model = 'player'
    form_fields = ['control_question_4', 'control_question_5',
                   'control_question_6', 'control_question_7', 'control_question_8', 'control_question_9']

    def is_displayed(self):
        return self.round_number == (Constants.num_rounds/2)+1

#=======================================================================================================================

class RoleAssignment(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.round_number == (Constants.num_rounds/2)+1

#=======================================================================================================================

class Decision(Page):
    form_model = 'player'
    form_fields = ['pay_contract', 'believe_pay_contract']

    def is_displayed(self):
        return self.round_number == (Constants.num_rounds/2)+1

    def vars_for_template(self):
        me = self.player.id_in_group
        titulo = ""
        if me == 1:
            titulo = "Decision Jugador X - Parte 1"
        else:
            titulo = "Decision Jugador Y - Parte 1"
        return{
            'titulo': titulo
        }

#=======================================================================================================================


class ResultsWaitPage3(WaitPage):
    def is_displayed(self):
        return self.round_number == (Constants.num_rounds/2)+1

#=======================================================================================================================


class Decision2(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.round_number == (Constants.num_rounds/2)+1

    def vars_for_template(self):
        me = self.player.id_in_group
        opponent = self.player.other_player()
        opponent_contract_decision = opponent.pay_contract
        titulo = ""
        if me == 1:
            titulo = "Reporte de decisión Jugador X"
        else:
            titulo = "Decision Jugador Y - Parte 2"
        return{
            'titulo': titulo,
            'opponent_contract_decision': opponent_contract_decision
        }

#=======================================================================================================================


class Start2(Page):
    def is_displayed(self):
        return self.round_number == (Constants.num_rounds/2)+1

    def before_next_page(self):
        import time
        self.participant.vars['expiry'] = time.time() + \
            Constants.num_seconds_stage_2

#=======================================================================================================================


class AddNumbers2(Page):
    form_model = 'player'
    form_fields = ['number_entered_2']
    timer_text = 'Tiempo restante para completar la Etapa 2:'

    def before_next_page(self):
        self.player.total_sums_2 = 1
        if self.player.sum_of_numbers_2 == self.player.number_entered_2:
            self.player.pago = Constants.payment_per_correct_answer_2
            self.player.correct_answers_2 = 1
        else:
            self.player.wrong_sums_2 = 1

    def get_timeout_seconds(self):
        import time
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        if self.round_number >= (Constants.num_rounds/2)+1:
            return self.get_timeout_seconds() > 3

    def vars_for_template(self):
        number_1 = random.randint(1, Constants.num1_random_stage_2)
        number_2 = random.randint(number_1+1, Constants.num2_random_stage_2)
        correct_answers = 0
        combined_payoff = 0
        wrong_sums = 0
        total_sums = 0
        self.player.sum_of_numbers_2 = number_2 - number_1
        all_players = self.player.in_all_rounds()
        opponent_id = self.player.other_player().id_in_group
        opponent_id_in_session = self.player.other_player().participant.id_in_session

        for player in all_players:
            combined_payoff += player.pago
            correct_answers += player.correct_answers_2
            wrong_sums += player.wrong_sums_2
            total_sums += player.total_sums_2

        opponent_contract_decision = self.player.other_player().in_round(
            (Constants.num_rounds/2)+1).pay_contract

        return {
            'number_1': number_1,
            'number_2': number_2,
            'combined_payoff': math.trunc(combined_payoff),
            'correct_answers': correct_answers,
            'round_number': self.round_number,
            'opponent_id': opponent_id,
            'wrong_sums': wrong_sums,
            'total_sums': total_sums,
            'opponent_contract_decision': opponent_contract_decision,
            'opponent_id_in_session': opponent_id_in_session
        }

#=======================================================================================================================


class ResultsWaitPage2(WaitPage):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

#=======================================================================================================================


class SecondQuoteY(Page):
    form_model = 'player'
    form_fields = ['pay_second_quote']

    def is_displayed(self):
        if self.player.id_in_group == 2:
            return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        opponent = self.player.other_player()
        contract_decision = self.player.in_round(
            (Constants.num_rounds/2)+1).pay_contract
        correct_answers_2_opponent = 0
        all_players = self.player.in_all_rounds()

        for player in all_players:
            correct_answers_2_opponent += player.other_player().correct_answers_2

        return {
            'contract_decision': contract_decision,
            'correct_answers_2_opponent': correct_answers_2_opponent
        }
#=======================================================================================================================


class WaitPageX(WaitPage):
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return self.round_number == Constants.num_rounds

#=======================================================================================================================


class SecondQuoteX(Page):
    form_model = 'player'

    def is_displayed(self):
        if self.player.id_in_group == 1:
            return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        opponent = self.player.other_player()
        opponent_pay_second_quote = opponent.in_round(
            (Constants.num_rounds/2)+1).pay_second_quote
        opponent_contract_decision = opponent.in_round(
            (Constants.num_rounds/2)+1).pay_contract
        correct_answers_2 = 0
        all_players = self.player.in_all_rounds()

        for player in all_players:
            correct_answers_2 += player.correct_answers_2

        return {
            'opponent_pay_second_quote': opponent_pay_second_quote,
            'opponent_contract_decision': opponent_contract_decision,
            'correct_answers_2': correct_answers_2
        }

#=======================================================================================================================


class CombinedResults2(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        # self.player.get_others_in_group()[0] == self.player.other_player() -> Player Object
        all_players = self.player.in_all_rounds()
        all_others = self.player.get_others_in_group()[0].in_all_rounds()
        others = self.player.get_others_in_group()[0]
        combined_payoff = 0
        correct_answers = 0
        correct_answers_opponent = 0
        correct_answers_team = 0
        combined_payoff_opponent = 0
        combined_payoff_team = 0
        combined_payoff_total = 0
        opponent = self.player.other_player()
        opponent_id = self.player.other_player().id_in_group
        correct_answers = 0
        combined_payoff = 0
        wrong_sums_2 = 0
        total_sums_2 = 0
        wrong_sums_2_opponent = 0
        total_sums_2_opponent = 0
        me = self.player.id_in_group
        titulo = ""
        contrato = 0
        pay_contract = self.player.in_round(
            (Constants.num_rounds/2)+1).pay_contract
        pay_contract_label = ""
        opponent_contract_decision = opponent.in_round(
            (Constants.num_rounds/2)+1).pay_contract
        opponent_pay_second_quote = opponent.in_round(
            (Constants.num_rounds/2)+1).pay_second_quote
        opponent_contract_decision_label = ""

        if me == 1:
            titulo = "Pagos Etapa 2 - Jugador X"
        else:
            titulo = "Pagos Etapa 2 - Jugador Y"
            opponent_pay_second_quote = self.player.pay_second_quote

        for player in all_players:
            combined_payoff += player.payoff
            correct_answers += player.correct_answers_2
            correct_answers_opponent += player.other_player().correct_answers_2
            combined_payoff_opponent += player.other_player().pago
            wrong_sums_2 += player.wrong_sums_2
            wrong_sums_2_opponent += player.other_player().wrong_sums_2
            total_sums_2 += player.total_sums_2
            total_sums_2_opponent += player.other_player().total_sums_2

        #Labels:
        if opponent_contract_decision == True:
            opponent_contract_decision_label = "Sí"

        if opponent_contract_decision == False:
            opponent_contract_decision_label = "No"

        if pay_contract == False:
            pay_contract_label = "No"

        if pay_contract == True:
            pay_contract_label = "Sí"

        ############### JUGADOR X ###############
        if player.id_in_group == 1:

            if opponent_contract_decision:  # Con contrato
                if total_sums_2 >= Constants.restas_obligatorias_contrato:  # Si cumple con la cantidad de restas
                    self.player.payment_stage_2 = 12000
                else:  # Si no cumple con la cantidad de restas
                    self.player.payment_stage_2 = -18000

            else:  # Sin contrato
                if not opponent_pay_second_quote:  # Solo la primera cuota
                    self.player.payment_stage_2 = 8000
                else:  # Pagando el jugador Y ambas cuotas
                    self.player.payment_stage_2 = 15000

        ############### JUGADOR Y ###############
        if player.id_in_group == 2:

            if pay_contract:  # Con contrato
                self.player.payment_stage_2 = 10000

            else:  # Sin contrato
                if total_sums_2_opponent >= Constants.restas_obligatorias_contrato:  # Si X cumple con la cantidad de restas
                    if not opponent_pay_second_quote:  # Si decide no pagar la segunda cuota
                        self.player.payment_stage_2 = 22000
                    else:  # Si decide pagar la segunda cuota
                        self.player.payment_stage_2 = 15000

                else:  # Si X no cumple con la cantidad de restas
                    if not opponent_pay_second_quote:  # Si decide no pagar la segunda cuota
                        self.player.payment_stage_2 = -8000
                    else:  # Si decide pagar la segunda cuota
                        self.player.payment_stage_2 = -15000

        combined_payoff_total = self.player.payment_stage_2 + \
            self.player.in_round(Constants.num_rounds/2).payment_stage_1
        ganancias_acumuladas = self.player.in_round(
            Constants.num_rounds/2).payment_stage_1 + self.player.payment_stage_2

        return {
            'payment_stage_1': self.player.in_round(Constants.num_rounds/2).payment_stage_1,
            'payment_stage_2': self.player.payment_stage_2,
            'combined_payoff_total': math.trunc(combined_payoff_total),
            'contrato': contrato,
            'titulo': titulo,
            'opponent_contract_decision': opponent_contract_decision_label,
            'pay_contract': pay_contract_label,
            'correct_answers': correct_answers,
            'correct_answers_opponent': correct_answers_opponent,
            'total_sums_2': total_sums_2,
            'total_sums_2_opponent': total_sums_2_opponent,
            'ganancias_acumuladas': ganancias_acumuladas
        }

# ******************************************************************************************************************** #
# *** STAGE 3
# ******************************************************************************************************************** #


class PlayCoin(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

#=======================================================================================================================


class DoubleMoney(Page):
    form_model = 'player'
    form_fields = ['monto']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

#=======================================================================================================================


class HeadTails(Page):
    form_model = 'player'
    form_fields = ['cara_sello_value']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        inversion = math.trunc(c(self.player.monto))
        self.player.countFlips = 1
        return {
            'inversion': inversion
        }
#=======================================================================================================================


class ResultsDoubleMoney(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        cara_sello_name = ""
        combined_payoff = 0
        cara_sello_payof = 0

        #Si ya se lanzo la moneda una vez
        if self.player.countFlips == 1:
            self.player.countFlips += 1
            inversion = math.trunc(c(self.player.monto))
            if(self.player.cara_sello_value <= 0.5):
                cara_sello_name = "rojo"
                self.player.monto = 5000-inversion + \
                    math.trunc(self.player.monto*2)
            else:
                cara_sello_name = "azul"
                self.player.monto = 5000-inversion

            return {
                'inversion': inversion,
                'cara_sello_name': cara_sello_name,
                'cara_sello_payoff': self.player.monto,
                'flips': self.player.countFlips,
            }
        else:
            inversion = math.trunc(c(self.player.monto))
            if(self.player.cara_sello_value <= 0.5):
                cara_sello_name = "rojo"
            else:
                cara_sello_name = "azul"
            return {
                'inversion': inversion,
                'cara_sello_name': cara_sello_name,
                'cara_sello_payoff': self.player.monto,
                'flips': self.player.countFlips,
                'cara_sello': self.player.cara_sello_value

            }

#=======================================================================================================================


class CombinedResults3(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        ganancias_acumuladas = self.player.in_round(
            Constants.num_rounds/2).payment_stage_1 + self.player.payment_stage_2 + self.player.monto
        return {
            'payment_stage_1': self.player.in_round(Constants.num_rounds/2).payment_stage_1,
            'payment_stage_2': self.player.payment_stage_2,
            'payment_stage_3': self.player.monto,
            'ganancias_acumuladas': ganancias_acumuladas
        }

#=======================================================================================================================


class SocioDemSurvey(Page):
    form_model = 'player'
    form_fields = [
        'edad',
        'ciudad',
        'rol_hogar',
        'estado_civil',
        'hijos',
        'etnia',
        'religion',
        'estudios',
        'actividad_actual',
        'esta_laborando',
        'ingreso_mensual',
        'gasto_mensual',
        'alimentos',
        'aseo',
        'electronicos',
        'transporte',
        'servicios',
        'diversion',
        'ahorro',
        'deudas',
        'offer_1',
        'Estabilidad',
        'Independencia',
        'Descanso',
        'Lucro',
        'Protección',
        'encuesta_tabla1_pregunta1',
        'encuesta_tabla1_pregunta2',
        'encuesta_tabla1_pregunta3',
        'encuesta_tabla1_pregunta4',
        'encuesta_tabla1_pregunta5',
        'encuesta_tabla1_pregunta6',
        'encuesta_tabla1_pregunta7',
        'encuesta_tabla1_pregunta8',
        'encuesta_tabla1_pregunta9',
        'encuesta_tabla1_pregunta10',
        'encuesta_tabla2_pregunta1',
        'encuesta_tabla2_pregunta2',
        'encuesta_tabla2_pregunta3',
        'encuesta_tabla2_pregunta4',
        'encuesta_tabla2_pregunta5',
        'encuesta_tabla2_pregunta6',
        'encuesta_tabla2_pregunta7',
        'encuesta_tabla2_pregunta8',
        'encuesta_tabla2_pregunta9',
        'encuesta_tabla3_pregunta1',
        'encuesta_tabla3_pregunta2',
        'encuesta_tabla3_pregunta3',
        'encuesta_tabla3_pregunta4',
        'encuesta_tabla3_pregunta5',
        'encuesta_tabla3_pregunta6',
        'encuesta_tabla3_pregunta7',
        'encuesta_tabla3_pregunta8',
        'encuesta_tabla3_pregunta9',
        'encuesta_tabla3_pregunta10',
        'encuesta_tabla3_pregunta11',
        'encuesta_tabla3_pregunta12',
        'encuesta_tabla3_pregunta13',
        'encuesta_tabla3_pregunta14',
        'encuesta_tabla3_pregunta15',
        'encuesta_tabla3_pregunta16',
        'encuesta_tabla3_pregunta17',
        'encuesta_tabla3_pregunta18',
        'encuesta_tabla3_pregunta19',
        'encuesta_tabla3_pregunta20',
        'encuesta_tabla3_pregunta21',
        'encuesta_tabla3_pregunta22',
        'encuesta_tabla3_pregunta23',
        'encuesta_tabla3_pregunta24',
        'encuesta_tabla3_pregunta25',
        'encuesta_tabla3_pregunta26',
    ]

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

#=======================================================================================================================


class CombinedResults4(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        ganancias_acumuladas = self.player.in_round(
            Constants.num_rounds/2).payment_stage_1 + self.player.payment_stage_2 + self.player.monto + 5000
        return {
            'payment_stage_1': self.player.in_round(Constants.num_rounds/2).payment_stage_1,
            'payment_stage_2': self.player.payment_stage_2,
            'payment_stage_3': self.player.monto,
            'ganancias_acumuladas': ganancias_acumuladas
        }

#=======================================================================================================================


class ReminderNequi(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        num_temporal = self.player.in_round(1).num_temporal
        ganancias_acumuladas = self.player.in_round(
            Constants.num_rounds/2).payment_stage_1 + self.player.payment_stage_2 + self.player.monto + Constants.fixed_payment
        return {
            'ganancias_acumuladas': ganancias_acumuladas,
            'num_temporal': num_temporal
        }


# ******************************************************************************************************************** #
# *** MANAGEMENT STAGE
# ******************************************************************************************************************** #
stage_1_sequence = [Consent, GenInstructions, Stage1Instructions, Stage1Questions,
                    Start, AddNumbers, PartialResults, ResultsWaitPage, CombinedResults]
stage_2_sequence = [Stage2Instructions, Stage2Questions, RoleAssignment, Decision, ResultsWaitPage3,
                    Decision2, Start2, AddNumbers2, ResultsWaitPage2, SecondQuoteY, WaitPageX, SecondQuoteX, CombinedResults2]
stage_3_sequence = [PlayCoin, DoubleMoney, HeadTails, ResultsDoubleMoney,
                    CombinedResults3, SocioDemSurvey, CombinedResults4, ReminderNequi]

page_sequence = stage_1_sequence + stage_2_sequence + stage_3_sequence
