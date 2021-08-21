from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
# Trabajar con fechas utilizando Python haremos uso de la librería datetime
from datetime import datetime, date, timedelta
import pytz
#
import difflib
from difflib import Differ

import math

class ConsentimientoInformado(Page):

    live_method = 'live_treatment'

    def is_displayed(self):
        print(self.participant.vars['contrato'])
        
        zona_horaria = datetime.now(pytz.timezone('America/Bogota'))
        fecha_actual = zona_horaria.date()
        print(fecha_actual)
        return self.round_number == 1 

    def before_next_page(self):
        self.player.get_time()
        print('======================')
        print(self.player.start_date)
        print(self.player.next_date)
        print(self.player.date_after_next)
        print('======================')
        
    form_model = 'player'
    form_fields = ['consentimiento','sexo','estrato']


class Instrucciones(Page):

   # live_method = 'live_treatment' 

    def is_displayed(self):
        print("============================")
        print(self.player.in_round(1).treatment)
        print("============================")
        return self.round_number == 2

    def vars_for_template(self):
        print(self.session.vars['treatments'])
        # self.player.set_treatment()
        # print(self.player.treatment)
       

    # form_model = 'player'
    # form_fields = ['sexo','estrato']


class Contrato_formal_fijo(Page):
    def is_displayed(self):
        # self.player.in_round(self.round_number - 1).payoff
        return self.player.in_round(1).treatment == Constants.contrato_formal_fijo and self.round_number == 2
        # return self.participant.vars['contrato'] == Constants.contrato_formal_fijo and self.round_number == 2

    form_model = 'player'
    form_fields = ['terminos_actividad']


class Contrato_formal_indefinido(Page):
    def is_displayed(self):
        return self.player.in_round(1).treatment == Constants.contrato_formal_indefinido and self.round_number == 2
        # return self.participant.vars['contrato'] == Constants.contrato_formal_indefinido and self.round_number == 2

    form_model = 'player'
    form_fields = ['terminos_actividad']


class Contrato_formal_servicios(Page):
    def is_displayed(self):
        return self.player.in_round(1).treatment == Constants.contrato_formal_servicios and self.round_number == 2
        # return self.participant.vars['contrato'] == Constants.contrato_formal_servicios and self.round_number == 2

    form_model = 'player'
    form_fields = ['terminos_actividad']


class Contrato_informal_fijo(Page):
    def is_displayed(self):
        return self.player.in_round(1).treatment == Constants.contrato_informal_fijo and self.round_number == 2
        # return self.participant.vars['contrato'] == Constants.contrato_informal_fijo and self.round_number == 2

    form_model = 'player'
    form_fields = ['terminos_actividad']


class Contrato_informal_indefinido(Page):
    def is_displayed(self):
        return self.player.in_round(1).treatment == Constants.contrato_informal_indefinido and self.round_number == 2
        # return self.participant.vars['contrato'] == Constants.contrato_informal_indefinido and self.round_number == 2
    
    form_model = 'player'
    form_fields = ['terminos_actividad']


class Contrato_informal_servicios(Page):
    def is_displayed(self):
        return self.player.in_round(1).treatment == Constants.contrato_informal_servicios and self.round_number == 2
        # return self.participant.vars['contrato'] == Constants.contrato_informal_servicios and self.round_number == 2

    form_model = 'player'
    form_fields = ['terminos_actividad']


class Identificacion(Page):
    def is_displayed(self):
        return self.round_number == 3

    form_model = 'player'
    form_fields = ['codigo', 'confirmacion_codigo']

    def error_message(self, values):
        print('values is', values)
        if values['codigo'] != values['confirmacion_codigo']:
            return 'El código y la verificación del código no coinciden'


