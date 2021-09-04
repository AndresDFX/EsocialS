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

class Constants(BaseConstants):
    name_in_url = 'Cuestionario'
    players_per_group = None
    num_rounds = 1
    endowment = c(1)
    minY1 = 0
    minZ1 = 2
    maxY1 = 10
    maxZ1 = 8

class Subsession(BaseSubsession):
    pass
    
    
class Group(BaseGroup):
    pass

class Participant(BasePlayer):

    pass

class Player(BasePlayer):
    import random
    var_aleY1 = models.IntegerField(initial=random.randint(0,10))
    var_aleZ1 = models.IntegerField(initial=random.randint(2,8))

    respuestasOK = models.IntegerField(initial = 0)
    Total = models.models.IntegerField(null = True, blank = True)
    
    age = models.IntegerField(label='¿Cuál es su edad?', min=13, max=125)

    gender = models.StringField(
        choices = [['H', 'Hombre'], ['M', 'Mujer']],
        label = '¿Cuál es su sexo?',
        widget = widgets.RadioSelectHorizontal,
    )
    
    decision = models.BooleanField(
        choices = [[True,'Urna Y'],[False,'Urna Z']],
        label = 'Por favor a continuación seleccione una de las urnas',
        widget = widgets.RadioSelectHorizontal,        
    )

    E1 = models.IntegerField(
        choices=[[1,'(2+2)*5/2'], [0,'((1+2+3+4+5+6)/7)+7'],[0,'((50*10)/2)-200'],[0,'Ninguna de las anteriores']],
        label='1. ¿Cuál es la ecuación equivalente a esta: ((100/2)-10)/2?',
        widget=widgets.RadioSelect,
    )

    E2 = models.IntegerField(
        choices=[[0,'(2+2)*5/2'], [1,'((1+2+3+4+5+6)/7)+7'],[0,'((50*10)/2)-200'],[0,'Ninguna de las anteriores']],
        label='2. ¿Cuál es la ecuación equivalente a esta: ((100/2)-10)/2?',
        widget=widgets.RadioSelect,
    )

    E3 = models.IntegerField(
        choices=[[1,'(2+2)*5/2'], [0,'((1+2+3+4+5+6)/7)+7'],[0,'((50*10)/2)-200'],[0,'Ninguna de las anteriores']],
        label='3. ¿Cuál es la ecuación equivalente a esta: ((100/2)-10)/2?',
        widget=widgets.RadioSelect,
    )

    E4 = models.IntegerField(
        choices=[[1,'(2+2)*5/2'], [2,'((1+2+3+4+5+6)/7)+7'],[3,'((50*10)/2)-200'],[4,'Ninguna de las anteriores']],
        label='4. ¿Cuál es la ecuación equivalente a esta: ((100/2)-10)/2?',
        widget=widgets.RadioSelect,
    )

    E5 = models.IntegerField(
        choices=[[1,'(2+2)*5/2'], [2,'((1+2+3+4+5+6)/7)+7'],[3,'((50*10)/2)-200'],[4,'Ninguna de las anteriores']],
        label='5. ¿Cuál es la ecuación equivalente a esta: ((100/2)-10)/2?',
        widget=widgets.RadioSelect,
    )

    primera = models.IntegerField(
        choices=[[1,'2 UM'], [2,'0 UM'],[3,'8 UM'],[4,'Ninguna de las anteriores']],
        label='1. ¿Cuál es el valor mínimo de UM que puede salir de la Urna Z?',
        widget=widgets.RadioSelect,
    )

    segunda = models.IntegerField(
        choices=[[1,'2 UM'], [2,'0 UM'],[3,'8 UM'],[4,'Ninguna de las anteriores']],
        label='2. ¿Cuál es el valor mínimo de UM que puede salir de la Urna Y?',
        widget=widgets.RadioSelect,
    )

    tercera = models.IntegerField(
        choices=[[1,'8 UM'], [2,'10 UM'],[3,'6 UM'],[4,'Ninguna de las anteriores']],
        label='3. ¿Cuál es el valor máximo de UM que puede salir de la Urna Y?',
        widget=widgets.RadioSelect,
    )

    cuarta = models.IntegerField(
        choices=[[1,'144 UM'], [2,'112 UM'],[3,'126 UM'],[4,'Ninguna de las anteriores']],
        label='4. Si para las rondas 6-10 usted escoge la urna Z y sale al azar una moneda de valor 7 UM, ¿cuántas UM ganará en la ronda 8 si logra 18 respuestas correctas?',
        widget=widgets.RadioSelect,
    )

    quinta = models.IntegerField(
        choices=[[1,'$2,500'], [2,'$1,680'],[3,'$2,800'],[4,'Ninguna de las anteriores']],
        label='5. Suponga que para las rondas 11-15 usted escoge la urna Y y sale al azar una moneda de valor 3 UM. ¿cuánto dinero ganaría si obtuvo 21 respuestas correctas? ',
        widget=widgets.RadioSelect,
    )
  
    

    def primera_error_message(self,value):
        if value != 1:
            return "Respuesta incorrecta, por favor lea de nuevo las instrucciones."
    def segunda_error_message(self,value):
        if value != 2:
            return "Respuesta incorrecta, por favor lea de nuevo las instrucciones."     
    def tercera_error_message(self,value):
        if value != 2:
            return "Respuesta incorrecta, por favor lea de nuevo las instrucciones."
    def cuarta_error_message(self,value):
        if value != 3:
            return "Respuesta incorrecta, por favor lea de nuevo las instrucciones."
    def quinta_error_message(self,value):
        if value != 4:
            return "Respuesta incorrecta, por favor lea de nuevo las instrucciones."
    