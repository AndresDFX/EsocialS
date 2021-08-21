from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random, math

class AddNumbers(Page):
    #Falta algoritmo de asignación de equipos
    form_model = 'player'
    form_fields = ['number_entered']
    timer_text = 'Tiempo restante para completar la Etapa 1:'

    def before_next_page(self):
        #Here's where the payoff is calculated
        self.player.total_sums = 1            
        if self.player.sum_of_numbers == self.player.number_entered:
            self.player.payoff = Constants.payment_per_correct_answer
            self.player.correct_answers = 1
        else:
            self.player.wrong_sums = 1    
        return

    def get_timeout_seconds(self):
        import time
        #Timeout variable used to show the timer
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        #Luego de que se acaba el tiempo, se salta las rondas (no las muestra) y va automáticamente a la siguiente página (Pagos).
        if self.round_number <= Constants.num_rounds/2:
            return self.get_timeout_seconds() > 3

    def vars_for_template(self):
        number_1 = random.randint(1,100)
        number_2 = random.randint(1,100)
        correct_answers = 0
        combined_payoff = 0
        combined_payoff_others = 0
        wrong_sums = 0
        total_sums = 0
        self.player.sum_of_numbers = number_1 + number_2
        all_players = self.player.in_all_rounds()
        me = self.player.id_in_group
        me_in_session = self.player.participant.id_in_session
        #opponent = self.player.other_player().id_in_group #self.player.get_others_in_group()[0].id_in_group
        others = self.player.get_others_in_group()[0] #Como es un juego de dos jugadres, devuelve al oponente. Nótese que "Oponente" es sólamente el id del otro jugador en el grupo
        opponent = self.player.other_player()
        correct_answers_opponent = 0
        opponent_id = self.player.other_player().id_in_group
        opponent_id_in_session = self.player.other_player().participant.id_in_session
        numero_aux = self.player.num_min_stage_1
        contador_numero_aux = 1
        round_label = 0
        # print("Matriz Ronda 1" + str(self.subsession.get_group_matrix()))
        # Matriz del grupo: 
        # [[<Player  1>, <Player  2>], 
        # [<Player  3>, <Player  4>]]
        # Yo: 1
        # Yo en la sesión: 1
        # Oponente: 2 
        # all_players: Jugadores en todas las rondas. O sea yo, en mi ronda.
        # Others: Otros jugadores (distintos a mí) en el grupo. 
        # print("Yo " + str(me))
        # print("Yo en la sesión " + str(me_in_session))
        # print("Oponente " + str(opponent))
        # print("All players: " + str(all_players))
        # print("Others: " + str(others))
        # print("Epa: " + str(self.player.get_others_in_subsession()))
        # self.player.contador_numero_aux = 1
        # Lo de del timeout hay que hacerlo dimacamente, tomando el evento y actialuzando la pagina    
        for player in all_players:
            #Calculating the payoff for each player
            combined_payoff += player.payoff
            correct_answers += player.correct_answers
            wrong_sums += player.wrong_sums
            total_sums += player.total_sums
        return {
            'number_1': number_1,
            'number_2': number_2,
            'combined_payoff' : math.trunc(combined_payoff),
            'correct_answers': correct_answers,
            'round_number' : self.round_number,
            'opponent_id': opponent_id,
            'wrong_sums': wrong_sums,
            'total_sums': total_sums,
            'round_label': round_label,
            'opponent_id_in_session': opponent_id_in_session
        }