class Ronda_1(Page):

    timeout_seconds = 300

    def is_displayed(self):
        return self.round_number > 2 and self.round_number < Constants.num_rounds

    def vars_for_template(self):

        titulo = ''
        texto = ''

        if self.round_number >= 3 and self.round_number <= 6:
            titulo = 'Mercados de energía' 
        if self.round_number >= 7 and self.round_number <= 10:
            titulo = 'Ecoturismo'
        if self.round_number >= 11 and self.round_number <= 14:
            titulo = 'Espacio'

        if self.round_number == 3:
            texto = Constants.texto1 
        if self.round_number == 4:
            texto = Constants.texto2
        if self.round_number == 5:
            texto = Constants.texto3
        if self.round_number == 6:
            texto = Constants.texto4
        if self.round_number == 7:
            texto = Constants.texto5
        if self.round_number == 8:
            texto = Constants.texto6
        if self.round_number == 9:
            texto = Constants.texto7
        if self.round_number == 10:
            texto = Constants.texto8
        if self.round_number == 11:
            texto = Constants.texto9
        if self.round_number == 12:
            texto = Constants.texto10
        if self.round_number == 13:
            texto = Constants.texto11
        if self.round_number == 14:
            texto = Constants.texto12

        return {
            "titulo": titulo,
            "texto": texto,
            "ronda": self.round_number - 2,
           
            "image_path" : 'imagenes\image{}.png'.format(self.round_number-2)
        }

    def before_next_page(self):
        if self.round_number == 3:
            c1 = Constants.texto1
            print(c1)
            c2 = self.player.texto_digitado1
        if self.round_number == 4:
            c1 = Constants.texto2
            print(c1)
            c2 = self.player.texto_digitado2
        if self.round_number == 5:
            c1 = Constants.texto3
            print(c1)
            c2 = self.player.texto_digitado3
        if self.round_number == 6:
            c1 = Constants.texto4
            print(c1)
            c2 = self.player.texto_digitado4
        if self.round_number == 7:
            c1 = Constants.texto5
            print(c1)
            c2 = self.player.texto_digitado5
        if self.round_number == 8:
            c1 = Constants.texto6
            print(c1)
            c2 = self.player.texto_digitado6
        if self.round_number == 9:
            c1 = Constants.texto7
            print(c1)
            c2 = self.player.texto_digitado7
        if self.round_number == 10:
            c1 = Constants.texto8
            print(c1)
            c2 = self.player.texto_digitado8
        if self.round_number == 11:
            c1 = Constants.texto9
            print(c1)
            c2 = self.player.texto_digitado9
        if self.round_number == 12:
            c1 = Constants.texto10
            print(c1)
            c2 = self.player.texto_digitado10
        if self.round_number == 13:
            c1 = Constants.texto11
            print(c1)
            c2 = self.player.texto_digitado11
        if self.round_number == 14:
            c1 = Constants.texto12
            print(c1)
            c2 = self.player.texto_digitado12

        # generar el porcentaje de similitud
        dif1 = difflib.SequenceMatcher(lambda x: x == " \t", c1, c2)
        self.player.porcentaje1 = dif1.ratio()

        if self.player.in_round(1).treatment == Constants.contrato_formal_servicios or self.player.in_round(1).treatment == Constants.contrato_informal_servicios:

            porcentaje = math.ceil(self.player.porcentaje1 *100)
        
            if porcentaje > 80 :
                self.player.payoff = c(1750)

        print(self.player.payoff)
                

    form_model = 'player'

    def get_form_fields(self):
        if self.round_number == 3:
            return ['texto_digitado1']    
        if self.round_number == 4:
            return ['texto_digitado2']     
        if self.round_number == 5:
            return ['texto_digitado3']       
        if self.round_number == 6:
            return ['texto_digitado4']       
        if self.round_number == 7:
            return ['texto_digitado5']       
        if self.round_number == 8:
            return ['texto_digitado6']       
        if self.round_number == 9:
            return ['texto_digitado7']       
        if self.round_number == 10:
            return ['texto_digitado8']      
        if self.round_number == 11:
            return ['texto_digitado9']      
        if self.round_number == 12:
            return ['texto_digitado10']       
        if self.round_number == 13:
            return ['texto_digitado11']       
        if self.round_number == 14:
            return ['texto_digitado12'] 


