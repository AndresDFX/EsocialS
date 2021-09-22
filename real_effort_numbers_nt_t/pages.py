from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import *
import random, math

# ******************************************************************************************************************** #
# *** UTILS
# ******************************************************************************************************************** #

def get_data(player, list_atrr):
    values = []
    for attr in list_atrr:
        values.append(getattr(player, attr))
    return values

def set_data(player, list_atrr, values):
    for i,atrr in enumerate(list_atrr):
        setattr(player, atrr, values[i])

#TODO: Not work if method get_forms_fields is present in Class Page.
def get_and_set_data(self_player, player, list_atrr):
    values = get_data(self_player, list_atrr)
    set_data(player, list_atrr, values)

def get_and_set_data_one_atrr(self_player, player, list_atrr, round_index, self_atrr):
    atrr = list_atrr[round_index]
    value = getattr(self_player, self_atrr)
    setattr(player, atrr, value)

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

#=======================================================================================================================

class AddNumbers(Page):
    form_model = 'player'
    timeout_seconds = Constants.num_seconds_stage_1
    timer_text = 'Tiempo restante para completar la Ronda: '

    def is_displayed(self):
        if self.round_number <= Constants.sub_rounds_stage_1:
            return self.round_number == self.round_number

    def vars_for_template(self):     
        player = self.player                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        number_1 = random.randint(1, Constants.num1_random_stage_1 )
        number_2 = random.randint(number_1+1, Constants.num2_random_stage_1)
        correct_answers_actual_round = player.correct_answers_actual_round 
        total_substract_actual_round = player.total_substract_actual_round 
        wrong_substract_actual_round = player.wrong_substract_actual_round
        payment_actual_round = player.payment_actual_round 

        return {
            'number_1': number_1,
            'number_2': number_2,
            'correct_answers_actual_round': correct_answers_actual_round,
            'total_substract_actual_round': total_substract_actual_round,
            'wrong_substract_actual_round': wrong_substract_actual_round,
            'payment_actual_round': payment_actual_round
        }

    def live_method(self, data):
        player = self  
        correct_answer = int(data)
        number_1 = random.randint(1, Constants.num1_random_stage_1 )
        number_2 = random.randint(number_1+1, Constants.num2_random_stage_1)
        
        self.correct_answers_actual_round = self.correct_answers_actual_round + correct_answer
        self.total_substract_actual_round  = self.total_substract_actual_round + 1
        self.wrong_substract_actual_round = self.total_substract_actual_round - self.correct_answers_actual_round 
        self.payment_actual_round = self.payment_actual_round + (Constants.payment_per_correct_answer * correct_answer)

        correct_answers_actual_round = self.correct_answers_actual_round 
        total_substract_actual_round = self.total_substract_actual_round 
        wrong_substract_actual_round = self.wrong_substract_actual_round
        payment_actual_round = self.payment_actual_round 

        response = dict(
            number_1=number_1,
            number_2=number_2,
            correct_answers_actual_round=correct_answers_actual_round,
            total_substract_actual_round=total_substract_actual_round,
            wrong_substract_actual_round=wrong_substract_actual_round,
            payment_actual_round=payment_actual_round
        )
        return {
            player.id_in_group: response
        }

#=======================================================================================================================
class ResultsWaitPage(WaitPage):
    def is_displayed(self):
        if self.round_number <= Constants.sub_rounds_stage_1:
            return self.round_number == self.round_number

#=======================================================================================================================

class PartialResults(Page):

    timeout_seconds = Constants.timeout_result_round
    timer_text = 'La siguiente ronda comenzara automaticamente en: '

    def is_displayed(self):
        if self.round_number <= Constants.sub_rounds_stage_1:
            return self.round_number == self.round_number

    def vars_for_template(self):
        player = self.player 
        player_round1 = player.in_round(1)
        opponent = player.other_player()
        opponent_id = self.player.other_player().id_in_group
        opponent_id_in_subsession = self.player.other_player().id_in_subsession

        combined_payoff = player.payment_actual_round
        combined_payoff_opponent = opponent.payment_actual_round
        combined_payoff_team = combined_payoff + combined_payoff_opponent
        correct_answers = player.correct_answers_actual_round
        correct_answers_opponent = opponent.correct_answers_actual_round
        correct_answers_team = correct_answers + correct_answers_opponent

        get_and_set_data_one_atrr(player, player_round1, Constants.list_atrr_round, 
                                    self.round_number-1, 'correct_answers_actual_round')

        return {
            'combined_payoff' : math.trunc(combined_payoff),
            'combined_payoff_opponent': math.trunc(combined_payoff_opponent),
            'correct_answers': correct_answers,
            'correct_answers_opponent': correct_answers_opponent,
            'opponent_id': opponent_id,
            'opponent_id_in_subsession': opponent_id_in_subsession,
            'correct_answers_team': correct_answers_team,
            'combined_payoff_team': math.trunc(combined_payoff_team)
        }
        
