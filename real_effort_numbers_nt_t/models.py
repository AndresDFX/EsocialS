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

import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'real_effort_numbers_nt_t'
    players_per_group = 2
    num_rounds = 100
    payment_per_correct_answer = 50
    payment_per_correct_answer_2 = 50
    fixed_payment = 5000
    sumas_obligatorias_contrato = 50
    num_min_stage_1 = 10
    num_min_stage_2 = 5
    

class Subsession(BaseSubsession):
    def creating_session(self):
        #print("Matriz del grupo: " + str(self.get_group_matrix()))
        #print("Grupos: " + str(self.get_groups()))
        # for player in self.get_players():
        #     print("Jugador id_group: " + str(player.id_in_group))
        #     print("Jugador id_session: " + str(player.participant.id_in_session))

        #Groups players randomly in the first half and in the second half assigns players with their teammates

        team_label = ['AB', 'CD', 'EF', 'GH', 'IJ', 'KL', 'MN', 'OP', 'QR', 'ST', 'UV', 'WX', 'YZ']
        number_of_groups = self.session.num_participants // Constants.players_per_group
        
        for player in self.get_players():
            player.cara_sello_value = random.random()

        if self.round_number == 1:
            self.group_randomly(fixed_id_in_group=True)

        if self.round_number >= 1 and self.round_number <= (Constants.num_rounds/2):
            self.group_like_round(1)

        # Randomizes teams and then groups them together

        if self.round_number == (Constants.num_rounds/2)+1:
            # print("Cambio")
            self.group_randomly(fixed_id_in_group=True)
        if self.round_number >= (Constants.num_rounds/2)+1:
            self.group_like_round((Constants.num_rounds/2+1))
            for i in range(0,number_of_groups):
                for j in range(0,Constants.players_per_group):
                    self.get_group_matrix()[i][j].team = team_label[i]
       # print("Matriz del grupo N: " + str(self.get_group_matrix()))
        #print("Grupos N: " + str(self.get_groups()))     

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
    num_min_stage_1 = models.IntegerField(initial=5)
    contador_numero_aux = models.IntegerField(initial=0)
    team = models.StringField()
    cara_sello_value = models.FloatField(initial=0.0)
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
# *** Variables Riesgo
# ******************************************************************************************************************** #
    monto = models.IntegerField(label = 
    "Por favor, indica el monto que invertirás en el activo de riesgo (sin puntos o comas)", min=0, max=5000)
    pago_total = models.IntegerField()    
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
        if value != False:
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
# *** Variables Encuesta sociodemográfica
# ******************************************************************************************************************** #
    genero = models.StringField(
        label="¿Cuál es su género?",
        choices=[["Masculino", "Masculino"], #[StoredValue, "Label"]
                ["Femenino", "Femenino"]],
        widget=widgets.RadioSelect,
    )
    edad = models.IntegerField(label="¿Cuántos años cumplidos tiene usted?")
    ciudad = models.StringField(label="¿En qué ciudad vive actualmente?")
    estrato = models.IntegerField(
        label="¿Cuál es el estrato de la vivienda en la cual habita actualmente?",
        choices = [
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
            [6, "6"]],
        widget=widgets.RadioSelect)
    estado_civil =  models.StringField(
        label="¿Cuál es su estado civil? Escoja una opción",
        choices = [
            ["Soltero", "Soltero"],
            ["Casado ", "Casado "],
            ["Unión libre", "Unión libre"],
            ["Divorciado", "Divorciado"],
            ["Viudo", "Viudo"],
            ["Prefiero no decir", "Prefiero no decir"],
        ],
        widget=widgets.RadioSelect
    )
    numero_hijos = models.IntegerField(label="¿Cuántos hijos tiene usted?")
    identifica_cultura = models.StringField(
        label="De acuerdo con su cultura o rasgos físicos, usted es o se reconoce como:",
        choices = [
            ["Afro-colombiano", "Afro-colombiano"],
            ["Indígena ", "Indígena "],
            ["Mestizo", "Mestizo"],
            ["Mulato", "Mulato"],
            ["Blanco", "Blanco"],
            ["Raizal del archipielago", "Raizal del archipielago"],
            ["Palenquero", "Palenquero"],
            ["Otro", "Otro"],
            ["Prefiero no decir", "Prefiero no decir"],
        ],
        widget=widgets.RadioSelect
    )
    identifica_religion = models.StringField(
        label="¿En cuál de los siguientes grupos se identifica usted? Escoja una opción",
        choices = [
            ["Católico", "Católico"],
            ["Cristiano ", "Cristiano "],
            ["Testigo de Jehová", "Testigo de Jehová"],
            ["Ateo", "Ateo"],
            ["Judío", "Judío"],
            ["Musulmán", "Musulmán"],
            ["Hinduista", "Hinduista"],
            ["Otro", "Otro"],
            ["Prefiero no decir", "Prefiero no decir"],
        ],
        widget=widgets.RadioSelect
    )
    nivel_estudios = models.StringField(
        label="¿Cuál es el máximo nivel de estudios alcanzado a la fecha? Escoja una opción",
        choices = [
            ["Primaria incompleta", "Primaria incompleta"],
            ["Primaria completa ", "Primaria completa "],
            ["Básica secundaria (9o grado completo)", "Básica secundaria (9o grado completo)"],
            ["Media secundaria (11o grado completo)", "Media secundaria (11o grado completo)"],
            ["Técnico incompleto", "Técnico incompleto"],
            ["Técnico completo", "Técnico completo"],
            ["Tecnológico incompleto", "Tecnológico incompleto"],
            ["Tecnológico completo", "Tecnológico completo"],
            ["Pregrado incompleto", "Pregrado incompleto"],
            ["Pregrado completo", "Pregrado completo"],
            ["Postgrado incompleto", "Postgrado incompleto"],
            ["Posgrado completo", "Posgrado completo"],
        ],
        widget=widgets.RadioSelect
    )
    tendencia_politica = models.IntegerField(
        label="Hoy en día cuando se habla de tendencias políticas, mucha gente habla de aquellos que simpatizan más con la izquierda o con la derecha. Según el sentido que tengan para usted los términos 'izquierda' y 'derecha' cuando piensa sobre su punto de vista político, ¿dónde se encontraría usted en esta escala?",
        choices = [
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
            [6, "6"],
            [7, "7"],
            [8, "8"],
            [9, "9"],
            [10, "10"],
        ],
        widget=widgets.RadioSelect,
    )
    disposicion_riesgos = models.IntegerField(
        label="Por favor, califique en un escala de 1 a 10 su disposición a asumir riesgos en general, siendo 1 para nada dispuesto y 10 completamente dispuesto",
        choices = [
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
            [6, "6"],
            [7, "7"],
            [8, "8"],
            [9, "9"],
            [10, "10"],
        ],
        widget=widgets.RadioSelect,
    )
     # ******************************************************************************************************************** #