class Results(Page):
    def is_displayed(self):
        return self.round_number > 2 and self.round_number < Constants.num_rounds

    def vars_for_template(self):

        porcentaje = math.ceil(self.player.porcentaje1 *100)
        print(porcentaje)
       

        return {
            "por": self.player.porcentaje1,
            "porcentaje": porcentaje,
            "ronda": self.round_number,
        }

class Pago(Page):

    def is_displayed(self):
        
        if self.round_number == 6:
            return True
        if self.round_number == 10:
            return True
        if self.round_number == 14:
            return True
        if self.round_number == Constants.num_rounds:
            return True

    def vars_for_template(self):

        if self.round_number != Constants.num_rounds:
            if self.player.in_round(1).treatment == Constants.contrato_formal_servicios or self.player.in_round(1).treatment == Constants.contrato_informal_servicios:
                self.player.payoff = c(0)
            else:
                self.player.payoff = c(7000)

    
class Articulos(Page):
    def is_displayed(self):
        if self.round_number == 6:
            return True
        if self.round_number == 10:
            return True
        if self.round_number == 14:
            return True

    form_model = 'player'
    form_fields = [
        'productos_alimentos',
        'productos_snack',
        'productos_aseo', 
        'productos_electronicos', 
        'productos_servicios', 
        'productos_transporte', 
        'productos_diversion', 
        'productos_ahorro', 
        'productos_deudas',
        'total', 
    ]


class DateWaitPage(Page):


    def is_displayed(self):
        if self.round_number == 6:
            return True
        if self.round_number == 10:
            return True
        if self.round_number == 14:
            return True

    #Pasando datos de Python a JavaScript
    def js_vars(self):
        fecha = ""
        if self.round_number == 6:
            fecha = self.player.in_round(1).next_date
        if self.round_number == 10:
            fecha = self.player.in_round(1).date_after_next
        if self.round_number == 14:
            fecha = self.player.in_round(1).date_after_next
        return dict(
            fecha_espera = fecha,
            #payoff=self.player.payoff,
        )

    def vars_for_template(self):
        
        #Pasar datos entre rondas
        print('======================')
        print(self.player.in_round(1).start_date)
        print(self.player.in_round(1).next_date)
        print(self.player.in_round(1).date_after_next)
        print('======================')

        fecha = ""
        if self.round_number == 6:
            fecha = self.player.in_round(1).next_date
            date_time_obj = datetime.strptime(fecha, '%Y-%m-%d')
        if self.round_number == 10:
            fecha = self.player.in_round(1).date_after_next
            date_time_obj = datetime.strptime(fecha, '%Y-%m-%d')
        if self.round_number == 14:
            fecha = self.player.in_round(1).date_after_next
            date_time_obj = datetime.strptime(fecha, '%Y-%m-%d')

        return {
            "date_time_obj": date_time_obj.date(),   
        }



class ArticulosPost(Page):
    def is_displayed(self):
        if self.round_number == 6:
            return True
        if self.round_number == 10:
            return True
        if self.round_number == 14:
            return True

    form_model = 'player'
    form_fields = [

        'productos_post_alimentos', 
        'productos_post_snack', 
        'productos_post_aseo', 
        'productos_post_electronicos', 
        'productos_post_servicios', 
        'productos_post_transporte', 
        'productos_post_diversion', 
        'productos_post_ahorro', 
        'productos_post_deudas', 
        'total',
       
    ]

class Test(Page):

    live_method ='live_test'

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    form_model = 'player'
    form_fields = ['actividad_2']


class Encuesta(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    
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


class EndGame(Page):
     def is_displayed(self):
        if self.player.consentimiento == False:
            return True
        if self.player.terminos_actividad == False:
            return True
        if self.round_number == Constants.num_rounds:
            return True
        else: 
            return False

page_sequence = [
    ConsentimientoInformado,
    Instrucciones, 
    Contrato_formal_fijo, 
    Contrato_formal_indefinido,
    Contrato_formal_servicios,
    Contrato_informal_fijo, 
    Contrato_informal_indefinido,
    Contrato_informal_servicios,
    Identificacion,
    Ronda_1,
    Results,
    Test,
    Pago,
    Articulos,
    DateWaitPage,
    ArticulosPost,
    Encuesta, 
    EndGame]