#=======================================================================================================================

class CombinedResults(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        player_round1 = self.player.in_round(1)
        me_in_other_rounds = self.player.in_rounds(1, Constants.sub_rounds_stage_1)
        combined_payoff = 0
        correct_answers = 0
        correct_answers_opponent = 0
        correct_answers_team = 0
        combined_payoff_opponent = 0
        combined_payoff_team = 0
        combined_payoff_total = 0
        total_substract = 0
        opponent_id = self.player.other_player().id_in_group
        opponent_id_in_subsession = self.player.other_player().id_in_subsession

        for player in me_in_other_rounds:
            combined_payoff += player.payment_actual_round
            correct_answers += player.correct_answers_actual_round
            total_substract += player.total_substract_actual_round
            correct_answers_opponent += player.other_player().correct_answers_actual_round
            combined_payoff_opponent += player.other_player().payment_actual_round

        correct_answers_team = correct_answers + correct_answers_opponent
        combined_payoff_team = combined_payoff + combined_payoff_opponent
        combined_payoff_total = combined_payoff

        #Si es T-T o T-NT el pago en la etapa uno es el pago del equipo más el pago fijo
        player_round1.payment_stage_1 = math.trunc(combined_payoff_total)
        player_round1.answers_correct_stage_1 = correct_answers
        player_round1.answers_total_stage_1 =  total_substract
        player_round1.answers_wrong_stage_1 =  total_substract - correct_answers

        return {
            'combined_payoff' : math.trunc(combined_payoff),
            'combined_payoff_opponent': math.trunc(combined_payoff_opponent),
            'correct_answers': correct_answers,
            'correct_answers_opponent': correct_answers_opponent,
            'round_number' : self.round_number,
            'opponent_id': opponent_id,
            'opponent_id_in_subsession': opponent_id_in_subsession,
            'correct_answers_team': correct_answers_team,
            'combined_payoff_team': math.trunc(combined_payoff_team),
            'combined_payoff_total': combined_payoff_total
        }


# ******************************************************************************************************************** #
# *** STAGE 2
# ******************************************************************************************************************** #

class Stage2Instructions(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

#=======================================================================================================================
class Stage2Instructions2(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

#=======================================================================================================================
class Stage2Instructions3(Page):

    form_model = 'player'
    form_fields = ['control_question_4', 'control_question_5', 'control_question_6', 'control_question_7', 'control_question_8', 'control_question_9']
    
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

#=======================================================================================================================

class Stage2Instructions4(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

#=======================================================================================================================
class Stage2Instructions5(Page):

    form_model = 'player'
    form_fields = ['control_question_3']
    
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

#=======================================================================================================================
class RoleAssignment(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

#=======================================================================================================================
class Decision(Page):
    form_model = 'player'
    form_fields = ['pay_contract', 'believe_pay_contract']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    
    def before_next_page(self):
        player = self.player.in_round(1)
        list_atrr = self.form_fields
        get_and_set_data(self.player, player, list_atrr)

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
        return self.round_number == Constants.num_rounds

#=======================================================================================================================

class Decision2(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

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
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        player = self.player
        opponent = player.other_player()

        contract_decision = player.pay_contract
        opponent_contract_decision = opponent.pay_contract

        return{
            'contract_decision': contract_decision,
            'opponent_contract_decision': opponent_contract_decision
        }

#=======================================================================================================================

class AddNumbers2(Page):
    form_model = 'player'
    timer_text = 'Tiempo restante para completar la Etapa 2:'
    timeout_seconds = Constants.num_seconds_stage_2
    
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
        
    def vars_for_template(self):     
        player = self.player                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        number_1 = random.randint(1, Constants.num1_random_stage_2)
        number_2 = random.randint(number_1+1, Constants.num2_random_stage_2)
        correct_answers_actual_round = player.correct_answers_actual_round 
        total_substract_actual_round = player.total_substract_actual_round 
        wrong_substract_actual_round = player.wrong_substract_actual_round
        payment_actual_round = player.payment_actual_round 

        return {
            'number_1': number_1,
            'number_2': number_2,
            'correct_answers_actual_round': correct_answers_actual_round,
            'total_substract_actual_round': total_substract_actual_round,
            'wrong_substract_actual_round': wrong_substract_actual_round,
            'payment_actual_round': payment_actual_round
        }

    def live_method(self, data):
        try:
            player = self  
            correct_answer = int(data)
            number_1 = random.randint(1, Constants.num1_random_stage_1 )
            number_2 = random.randint(number_1+1, Constants.num2_random_stage_1)
            
            player.correct_answers_actual_round = player.correct_answers_actual_round + correct_answer
            player.total_substract_actual_round  = player.total_substract_actual_round + 1
            player.wrong_substract_actual_round = player.total_substract_actual_round - player.correct_answers_actual_round 
            player.payment_actual_round = player.payment_actual_round + (Constants.payment_per_correct_answer * correct_answer)

            correct_answers_actual_round = player.correct_answers_actual_round 
            total_substract_actual_round = player.total_substract_actual_round 
            wrong_substract_actual_round = player.wrong_substract_actual_round
            payment_actual_round = player.payment_actual_round 

            response = dict(
                number_1=number_1,
                number_2=number_2,
                correct_answers_actual_round=correct_answers_actual_round,
                total_substract_actual_round=total_substract_actual_round,
                wrong_substract_actual_round=wrong_substract_actual_round,
                payment_actual_round=payment_actual_round
            )
            return {
                player.id_in_group: response
            }
        except AttributeError as e:
            print("Excepcion conrolada", e)
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

    def before_next_page(self):
        player = self.player.in_round(1)
        list_atrr = self.form_fields
        get_and_set_data(self.player, player, list_atrr)

    def vars_for_template(self):
        contract_decision = self.player.pay_contract
        correct_answers_2_opponent = self.player.other_player().correct_answers_actual_round

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

    def is_displayed(self):
        if self.player.id_in_group == 1:
            return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        player = self.player
        opponent = self.player.other_player()
        opponent_pay_second_quote = opponent.pay_second_quote
        opponent_contract_decision = opponent.pay_contract
        answers_correct_stage_2 = player.correct_answers_actual_round

        return {
            'opponent_pay_second_quote': opponent_pay_second_quote,
            'opponent_contract_decision': opponent_contract_decision,
            'answers_correct_stage_2': answers_correct_stage_2
        }

#=======================================================================================================================

class CombinedResults2(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        player = self.player
        player_round1 = self.player.in_round(1)
        me = player.id_in_group
        opponent = player.other_player()
        titulo = ""
        pay_contract_label = ""
        opponent_contract_decision_label = ""
        answer_correct_stage_2 = 0
        answer_correct_stage_2_opponent = 0
        combined_payoff_total = 0
        answer_correct_stage_2 = 0
        answers_total_stage_2 = 0
        answers_total_stage_2_opponent = 0
        contrato = 0
        
        pay_contract = player.pay_contract
        opponent_contract_decision = opponent.pay_contract
        opponent_pay_second_quote = False
        
        if me == 1:
            titulo = "Pagos Etapa 2 - Jugador X"
        else:
            titulo = "Pagos Etapa 2 - Jugador Y"
            opponent_pay_second_quote = self.player.pay_second_quote
                   
        answer_correct_stage_2 = player.correct_answers_actual_round
        answer_correct_stage_2_opponent = opponent.correct_answers_actual_round
        answers_total_stage_2 = player.total_substract_actual_round
        answers_total_stage_2_opponent = opponent.total_substract_actual_round

        player.answers_correct_stage_2 = answer_correct_stage_2
        player.answers_total_stage_2 = answers_total_stage_2
        player.answers_wrong_stage_2 = answers_total_stage_2 - answer_correct_stage_2


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

            if opponent_contract_decision: # Con contrato
                if answers_total_stage_2 >= Constants.mandatory_subtraction: #Si cumple con la cantidad de restas
                    self.player.payment_stage_2 = 12000
                else: #Si no cumple con la cantidad de restas
                    self.player.payment_stage_2 = -18000

            else: # Sin contrato
                if not opponent_pay_second_quote: #Solo la primera cuota
                    self.player.payment_stage_2 = 8000
                else: #Pagando el jugador Y ambas cuotas
                    self.player.payment_stage_2 = 15000

        ############### JUGADOR Y ###############
        if player.id_in_group == 2:

            if pay_contract: #Con contrato
                self.player.payment_stage_2 = 10000

            else: #Sin contrato
                if answers_total_stage_2_opponent >= Constants.mandatory_subtraction: #Si X cumple con la cantidad de restas
                    if not opponent_pay_second_quote: #Si decide no pagar la segunda cuota
                        self.player.payment_stage_2 = 22000
                    else: #Si decide pagar la segunda cuota
                        self.player.payment_stage_2 = 15000

                else:  #Si X no cumple con la cantidad de restas
                    if not opponent_pay_second_quote: #Si decide no pagar la segunda cuota
                        self.player.payment_stage_2 = -8000
                    else: #Si decide pagar la segunda cuota
                        self.player.payment_stage_2 = -15000
         
        payment_stage_1 = player_round1.payment_stage_1
        payment_stage_2 = self.player.payment_stage_2
        player_round1.payment_stage_2 = payment_stage_2
        combined_payoff_total = payment_stage_1 + payment_stage_2


        return {
            'payment_stage_1': payment_stage_1,
            'payment_stage_2': payment_stage_2,
            'combined_payoff_total' : math.trunc(combined_payoff_total),
            'contrato': contrato,
            'titulo': titulo,
            'opponent_contract_decision': opponent_contract_decision_label,
            'pay_contract': pay_contract_label,
            'answer_correct_stage_2': answer_correct_stage_2,
            'answer_correct_stage_2_opponent': answer_correct_stage_2_opponent,
            'answers_total_stage_2': answers_total_stage_2,
            'answers_total_stage_2_opponent': answers_total_stage_2_opponent
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
    form_fields = ['amount_inversion']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

#=======================================================================================================================

class HeadTails(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def live_method(self, data):
        player = self.in_round(1)
        player.flip_value = float(data)
        self.flip_value = float(data)

    def vars_for_template(self):
        amount_inversion = math.trunc(c(self.player.amount_inversion))
        return {
            'amount_inversion' : amount_inversion
        }
        
#=======================================================================================================================
class ResultsDoubleMoney(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        player = self.player.in_round(1)
        flip_value = self.player.flip_value 
        amount_inversion = math.trunc(c(self.player.amount_inversion))
        cara_sello_name = ""
        payment_stage_3 = 0

        if(flip_value <= 0.5):
            cara_sello_name = "rojo"
            payment_stage_3 = 5000-amount_inversion + math.trunc(amount_inversion*2)
        else:
            cara_sello_name = "azul"
            payment_stage_3 = 5000-amount_inversion

        player.payment_stage_3 = payment_stage_3

        return {
            'amount_inversion' : amount_inversion,
            'cara_sello_name' : cara_sello_name,
            'payment_stage_3' : payment_stage_3
        }
#=======================================================================================================================

class CombinedResults3(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        player = self.player.in_round(1)
        player.payment_total = player.payment_stage_1 + player.payment_stage_2 + player.payment_stage_3
        payment_total = player.payment_total
        return {
            'payment_stage_1' : player.payment_stage_1,
            'payment_stage_2' : player.payment_stage_2,
            'payment_stage_3' : player.payment_stage_3,
            'payment_total': payment_total
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
        'esta_laborando' ,
        'ingreso_mensual' ,
        'gasto_mensual' ,
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

    def before_next_page(self):
        player = self.player.in_round(1)
        list_atrr = self.form_fields
        get_and_set_data(self.player, player, list_atrr)

#=======================================================================================================================

class CombinedResults4(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        player = self.player.in_round(1)
        player.payment_total = player.payment_stage_1 + player.payment_stage_2 + player.payment_stage_3 + Constants.fixed_payment
        payment_total = player.payment_total
        return {
            'payment_stage_1' : player.payment_stage_1,
            'payment_stage_2' : player.payment_stage_2,
            'payment_stage_3' : player.payment_stage_3,
            'payment_total': payment_total
        }

#=======================================================================================================================

class ReminderNequi(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        player = self.player.in_round(1)
        num_temporal = player.num_temporal
        payment_total = player.payment_total
        
        return {
            'payment_total': payment_total,
            'num_temporal': num_temporal
        }

# ******************************************************************************************************************** #
# *** MANAGEMENT STAGE
# ******************************************************************************************************************** #
stage_1_sequence = [Consent, GenInstructions, Stage1Instructions, Stage1Questions, Start, AddNumbers, ResultsWaitPage, PartialResults, CombinedResults]
stage_2_sequence = [Stage2Instructions, Stage2Instructions2, Stage2Instructions3, Stage2Instructions4, Stage2Instructions5, RoleAssignment, Decision, ResultsWaitPage3, Decision2, Start2, AddNumbers2, ResultsWaitPage2, SecondQuoteY, WaitPageX, SecondQuoteX, CombinedResults2]
#stage_2_sequence = [RoleAssignment, Decision, ResultsWaitPage3, Decision2, Start2, AddNumbers2, ResultsWaitPage2, SecondQuoteY, WaitPageX, SecondQuoteX, CombinedResults2]
stage_3_sequence = [PlayCoin, DoubleMoney, HeadTails, ResultsDoubleMoney, CombinedResults3, SocioDemSurvey, CombinedResults4, ReminderNequi]

page_sequence = stage_1_sequence + stage_2_sequence + stage_3_sequence