# *** Pregunta 24: Primer conjunto de afirmaciones (10 preguntas)
# ******************************************************************************************************************** #
    conseguir_esfuerzo =  models.StringField(
        label="Por lo general, cuando consigo lo que quiero es porque me he esforzado por lograrlo.",
        choices = [
            ["Fuertemente en desacuerdo", "Fuertemente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ligeramente en desacuerdo", "Ligeramente en desacuerdo"],
            ["Ni de acuerdo, ni en desacuerdo", "Ni de acuerdo, ni en desacuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Fuertemente de acuerdo", "Fuertemente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    planes_termino =  models.StringField(
        label="Cuando hago planes estoy casi seguro (a) que conseguiré que lleguen a buen término.",
        choices = [
            ["Fuertemente en desacuerdo", "Fuertemente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ligeramente en desacuerdo", "Ligeramente en desacuerdo"],
            ["Ni de acuerdo, ni en desacuerdo", "Ni de acuerdo, ni en desacuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Fuertemente de acuerdo", "Fuertemente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    juego_suerte =  models.StringField(
        label="Prefiero los juegos que entrañan algo de suerte que los que sólo requieren habilidad.",
        choices = [
            ["Fuertemente en desacuerdo", "Fuertemente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ligeramente en desacuerdo", "Ligeramente en desacuerdo"],
            ["Ni de acuerdo, ni en desacuerdo", "Ni de acuerdo, ni en desacuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Fuertemente de acuerdo", "Fuertemente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    propongo_aprender =  models.StringField(
        label="Si me lo propongo, puedo aprender casi cualquier cosa.",
        choices = [
            ["Fuertemente en desacuerdo", "Fuertemente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ligeramente en desacuerdo", "Ligeramente en desacuerdo"],
            ["Ni de acuerdo, ni en desacuerdo", "Ni de acuerdo, ni en desacuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Fuertemente de acuerdo", "Fuertemente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    mayores_logros =  models.StringField(
        label="Mis mayores logros se deben más que nada a mi trabajo arduo y a mi capacidad",
        choices = [
            ["Fuertemente en desacuerdo", "Fuertemente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ligeramente en desacuerdo", "Ligeramente en desacuerdo"],
            ["Ni de acuerdo, ni en desacuerdo", "Ni de acuerdo, ni en desacuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Fuertemente de acuerdo", "Fuertemente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    establecer_metas =  models.StringField(
        label="Por lo general no establezco metas porque se me dificulta mucho hacer lo necesario para alcanzarlas.",
        choices = [
            ["Fuertemente en desacuerdo", "Fuertemente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ligeramente en desacuerdo", "Ligeramente en desacuerdo"],
            ["Ni de acuerdo, ni en desacuerdo", "Ni de acuerdo, ni en desacuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Fuertemente de acuerdo", "Fuertemente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    competencia_excelencia =  models.StringField(
        label="La competencia desalienta la excelencia",
        choices = [
            ["Fuertemente en desacuerdo", "Fuertemente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ligeramente en desacuerdo", "Ligeramente en desacuerdo"],
            ["Ni de acuerdo, ni en desacuerdo", "Ni de acuerdo, ni en desacuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Fuertemente de acuerdo", "Fuertemente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    salir_adelante =  models.StringField(
        label="Las personas a menudo salen adelante por pura suerte.",
        choices = [
            ["Fuertemente en desacuerdo", "Fuertemente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ligeramente en desacuerdo", "Ligeramente en desacuerdo"],
            ["Ni de acuerdo, ni en desacuerdo", "Ni de acuerdo, ni en desacuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Fuertemente de acuerdo", "Fuertemente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    comparar_calificaciones =  models.StringField(
        label="En cualquier tipo de examen o competencia me gusta comparar mis calificaciones con las de los demás.",
        choices = [
            ["Fuertemente en desacuerdo", "Fuertemente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ligeramente en desacuerdo", "Ligeramente en desacuerdo"],
            ["Ni de acuerdo, ni en desacuerdo", "Ni de acuerdo, ni en desacuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Fuertemente de acuerdo", "Fuertemente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    empeno_trabajo = models.StringField(
        label="Pienso que no tiene sentido empeñarme en trabajar en algo que es demasiado difícil para mí.",
        choices = [
            ["Fuertemente en desacuerdo", "Fuertemente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ligeramente en desacuerdo", "Ligeramente en desacuerdo"],
            ["Ni de acuerdo, ni en desacuerdo", "Ni de acuerdo, ni en desacuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Fuertemente de acuerdo", "Fuertemente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    # ******************************************************************************************************************** #
# *** Pregunta 25: Segundo conjunto de afirmaciones (10 preguntas)
# ******************************************************************************************************************** #
    alcanzar_objetivos = models.StringField(
        label="Podré alcanzar la mayoría de los objetivos que me he propuesto.",
        choices = [
            ["Fuertemente en desacuerdo", "Fuertemente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ligeramente en desacuerdo", "Ligeramente en desacuerdo"],
            ["Ni de acuerdo, ni en desacuerdo", "Ni de acuerdo, ni en desacuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Fuertemente de acuerdo", "Fuertemente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    cumplir_tareas = models.StringField(
        label="Cuando me enfrento a tareas difíciles, estoy seguro de que las cumpliré.",
        choices = [
            ["Fuertemente en desacuerdo", "Fuertemente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ligeramente en desacuerdo", "Ligeramente en desacuerdo"],
            ["Ni de acuerdo, ni en desacuerdo", "Ni de acuerdo, ni en desacuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Fuertemente de acuerdo", "Fuertemente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    obtener_resultados = models.StringField(
        label="En general, creo que puedo obtener resultados que son importantes para mí.",
        choices = [
            ["Fuertemente en desacuerdo", "Fuertemente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ligeramente en desacuerdo", "Ligeramente en desacuerdo"],
            ["Ni de acuerdo, ni en desacuerdo", "Ni de acuerdo, ni en desacuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Fuertemente de acuerdo", "Fuertemente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    exito_esfuerzo = models.StringField(
        label="Creo que puedo tener éxito en cualquier esfuerzo que me proponga.",
        choices = [
            ["Fuertemente en desacuerdo", "Fuertemente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ligeramente en desacuerdo", "Ligeramente en desacuerdo"],
            ["Ni de acuerdo, ni en desacuerdo", "Ni de acuerdo, ni en desacuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Fuertemente de acuerdo", "Fuertemente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    superar_desafios = models.StringField(
        label="Seré capaz de superar con éxito muchos desafíos.",
        choices = [
            ["Fuertemente en desacuerdo", "Fuertemente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ligeramente en desacuerdo", "Ligeramente en desacuerdo"],
            ["Ni de acuerdo, ni en desacuerdo", "Ni de acuerdo, ni en desacuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Fuertemente de acuerdo", "Fuertemente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    confianza_tareas = models.StringField(
        label="Confío en que puedo realizar eficazmente muchas tareas diferentes.",
        choices = [
            ["Fuertemente en desacuerdo", "Fuertemente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ligeramente en desacuerdo", "Ligeramente en desacuerdo"],
            ["Ni de acuerdo, ni en desacuerdo", "Ni de acuerdo, ni en desacuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Fuertemente de acuerdo", "Fuertemente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    tareas_excelencia = models.StringField(
        label="Comparado con otras personas, puedo hacer la mayoría de las tareas muy bien.",
        choices = [
            ["Fuertemente en desacuerdo", "Fuertemente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ligeramente en desacuerdo", "Ligeramente en desacuerdo"],
            ["Ni de acuerdo, ni en desacuerdo", "Ni de acuerdo, ni en desacuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Fuertemente de acuerdo", "Fuertemente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    tareas_dificiles = models.StringField(
        label="Incluso cuando las cosas son difíciles, puedo realizarlas bastante bien.",
        choices = [
            ["Fuertemente en desacuerdo", "Fuertemente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ligeramente en desacuerdo", "Ligeramente en desacuerdo"],
            ["Ni de acuerdo, ni en desacuerdo", "Ni de acuerdo, ni en desacuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Fuertemente de acuerdo", "Fuertemente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
     # ******************************************************************************************************************** #
# *** Pregunta 26: Segundo conjunto de afirmaciones (10 preguntas)
# ******************************************************************************************************************** #
    tarde_cita = models.IntegerField(
        label="Llegar tarde a una cita",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    comprar_vendedores_ambulantes = models.IntegerField(
        label="Comprar a vendedores ambulantes",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    trabajar_sin_contrato = models.IntegerField(
        label="Trabajar y recibir un pago sin que haya firmado un contrato formal (pintar una casa, realizar un reporte, etc.)",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    emplear_sin_contrato = models.IntegerField(
        label="Darle trabajo a alguien y pagarle sin pedirle que firme un contrato formal (pintar una casa, realizar un reporte, etc.)",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    no_cotizar_pension = models.IntegerField(
        label="No cotizar al sistema de pensiones",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    no_cotizar_salud = models.IntegerField(
        label="No aportar al sistema de salud",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    no_cuenta_bancaria = models.IntegerField(
        label="No tener cuenta bancaria",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    pedir_prestado = models.IntegerField(
        label="Pedir dinero prestado a prestamistas informales (ejemplo: gota a gota)",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    transporte_alternativo = models.IntegerField(
        label="Usar transportes alternativos como piratas o mototaxis",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    vender_informal = models.IntegerField(
        label="Vender cosas o hacer negocios de manera informal",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    no_votar = models.IntegerField(
        label="No votar",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    comprar_sin_factura = models.IntegerField(
        label="Comprar productos sin factura",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    # ******************************************************************************************************************** #
# *** Pregunta 27: Segundo conjunto de afirmaciones (10 preguntas)
# ******************************************************************************************************************** #
    tarde_cita_otros = models.IntegerField(
        label="Llegar tarde a una cita",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    comprar_vendedores_ambulantes_otros = models.IntegerField(
        label="Comprar a vendedores ambulantes",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    trabajar_sin_contrato_otros = models.IntegerField(
        label="Trabajar y recibir un pago sin que haya firmado un contrato formal (pintar una casa, realizar un reporte, etc.)",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    emplear_sin_contrato_otros = models.IntegerField(
        label="Darle trabajo a alguien y pagarle sin pedirle que firme un contrato formal (pintar una casa, realizar un reporte, etc.)",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    no_cotizar_pension_otros = models.IntegerField(
        label="No cotizar al sistema de pensiones",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    no_cotizar_salud_otros = models.IntegerField(
        label="No aportar al sistema de salud",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    no_cuenta_bancaria_otros = models.IntegerField(
        label="No tener cuenta bancaria",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    pedir_prestado_otros = models.IntegerField(
        label="Pedir dinero prestado a prestamistas informales (ejemplo: gota a gota)",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    transporte_alternativo_otros = models.IntegerField(
        label="Usar transportes alternativos como piratas o mototaxis",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    vender_informal_otros = models.IntegerField(
        label="Vender cosas o hacer negocios de manera informal",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    no_votar_otros = models.IntegerField(
        label="No votar",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    comprar_sin_factura_otros = models.IntegerField(
        label="Comprar productos sin factura",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect   
    )
     # ******************************************************************************************************************** #
# *** Pregunta 28: Apropiado (10 preguntas)
# ******************************************************************************************************************** #
    tarde_cita_apropiado = models.IntegerField(
        label="Llegar tarde a una cita",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    comprar_vendedores_ambulantes_apropiado = models.IntegerField(
        label="Comprar a vendedores ambulantes",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    trabajar_sin_contrato_apropiado = models.IntegerField(
        label="Trabajar y recibir un pago sin que haya firmado un contrato formal (pintar una casa, realizar un reporte, etc.)",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    emplear_sin_contrato_apropiado = models.IntegerField(
        label="Darle trabajo a alguien y pagarle sin pedirle que firme un contrato formal (pintar una casa, realizar un reporte, etc.)",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    no_cotizar_pension_apropiado = models.IntegerField(
        label="No cotizar al sistema de pensiones",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    no_cotizar_salud_apropiado = models.IntegerField(
        label="No aportar al sistema de salud",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    no_cuenta_bancaria_apropiado = models.IntegerField(
        label="No tener cuenta bancaria",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    pedir_prestado_apropiado = models.IntegerField(
        label="Pedir dinero prestado a prestamistas informales (ejemplo: gota a gota)",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    transporte_alternativo_apropiado = models.IntegerField(
        label="Usar transportes alternativos como piratas o mototaxis",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    vender_informal_apropiado = models.IntegerField(
        label="Vender cosas o hacer negocios de manera informal",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    no_votar_apropiado = models.IntegerField(
        label="No votar",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    comprar_sin_factura_apropiado = models.IntegerField(
        label="Comprar productos sin factura",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect  
    )
# ******************************************************************************************************************** #
# *** Acceder al otro jugador
# ******************************************************************************************************************** #
    def other_player(self):
        #self.get_others_in_group() -> Vector[<Player  2>, <Player  3>, <Player  4>]
        return self.get_others_in_group()[0]
  