from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import math


# variables for all templates
# --------------------------------------------------------------------------------------------------------------------
def vars_for_all_templates(self):
    return {
        'lottery_a_lo': c(Constants.lottery_a_lo),
        'lottery_a_hi': c(Constants.lottery_a_hi),
        'lottery_b_lo': c(Constants.lottery_b_lo),
        'lottery_b_hi': c(Constants.lottery_b_hi)
    }


# ******************************************************************************************************************** #
# *** CLASS INSTRUCTIONS *** #
# ******************************************************************************************************************** #
class Instructions(Page):

    # only display instruction in round 1
    # ----------------------------------------------------------------------------------------------------------------
    def is_displayed(self):
        return self.subsession.round_number == 1

    # variables for template
    # ----------------------------------------------------------------------------------------------------------------
    def vars_for_template(self):
        return {
            'num_choices':  len(self.participant.vars['mpl_choices'])
        }


# ******************************************************************************************************************** #
# *** PAGE DECISION *** #
# ******************************************************************************************************************** #
class Decision(Page):

    # form model
    # ----------------------------------------------------------------------------------------------------------------
    form_model = 'player'

    # form fields
    # ----------------------------------------------------------------------------------------------------------------
    def get_form_fields(self):

        # unzip list of form_fields from <mpl_choices> list
        form_fields = [list(t) for t in zip(*self.participant.vars['mpl_choices'])][1]
        #form_fields = ['choice_1', 'choice_2', 'choice_3', 'choice_4', 'choice_5', 'choice_6', 'choice_7', 'choice_8', 'choice_9', 'choice_10', 'choice_11']
        # provide form field associated with pagination or full list
        if Constants.one_choice_per_page:
            page = self.subsession.round_number
            return [form_fields[page - 1]]
            # [form_fields[page - 1]] = Each choice ['choice_1'] ... ['choice_11']
        else:
            return form_fields

    # variables for template
    # ----------------------------------------------------------------------------------------------------------------
    def vars_for_template(self):

        # specify info for progress bar
        total = len(self.participant.vars['mpl_choices'])
        page = self.subsession.round_number #Page number
        progress = page / total * 100

        if Constants.one_choice_per_page:
            return {
                'page':      page,
                'total':     total,
                'progress':  progress,
                'choices':   [self.player.participant.vars['mpl_choices'][page - 1]]
                #'choices': Each choice ['choice_1'] ... ['choice_11']
            }
        else:
            #print("Choices"+ str(self.player.participant.vars['mpl_choices']))
            return {
                'choices':   self.player.participant.vars['mpl_choices']
                #'choices': Choices[(1, 'choice_1', '0/10'), (2, 'choice_2', '1/10'), (3, 'choice_3', '2/10'), (4, 'choice_4', '3/10'), (5, 'choice_5', '4/10'), (6, 'choice_6', '5/10'), (7, 'choice_7', '6/10'), (8, 'choice_8', '7/10'), (9, 'choice_9', '8/10'), (10, 'choice_10', '9/10'), (11, 'choice_11', '10/10')]
            }

    # set player's payoff
    # ----------------------------------------------------------------------------------------------------------------
    def before_next_page(self):

        # unzip indices and form fields from <mpl_choices> list
        round_number = self.subsession.round_number
        form_fields = [list(t) for t in zip(*self.participant.vars['mpl_choices'])][1]
        indices = [list(t) for t in zip(*self.participant.vars['mpl_choices'])][0]
        print("Indices" + str(indices))
        index = indices[round_number - 1]
        print("Index" + str(index))
        # if choices are displayed sequentially
        # ------------------------------------------------------------------------------------------------------------
        if Constants.one_choice_per_page:
            print("Que hay ahi" + str(form_fields[round_number-1]))
            # replace current choice in <choices_made>
            current_choice = getattr(self.player, form_fields[round_number - 1])
            print("Current choice " + str(current_choice))
            self.participant.vars['mpl_choices_made'][index - 1] = current_choice
            print("Choices Pages index - 1" + self.participant.vars['mpl_choices_made'][index - 1])
            # if current choice equals index to pay ...
            if index == self.player.participant.vars['mpl_index_to_pay']:
                # set payoff
                self.player.set_payoffs()

            # after final choice
            if round_number == Constants.num_choices:
                # determine consistency
                self.player.set_consistency()
                # set switching row
                self.player.set_switching_row()

        # if choices are displayed in tabular format
        # ------------------------------------------------------------------------------------------------------------
        if not Constants.one_choice_per_page:

            # replace choices in <choices_made>
            for j, choice in zip(indices, form_fields):
                choice_i = getattr(self.player, choice)
                self.participant.vars['mpl_choices_made'][j - 1] = choice_i

            # set payoff
            self.player.set_payoffs()
            # determine consistency
            self.player.set_consistency()
            # set switching row
            self.player.set_switching_row()