class AddNumbers2(Page):
    # Works in similar way as the previous class 
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
        return

    def get_timeout_seconds(self):
        import time
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        #Luego de que se acaba el tiempo, se salta las rondas (no las muestra) y va automáticamente a la siguiente página (Pagos).
        if self.round_number >= (Constants.num_rounds/2)+1:
            return self.get_timeout_seconds() > 3    

    def vars_for_template(self):
        number_1 = random.randint(1,100)
        number_2 = random.randint(1,100)
        correct_answers = 0
        combined_payoff = 0
        combined_payoff_others = 0
        wrong_sums_2 = 0
        total_sums_2 = 0
        self.player.sum_of_numbers_2 = number_1 + number_2
        all_players = self.player.in_all_rounds()
        me = self.player.id_in_group
        me_in_session = self.player.participant.id_in_session
        #opponent = self.player.other_player().id_in_group #self.player.get_others_in_group()[0].id_in_group
        others = self.player.get_others_in_group()[0] #Como es un juego de dos jugadres, devuelve al oponente. Nótese que "Oponente" es sólamente el id del otro jugador en el grupo
        opponent = self.player.other_player()
        opponent_id = self.player.other_player().id_in_group
        opponent_contract_decision = opponent.pay_contract
        opponent_suggested_sums = opponent.suggested_sums
        opponent_id_in_session = self.player.other_player().participant.id_in_session
        # Matriz del grupo: 
        # [[<Player  1>, <Player  2>], 
        # [<Player  3>, <Player  4>]]
        # Yo: 1
        # Yo en la sesión: 1
        # Oponente: 2 
        # all_players: Jugadores en todas las rondas. O sea yo, en mi ronda.
        # Others: Otros jugadores (distintos a mí) en el grupo. 
        # print("Yo " + str(me))
        # print("Yo en la sesión " + str(me_in_session))
        # print("Oponente " + str(opponent))
        # print("All players: " + str(all_players))
        # print("Others: " + str(others))
        # print("Epa: " + str(self.player.get_others_in_subsession()))
        for player in all_players:
            combined_payoff += player.pago
            correct_answers += player.correct_answers_2
            wrong_sums_2 += player.wrong_sums_2
            total_sums_2 += player.total_sums_2
        
        pay_contract = self.player.in_round((Constants.num_rounds/2)+1).pay_contract
        opponent_contract_decision = self.player.other_player().in_round((Constants.num_rounds/2)+1).pay_contract
        # print(me)
        # print(opponent_id)
        # print(opponent_contract_decision)
        # print(pay_contract)
        # print("Matriz Ronda 3" + str(self.subsession.get_group_matrix()))
        # print("Pago ronda 1" + str(self.player.payment_stage_1))
        return {
            'number_1': number_1,
            'number_2': number_2,
            'combined_payoff' : math.trunc(combined_payoff),
            'correct_answers': correct_answers,
            'round_number' : self.round_number,
            'opponent_id': opponent_id,
            'wrong_sums': wrong_sums_2,
            'total_sums': total_sums_2,
            'opponent_contract_decision': opponent_contract_decision,
            'opponent_id_in_session': opponent_id_in_session
        }

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
        combined_payoff_others = 0
        wrong_sums_2 = 0
        total_sums_2 = 0
        wrong_sums_2_opponent = 0
        total_sums_2_opponent = 0
        me = self.player.id_in_group
        titulo = ""
        opponent_suggested_sums = opponent.in_round((Constants.num_rounds/2)+1).suggested_sums
        contrato = 0
        pay_contract = self.player.in_round((Constants.num_rounds/2)+1).pay_contract
        pay_contract_label = ""
        opponent_contract_decision = opponent.in_round((Constants.num_rounds/2)+1).pay_contract
        opponent_contract_decision_label = ""
        if me == 1:
            titulo = "Pagos Etapa 2 - Jugador X"
        else:
            titulo = "Pagos Etapa 2 - Jugador Y"
        # print("Yo " + str(me))
        # print("Oponente " + str(opponent_id))
        # print("Other " + str(others))
        # print("All Others " + str(all_others))
        # print("Group players" + str(self.group.get_players()))
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


        #Jugador X sin contrato
        if player.id_in_group == 1 and opponent_contract_decision == False:
            # print("11" + "Ba") 
            self.player.payment_stage_2 = 2500 - (20 * total_sums_2 )
            contrato = 0

         #Jugador Y sin contrato
        if player.id_in_group == 2 and pay_contract == False:
            self.player.payment_stage_2 = -2500 + (100 * correct_answers_opponent )
            # print("22" + "Be")
            contrato = 0

        #Jugador X cumple con sumas
        if player.id_in_group == 1 and opponent_contract_decision == True:
            if correct_answers >= Constants.sumas_obligatorias_contrato:
                # print(33) 
                self.player.payment_stage_2 = 2500 - (20 * total_sums_2 )
                contrato = 2500
        
        #Jugador X no cumple con sumas
        if player.id_in_group == 1 and opponent_contract_decision == True:
            if correct_answers < Constants.sumas_obligatorias_contrato: 
                # print(44)
                self.player.payment_stage_2 = -2500
                contrato = 2500
        
        #Y: Jugador X cumple con sumas
        if player.id_in_group == 2 and pay_contract == True:
            if correct_answers_opponent >= Constants.sumas_obligatorias_contrato: 
                # print(55)
                self.player.payment_stage_2 = -5000 + (100 * correct_answers_opponent )
                contrato = 2500

        #Y: Jugador X no cumple con sumas
        if player.id_in_group == 2 and pay_contract == True:
            if correct_answers_opponent < Constants.sumas_obligatorias_contrato: 
                # print(66)
                self.player.payment_stage_2 = 0
                contrato = 2500

        # print("Jugador "+ str(player.id_in_group) + ". Contrato Op "+ str(opponent_contract_decision))
        # print("Jugador "+ str(player.id_in_group) + ". Contrato Jug "+ str(pay_contract))
        #self.player.payment_stage_1 = math.trunc(combined_payoff) + Constants.fixed_payment
        combined_payoff_total = self.player.payment_stage_2 + self.player.in_round(Constants.num_rounds/2).payment_stage_1
        return {
            'payment_stage_1': self.player.in_round(Constants.num_rounds/2).payment_stage_1,
            'payment_stage_2': self.player.payment_stage_2,
            'combined_payoff_total' : math.trunc(combined_payoff_total),
            'contrato': contrato,
            'titulo': titulo,
            'opponent_contract_decision': opponent_contract_decision_label,
            'pay_contract': pay_contract_label,
            'correct_answers': correct_answers,
            'correct_answers_opponent': correct_answers_opponent,
            'total_sums_2': total_sums_2,
            'total_sums_2_opponent': total_sums_2_opponent
        }