# ******************************************************************************************************************** #
# *** PAGE RESULTS *** #
# ******************************************************************************************************************** #
class Results(Page):

    # skip results until last page
    # ----------------------------------------------------------------------------------------------------------------
    def is_displayed(self):
        if Constants.one_choice_per_page:
            return self.subsession.round_number == Constants.num_rounds
        else:
            return True

    # variables for template
    # ----------------------------------------------------------------------------------------------------------------
    def vars_for_template(self):

        # unzip <mpl_choices> into list of lists
        choices = [list(t) for t in zip(*self.participant.vars['mpl_choices'])]
        indices = choices[0]
        # get index, round, and choice to pay
        index_to_pay = self.player.participant.vars['mpl_index_to_pay']
        round_to_pay = indices.index(index_to_pay) + 1
        choice_to_pay = self.participant.vars['mpl_choices'][round_to_pay - 1]
        decision = choice_to_pay[0]

        if Constants.one_choice_per_page:
            return {
                'choice_to_pay':  [choice_to_pay],
                'option_to_pay':  self.player.in_round(round_to_pay).option_to_pay,
                'payoff':         self.player.in_round(round_to_pay).payoff,
                'decision':       decision
            }
        else:
            return {
                'choice_to_pay':  [choice_to_pay],
                'option_to_pay':  self.player.option_to_pay,
                'payoff':         math.trunc(self.player.payoff),
                'decision':       decision,
                'pelota':         self.player.ball
            }
class Results2(Page):

    # skip results until last page
    # ----------------------------------------------------------------------------------------------------------------
    def is_displayed(self):
        if Constants.one_choice_per_page:
            return self.subsession.round_number == Constants.num_rounds
        else:
            return True

    # variables for template
    # ----------------------------------------------------------------------------------------------------------------
    def vars_for_template(self):

        # unzip <mpl_choices> into list of lists
        choices = [list(t) for t in zip(*self.participant.vars['mpl_choices'])]
        indices = choices[0]
        # get index, round, and choice to pay
        index_to_pay = self.player.participant.vars['mpl_index_to_pay']
        round_to_pay = indices.index(index_to_pay) + 1
        choice_to_pay = self.participant.vars['mpl_choices'][round_to_pay - 1]
        decision = choice_to_pay[0]

        if Constants.one_choice_per_page:
            return {
                'choice_to_pay':  [choice_to_pay],
                'option_to_pay':  self.player.in_round(round_to_pay).option_to_pay,
                'payoff':         self.player.in_round(round_to_pay).payoff,
                'decision':       decision
            }
        else:
            return {
                'choice_to_pay':  [choice_to_pay],
                'option_to_pay':  self.player.option_to_pay,
                'payoff':         math.trunc(self.player.payoff),
                'decision':       decision,
                'pelota':         self.player.ball
            }
class Results3(Page):

    # skip results until last page
    # ----------------------------------------------------------------------------------------------------------------
    def is_displayed(self):
        if Constants.one_choice_per_page:
            return self.subsession.round_number == Constants.num_rounds
        else:
            return True

    # variables for template
    # ----------------------------------------------------------------------------------------------------------------
    def vars_for_template(self):

        # unzip <mpl_choices> into list of lists
        choices = [list(t) for t in zip(*self.participant.vars['mpl_choices'])]
        indices = choices[0]
        # get index, round, and choice to pay
        index_to_pay = self.player.participant.vars['mpl_index_to_pay']
        round_to_pay = indices.index(index_to_pay) + 1
        choice_to_pay = self.participant.vars['mpl_choices'][round_to_pay - 1]
        decision = choice_to_pay[0]

        if Constants.one_choice_per_page:
            return {
                'choice_to_pay':  [choice_to_pay],
                'option_to_pay':  self.player.in_round(round_to_pay).option_to_pay,
                'payoff':         self.player.in_round(round_to_pay).payoff,
                'decision':       decision
            }
        else:
            return {
                'choice_to_pay':  [choice_to_pay],
                'option_to_pay':  self.player.option_to_pay,
                'payoff':         math.trunc(self.player.payoff),
                'decision':       decision,
                'pelota':         self.player.ball
            }     