class GenInstructions(Page):
    def is_displayed(self):
        return self.round_number == 1

class Stage1Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1

class Stage1Questions(Page):
    form_model = 'player'
    form_fields = ['control_question_1', 'control_question_2']
    def is_displayed(self):
        return self.round_number == 1

class Stage2Instructions(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds/2        

class Stage2Questions(Page):
    form_model = 'player'
    form_fields = ['control_question_3', 'control_question_4', 'control_question_5', 'control_question_6', 'control_question_7']
    def is_displayed(self):
        return self.round_number == Constants.num_rounds/2        

class Start(Page):
    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        import time
        self.participant.vars['expiry'] = time.time() + Constants.num_min_stage_1*60

class Start2(Page):
    def is_displayed(self):
        return self.round_number == (Constants.num_rounds/2)+1   

    def before_next_page(self):
        import time
        self.participant.vars['expiry'] = time.time() + Constants.num_min_stage_2*60        

class Consent(Page):
    form_model = 'player'
    form_fields = ['accepts_data', 'num_temporal', 'accepts_terms']

    def is_displayed(self):
        # print(self.player.cara_sello_value)
        return self.round_number == 1

class ResultsWaitPage(WaitPage):
    #Muestra el WaitPage al final de la cuarta ronda. Antes del pago
    def is_displayed(self):
        # print("Matriz Ronda 2" + str(self.subsession.get_group_matrix()))
        return self.round_number == Constants.num_rounds/2

class ResultsWaitPage2(WaitPage):
    #Muestra el WaitPage al final de todo. Antes del pago
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

class ResultsWaitPage3(WaitPage):
    #Muestra el WaitPage al final de la cuarta ronda. Antes del pago
    def is_displayed(self):
        # print("Matriz Ronda 2" + str(self.subsession.get_group_matrix()))
        return self.round_number == (Constants.num_rounds/2)+1

class RoleAssignment(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.round_number == (Constants.num_rounds/2)+1

class Decision(Page):
    form_model = 'player'
    form_fields = ['pay_contract', 'believe_pay_contract', 'suggested_sums']
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

class Decision2(Page):
    form_model = 'player'
    form_fields = ['suggested_sums']
    def is_displayed(self):
        return self.round_number == (Constants.num_rounds/2)+1
    def vars_for_template(self):
        me = self.player.id_in_group
        opponent = self.player.other_player()
        opponent_contract_decision = opponent.pay_contract
        opponent_suggested_sums = opponent.suggested_sums
        titulo = ""
        if me == 1:
            titulo = "Reporte de decisión Jugador X"
        else:
            titulo = "Decision Jugador Y - Parte 2"
        return{
                'titulo': titulo,
                'opponent_contract_decision': opponent_contract_decision,
                'opponent_suggested_sums': opponent_suggested_sums
            }

class CombinedResults(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds/2

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
        # print("Yo " + str(me))
        # print("Oponente " + str(opponent_id))
        # print("Other " + str(others))
        # print("All Others " + str(all_others))
        # print("Group players" + str(self.group.get_players()))
        for player in all_players:
            combined_payoff += player.payoff
            correct_answers += player.correct_answers
            correct_answers_opponent += player.other_player().correct_answers
            combined_payoff_opponent += player.other_player().payoff

        correct_answers_team = correct_answers + correct_answers_opponent
        combined_payoff_team = combined_payoff + combined_payoff_opponent
        combined_payoff_total = combined_payoff_team
        #Si es T-T o T-NT el pago en la etapa uno es el pago del equipo más el pago fijo
        self.player.payment_stage_1 = math.trunc(combined_payoff_total)
        # print("Jugador "+ str(player.id_in_group) + ". Pago total "+ str(self.player.payment_stage_1))
        return {
            'combined_payoff' : math.trunc(combined_payoff),
            'combined_payoff_opponent': math.trunc(combined_payoff_opponent),
            'correct_answers': correct_answers,
            'correct_answers_opponent': correct_answers_opponent,
            'round_number' : self.round_number,
            'opponent_id': opponent_id,
            'correct_answers_team': correct_answers_team,
            'combined_payoff_team': math.trunc(combined_payoff_team),
            'combined_payoff_total': self.player.payment_stage_1
        }

class PlayCoin(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

class DoubleMoney(Page):
    form_model = 'player' #Le dice que es un jugador
    form_fields = ['monto']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

class HeadTails(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.round_number == Constants.num_rounds       

class ResultsDoubleMoney(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    #form_model = 'player' #Le dice que es un jugador
    #form_fields = ['monto', 'combined_payoff', 'inversion', 'cara_sello_payoff' ]
    def vars_for_template(self):
        #all_players = self.player.in_all_rounds()
        cara_sello_name = ""
        combined_payoff = 0
        cara_sello_payof = 0
        inversion = math.trunc(c(self.player.monto))
        # print(self.player.cara_sello_value)
        if(self.player.cara_sello_value <= 0.5):
            cara_sello_name = "Cara"
            self.player.monto = 5000-inversion + math.trunc(self.player.monto*2)
        else:
            cara_sello_name = "Sello"
            self.player.monto = 5000-inversion + 0
        # print(cara_sello_name)
        #combined_payoff = math.trunc(self.player.payoff) + cara_sello_payoff
        return {
            #'combined_payoff' : combined_payoff,
            'inversion' : inversion,
            'cara_sello_name' : cara_sello_name,
            'cara_sello_payoff' : self.player.monto
        }

class CombinedResults3(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        ganancias_acumuladas = self.player.in_round(Constants.num_rounds/2).payment_stage_1 + self.player.payment_stage_2 + self.player.monto
        return {
            'payment_stage_1' : self.player.in_round(Constants.num_rounds/2).payment_stage_1,
            'payment_stage_2' : self.player.payment_stage_2,
            'payment_stage_3' : self.player.monto,
            'ganancias_acumuladas': ganancias_acumuladas
        }

class CombinedResults4(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        ganancias_acumuladas = self.player.in_round(Constants.num_rounds/2).payment_stage_1 + self.player.payment_stage_2 + self.player.monto + 5000
        return {
            'payment_stage_1' : self.player.in_round(Constants.num_rounds/2).payment_stage_1,
            'payment_stage_2' : self.player.payment_stage_2,
            'payment_stage_3' : self.player.monto,
            'ganancias_acumuladas': ganancias_acumuladas
        }

class SocioDemSurvey(Page):
    form_model = 'player'
    form_fields = ['genero', 'edad', 'ciudad', 'estrato', 'estado_civil', 'numero_hijos', 'identifica_cultura',
    'identifica_religion','nivel_estudios', 'tendencia_politica', 'disposicion_riesgos', 'conseguir_esfuerzo',
    'planes_termino', 'juego_suerte', 'propongo_aprender', 'mayores_logros', 'establecer_metas', 'competencia_excelencia',
    'salir_adelante', 'comparar_calificaciones', 'empeno_trabajo', 'alcanzar_objetivos', 'cumplir_tareas', 'obtener_resultados',
    'exito_esfuerzo','superar_desafios', 'confianza_tareas', 'tareas_excelencia', 'tareas_dificiles', 'alcanzar_objetivos',
    'tarde_cita', 'comprar_vendedores_ambulantes', 'trabajar_sin_contrato', 'emplear_sin_contrato', 'no_cotizar_pension', 'no_cotizar_salud',
    'no_cuenta_bancaria', 'pedir_prestado', 'transporte_alternativo', 'vender_informal', 'no_votar', 'comprar_sin_factura',
    'tarde_cita_otros', 'comprar_vendedores_ambulantes_otros', 'trabajar_sin_contrato_otros', 'emplear_sin_contrato_otros', 'no_cotizar_pension_otros', 'no_cotizar_salud_otros',
    'no_cuenta_bancaria_otros', 'pedir_prestado_otros', 'transporte_alternativo_otros', 'vender_informal_otros', 'no_votar_otros', 'comprar_sin_factura_otros',
    'tarde_cita_apropiado', 'comprar_vendedores_ambulantes_apropiado', 'trabajar_sin_contrato_apropiado', 'emplear_sin_contrato_apropiado', 'no_cotizar_pension_apropiado', 'no_cotizar_salud_apropiado',
    'no_cuenta_bancaria_apropiado', 'pedir_prestado_apropiado', 'transporte_alternativo_apropiado', 'vender_informal_apropiado', 'no_votar_apropiado', 'comprar_sin_factura_apropiado'
    ]

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

class ReminderNequi(Page):
    form_model = 'player'
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        num_temporal = self.player.in_round(1).num_temporal
        ganancias_acumuladas = self.player.in_round(Constants.num_rounds/2).payment_stage_1 + self.player.payment_stage_2 + self.player.monto + 5000
        return {
            'ganancias_acumuladas': ganancias_acumuladas,
            'num_temporal': num_temporal
        }

    

page_sequence = [Consent, GenInstructions,Stage1Instructions, Stage1Questions, Start, AddNumbers, ResultsWaitPage,  CombinedResults, Stage2Instructions, Stage2Questions, RoleAssignment, Decision,ResultsWaitPage3, Decision2, Start2, AddNumbers2, ResultsWaitPage2, CombinedResults2,PlayCoin,DoubleMoney,HeadTails,ResultsDoubleMoney, CombinedResults3, SocioDemSurvey, CombinedResults4, ReminderNequi]
# page_sequence = [Start, AddNumbers, ResultsWaitPage, CombinedResults, RoleAssignment, Decision, ResultsWaitPage3, Decision2, Start2, AddNumbers2, ResultsWaitPage2, CombinedResults2, PlayCoin,DoubleMoney,HeadTails,ResultsDoubleMoney, CombinedResults3,SocioDemSurvey, CombinedResults4, ReminderNequi]
# page_sequence = [Start, AddNumbers, ResultsWaitPage, CombinedResults]