class Consent(Page):
    form_model = 'player' #Le dice que es un jugador
    form_fields = ['num_temporal','accepts_terms']

class DoubleMoney(Page):
    form_model = 'player' #Le dice que es un jugador
    form_fields = ['monto']

class ResultsDoubleMoney(Page):
    #form_model = 'player' #Le dice que es un jugador
    #form_fields = ['monto', 'combined_payoff', 'inversion', 'cara_sello_payoff' ]
    def vars_for_template(self):
        #all_players = self.player.in_all_rounds()
        cara_sello_name = ""
        combined_payoff = 0
        cara_sello_payof = 0
        inversion = math.trunc(c(self.player.monto))
        #Here is where the payoff is calculated. With head (Cara) you double your initial bet. Tails (Sello) makes you lose money 
        if(Constants.cara_sello_value == 0):
            cara_sello_name = "Cara"
            self.player.monto = 10000-inversion + math.trunc(self.player.monto*2) 
        else:
            cara_sello_name = "Sello"
            self.player.monto = 10000-inversion + 0
        # print(cara_sello_name)
        #combined_payoff = math.trunc(self.player.payoff) + cara_sello_payoff
        return {
            #'combined_payoff' : combined_payoff,
            'inversion' : inversion,
            'cara_sello_name' : cara_sello_name,
            'cara_sello_payoff' : self.player.monto
        }
class CombinedResults(Page):
    def vars_for_template(self):
        #Calculating the player's combinded payoff based on their actual payoff and the gambled amount 
        combined_payoff = math.trunc(self.player.payoff) + self.player.monto
        return {
            'combined_payoff' : combined_payoff,
        }

class TotalPayoff(Page):
    form_model = 'player'
    def vars_for_template(self):
        self.player.set_total_payoff()
        return {
            'total_payoff' : self.player.pago_total,
        }       
        
class Priming(Page):
    form_model = 'player' #Le dice que es un jugador
    form_fields = ['nombre_entidad', 'tiempo_entidad', 'tipo_contrato', 'horas_semanales', 'rango_pago', 'satisfecho_trabajo_actual',
    'satisfecho_beneficios', 'satisfecho_jornada', 'conforme_contrato', 'empleo_estable', 'contrato_credito_vivienda','contrato_credito_carro' ,

    'recibe_prima' , 'recibe_cesantias', 'recibe_vacaciones_sueldo','aporte_pension' , 'aporte_ahorro', 'aporte_inversiones', 'aporte_seguro',
    'aporte_hijos_vejez', 'aporte_otro', 'aporte_nada',

    'cambiar_empresa' , 'cambiar_trabajo', 'mejorar_capacidades', 'mejorar_ingresos', 'trabajar_menos', 
    'trabajo_temporal', 'trabajo_estable', 'crecimiento_profesional', 'dinero_compra_vivienda', 'contrato_compra_vivienda', 'problemas_companeros',
    'problemas_jefe', 'labor_desempenada', 'esfuerzo_fisico', 'problemas_ambientales', 'otro_problema' ]     

class Tips(Page):
    form_model = 'player'
    form_fields = ['pregunta_uno', 'pregunta_dos','pregunta_tres', 'pregunta_cuatro', 'pregunta_cinco','pregunta_seis', 'pregunta_siete' ]

class ResultsTips(Page):
    def vars_for_template(self):
        pago = 20000
        return {
            'payoff' : pago,
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

class ReminderNequi(Page):
    form_model = 'player'

class HeadTails(Page):
    form_model = 'player'

class PlayCoin(Page):
    form_model = 'player'            
# ******************************************************************************************************************** #
# *** PAGE SEQUENCE *** #Usted obtuvo invertió {{inversion }}y obtuvo {{cara_sello}} 
# por lo que su pago en esta activdad es de {{cara_sello_payoff}} y su pago total es {{combined_payoff}}
# ******************************************************************************************************************** #
# page_sequence = [HeadTails, Instructions, Decision, Results,Tips,ResultsTips, DoubleMoney,HeadTails,ResultsDoubleMoney, Instructions, Decision, Results, CombinedResults, TotalPayoff]
page_sequence = [Consent,Priming,Tips,ResultsTips, PlayCoin, DoubleMoney,HeadTails,ResultsDoubleMoney, Instructions, Decision, Results3, Results2, Results , CombinedResults, TotalPayoff, SocioDemSurvey, ReminderNequi, TotalPayoff]
# if Constants.instructions:
#     page_sequence.insert(0, Instructions)

# if Constants.results:
#     page_sequence.append(Results)
