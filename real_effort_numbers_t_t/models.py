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

# ******************************************************************************************************************** #
# *** Funciones de Utileria
# ******************************************************************************************************************** #

def make_field(label):
    return models.StringField(
        choices=[
            ['Fuertemente en desacuerdo', ""],
            ['En desacuerdo', ""],
            ['Ligeramente en desacuerdo', ""],
            ['Ni de acuerdo, ni en desacuerdo', ""],
            ['De acuerdo', ""],
            ['Fuertemente de acuerdo', ""],
        ],
        label=label,
        widget=widgets.RadioSelect,
    )

def make_field2(label):
    return models.IntegerField(
        choices=[-2,-1,0,1,2],
        label=label,
    )
class Constants(BaseConstants):
    name_in_url = 'real_effort_numbers_t_t'
    players_per_group = 2
    num_rounds = 11
    fixed_payment = 5000
    payment_per_correct_answer = 50

    #STAGE 1
    num_seconds_stage_1 = 30 # default: 60
    sub_rounds_stage_1 = 10 # final: 10
    num1_random_stage_1 = 1 # default: 50
    num2_random_stage_1 = 2 # default: 99
    timeout_result_round = 5 # default: 10
    list_atrr_round = [
        'correct_answers_round1',
        'correct_answers_round2',
        'correct_answers_round3',
        'correct_answers_round4',
        'correct_answers_round5',
        'correct_answers_round6',
        'correct_answers_round7',
        'correct_answers_round8',
        'correct_answers_round9',
        'correct_answers_round10'
    ]

    #STAGE 2
    num_seconds_stage_2 = 60*5 # default: 60*10
    mandatory_subtraction = 50 # default: 50
    num1_random_stage_2 = 1 # default: 50
    num2_random_stage_2 = 2 # default: 99

class Subsession(BaseSubsession):
    def creating_session(self):
        team_label = ['AB', 'CD', 'EF', 'GH', 'IJ', 'KL']
        labels = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10', 'P11', 'P12']
        number_of_groups = self.session.num_participants // Constants.players_per_group

        for i, player in enumerate(self.get_players()):
            player.participant.label = labels[i]

        #ALL STAGES
        for i in range(0, number_of_groups):
            for j in range(0, Constants.players_per_group):
                self.get_group_matrix(objects=True)[i][j].team = team_label[i]


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    team = models.StringField()
    payment_total = models.IntegerField()

# ******************************************************************************************************************** #
# *** STAGE 1
# ******************************************************************************************************************** #
    answers_correct_stage_1 = models.IntegerField(initial=0)
    answers_wrong_stage_1 = models.IntegerField(initial=0)
    answers_total_stage_1 = models.IntegerField(initial=0)
    payment_stage_1 = models.IntegerField(initial=0)

    ########################## ROUNDS ##########################
    correct_answers_actual_round = models.IntegerField(initial=0) 
    total_substract_actual_round = models.IntegerField(initial=0) 
    payment_actual_round = models.IntegerField(initial=0)
    wrong_substract_actual_round = models.IntegerField(initial=0)

    correct_answers_round1 = models.IntegerField(initial=0) 
    correct_answers_round2 = models.IntegerField(initial=0) 
    correct_answers_round3 = models.IntegerField(initial=0) 
    correct_answers_round4 = models.IntegerField(initial=0) 
    correct_answers_round5 = models.IntegerField(initial=0) 
    correct_answers_round6 = models.IntegerField(initial=0) 
    correct_answers_round7 = models.IntegerField(initial=0) 
    correct_answers_round8 = models.IntegerField(initial=0) 
    correct_answers_round9 = models.IntegerField(initial=0) 
    correct_answers_round10 = models.IntegerField(initial=0) 
    
# ******************************************************************************************************************** #
# *** STAGE 2
# ******************************************************************************************************************** #
    answers_correct_stage_2 = models.IntegerField(initial=0)
    answers_wrong_stage_2 = models.IntegerField(initial=0)
    answers_total_stage_2 = models.IntegerField(initial=0)
    payment_stage_2 = models.IntegerField(initial=0)

# ******************************************************************************************************************** #
# *** STAGE 3
# ******************************************************************************************************************** #
    flip_value = models.FloatField(initial=0.0)
    amount_inversion = models.IntegerField(
        label="Por favor, indica el monto que invertir??s en el activo de riesgo (sin puntos o comas)", 
        min=0, 
        max=5000
    )
    payment_stage_3 = models.IntegerField(initial=0)

# ******************************************************************************************************************** #
# *** Preguntas de Control: 1
# ******************************************************************************************************************** #
    control_question_1 = models.BooleanField(
        label="??Estar?? emparejado con la misma persona en toda la Etapa 1?",
        choices=[
            [True, "S??"],
            [False, "No"],
        ],
        widget=widgets.RadioSelect,
    )

    control_question_2 = models.IntegerField(
        label="Si en la ronda 1, mi compa??ero(a) y yo logramos 20 restas correctas, cada uno ganar??:",
        choices=[
            [1, "1000"],
            [2, "2000"],
            [3, "3000"],
        ],
        widget=widgets.RadioSelect,
    )
# ******************************************************************************************************************** #
# *** Preguntas de Control: 2
# ******************************************************************************************************************** #
    control_question_3 = models.IntegerField(
        label="En la Etapa 2 usted estar?? emparejado con:",
        choices=[
            [1, "Nadie, es un juego individual"],
            [2, "Con la misma persona de la Etapa 1"],
            [3, "Con una persona distinta a la de la Etapa 1"],
        ],
        widget=widgets.RadioSelect,
    )

    control_question_4 = models.IntegerField(
        label="El Jugador X (Juan) puede rechazar el contrato",
        choices=[
            [1, "Verdadero"],
            [2, "Falso"],
        ],
        widget=widgets.RadioSelect,
    )

    control_question_5 = models.IntegerField(
        label="??Cu??nto gana el Jugador X (Juan) cuando NO hay un contrato?",
        choices=[
            [1, "$15,000 siempre"],
            [2, "$8,000 si el Jugador Y (Maria) s??lo le paga una cuota y $15,000 si el Jugador Y (Maria) le paga ambas cuotas"],
            [3, "M??ximo $8,000"],
            [4, "Todos los jugadores reciben $8,000 al iniciar la Etapa 2."],
        ],
        widget=widgets.RadioSelect,
    )

    control_question_6 = models.IntegerField(
        label="??Cu??nto gana el Jugador Y (Maria) cuando S?? hay un contrato?",
        choices=[
            [1, "$10,000 siempre"],
            [2, "$10,000 si el Jugador X (Juan) realiza la tarea completa, y $0 si no lo hace"],
            [3, "$30,000"],
            [4, "Todos los jugadores ganan $15,000 en la Etapa 2"],
        ],
        widget=widgets.RadioSelect,
    )

    control_question_7 = models.IntegerField(
        label="En total, ??Cu??nto le pagar?? a Juan si decide contratarlo? (por favor, registre su respuesta sin puntos ni comas)", 
        min=0, 
        max=50000
    )

    control_question_8 = models.IntegerField(
        label="??Cu??nto pagar?? Juan por el contrato si Mar??a decide contratarlo? (por favor, registre su respuesta sin puntos ni comas)", 
        min=0, 
        max=50000
    )

    control_question_9 = models.IntegerField(
        label="Si Mar??a contratara a Juan ??Cu??nto se le descontar??a a Juan si no alcanzara a completar las 50 restas? (por favor, registre su respuesta sin puntos ni comas)", 
        min=0, 
        max=50000
    )

# ******************************************************************************************************************** #
# *** Validaciones
# ******************************************************************************************************************** #

    def control_question_1_error_message(self, value):
        if value != True:
            return 'Esta respuesta es incorrecta. Por favor, lea las instrucciones e intente de nuevo.'

    def control_question_2_error_message(self, value):
        if value != 1:
            return 'Recuerde que ganar??n $50 por cada respuesta correcta que hayan dado juntos.'

    def control_question_3_error_message(self, value):
        if value != 2:
            return 'Recuerde que usted ser?? emparejado con la misma persona de la Etapa 1.'

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
        if value != 15000:
            return 'Por favor, lea nuevamente las instrucciones'

    def control_question_8_error_message(self, value):
        if value != 3000:
            return 'Por favor, lea nuevamente las instrucciones'
    
    def control_question_9_error_message(self, value):
        if value != 30000:
            return 'Por favor, lea nuevamente las instrucciones'

# ******************************************************************************************************************** #
# *** Variables Consentimiento
# ******************************************************************************************************************** #
    num_temporal = models.IntegerField(
        label="Por favor, ingrese el numero de identificaci??n temporal que le lleg?? en el correo de invitaci??n")
    accepts_data = models.BooleanField(
        label="??Autoriza el uso de los datos recolectados para futuros estudios?",
        choices=[
            [True, "S??"],
            [False, "No"],
        ],
        default=True)
    accepts_terms = models.BooleanField()

# ******************************************************************************************************************** #
# *** Variables Contrato
# ******************************************************************************************************************** #
    pay_contract = models.BooleanField(
        label="",
        choices=[
            [True, "S??"],
            [False, "No"],
        ],
        widget=widgets.RadioSelect,
        default=False,
        blank=True
    )
    believe_pay_contract = models.BooleanField(
        label="",
        choices=[
            [True, "S??"],
            [False, "No"],
        ],
        widget=widgets.RadioSelect,
        default=False,
        blank=True
    )
    pay_second_quote = models.BooleanField(
        label="",
        choices=[
            [True, "S??"],
            [False, "No"],
        ],
        widget=widgets.RadioSelect,
        default=True,
        blank=True
    )

# ******************************************************************************************************************** #
# *** Variables Encuesta sociodemogr??fica
# ******************************************************************************************************************** #
    edad = models.IntegerField(label='??Cu??ntos a??os cumplidos tiene?')
    ciudad = models.StringField(label='??En qu?? ciudad vive actualmente?')

    rol_hogar = models.StringField(
        label='??Cu??l es su rol en su hogar? (Por favor, escoja una opci??n)',
        choices=['Padre / Madre', 'Espos@', 'Hij@', 'Otro']
    )

    estado_civil = models.StringField(
        label='??Cu??l es su estado civil? (Por favor, escoja una opci??n)',
        choices=['Soltero', 'casado', 'Uni??n libre', 'Divorciado', 'Viudo', 'Prefiero no decir']
    )

    hijos = models.IntegerField(label='??Cu??ntos hijos tiene usted?')

    etnia = models.StringField(
        label='De acuerdo con su cultura o rasgos f??sicos, usted es o se reconoce como:(Por favor, escoja una opci??n)',
        choices=['Afrocolombiano', 'Indigena', 'Mestizo', 'Mulato', 'Blanco', 'Raizal del archipielago', 'Palenquero', 'Otro', 'Prefiero no decir']
    )

    religion = models.StringField(
        label='??En cu??l de los siguientes grupos se identifica usted?(Por favor, escoja una opci??n)',
        choices=['Cat??lico', 'Cristiano', 'Testigo de Jehov??', 'Ateo', 'Agn??stico', 'Jud??o', 'Musulm??n', 'Hinduista', 'Otro', 'Prefiero no decir' ]
    )

    estudios = models.StringField(
        label='??Cu??l es el m??ximo nivel de estudios alcanzado a la fecha? (Por favor, escoja una opci??n)',
        choices=[
            'Primaria incompleta',
            'Primaria completa',
            'B??sica secundaria (9?? grado completo)',
            'Media secundaria (11?? grado completo)',
            'T??cnico incompleto',
            'T??cnico completo',
            'Tecnol??gico incompleto',
            'Tecnol??gico completo',
            'Pregrado incompleto',
            'Pregrado completo',
            'Postgrado incompleto',
            'Posgrado completo'
        ]
    )

    actividad_actual = models.StringField(
        label='Actualmente, ??cu??l es su actividad principal? (Por favor, escoja una opci??n)',
        choices=['Estudiar', 'Trabajar', 'Oficios del hogar', 'Buscar trabajo' ,'Otra actividad']
    )

    esta_laborando = models.BooleanField(
        label='??Se encuentra usted laborando actualmente? (Por favor, escoja una opci??n)',
        choices=[
            [True, "S??"],
            [False, "No"],
        ]
    )

    ingreso_mensual = models.StringField(
        label='??Cu??l es su nivel aproximado de ingresos mensuales (incluya mesadas, subsidios y remesas)?',
        choices=[
            'De 1 a $200.000',
            'De $200.001 a $400.000',
            'De $400.001 a $700.000',
            'De $700.001 a $1.000.000',
            'De $1.000.001 a $2.000.000',
            'De $2.000.001 a $5.000.000',
            'M??s de 5.000.001',
            'Prefiero no decir'
        ]
    )

    gasto_mensual = models.StringField(
        label='??Cu??l es su nivel aproximado de gastos mensuales?',
        choices=[
            'De 1 a $200.000',
            'De $200.001 a $400.000',
            'De $400.001 a $700.000',
            'De $700.001 a $1.000.000',
            'De $1.000.001 a $2.000.000',
            'De $2.000.001 a $5.000.000',
            'M??s de 5.000.001',
            'Prefiero no decir'
        ]
    )

    #
    alimentos = models.IntegerField(label="Alimentos")
    aseo = models.IntegerField(label="Productos de aseo")
    electronicos = models.IntegerField(label="Art??culos electr??nicos")
    transporte = models.IntegerField(label="Transporte")
    servicios = models.IntegerField(label="Pago de servicios")
    diversion  = models.IntegerField(label="Diversi??n y ocio")
    ahorro = models.IntegerField(label="Ahorro")
    deudas = models.IntegerField(label="Pago de deudas")

    #Esacala Likert
    offer_1 = models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7,8,9,10], label= "")

    Estabilidad = models.IntegerField(choices=[1,2,3,4,5], label='Mantenerse invariable o inalterable en el mismo lugar, estado o situaci??n.')
    Independencia = models.IntegerField(choices=[1,2,3,4,5], label='Autonom??a de tomar las decisiones propias.')
    Descanso = models.IntegerField(choices=[1,2,3,4,5], label='Reposar fuerzas a trav??s de un estado inactivo')
    Lucro = models.IntegerField(choices=[1,2,3,4,5], label='Ganancia o provecho de alg??n actividad u objeto.')
    Protecci??n = models.IntegerField(choices=[1,2,3,4,5], label='Seguridad o respaldo frente a un acontecimiento.')

    encuesta_tabla1_pregunta1 = make_field('Por lo general, cuando consigo lo que quiero es porque me he esforzado por lograrlo.')
    encuesta_tabla1_pregunta2 = make_field('Cuando hago planes estoy casi seguro (a) que conseguir?? que lleguen a buen t??rmino.')
    encuesta_tabla1_pregunta3 = make_field('Prefiero los juegos que entra??an algo de suerte que los que s??lo requieren habilidad.')
    encuesta_tabla1_pregunta4 = make_field('Si me lo propongo, puedo aprender casi cualquier cosa.')
    encuesta_tabla1_pregunta5 = make_field('Mis mayores logros se deben m??s que nada a mi trabajo arduo y a mi capacidad.')
    encuesta_tabla1_pregunta6 = make_field('Por lo general no establezco metas porque se me dificulta mucho hacer lo necesario para alcanzarlas.')
    encuesta_tabla1_pregunta7 = make_field('La competencia desalienta la excelencia.')
    encuesta_tabla1_pregunta8 = make_field('Las personas a menudo salen adelante por pura suerte.')
    encuesta_tabla1_pregunta9 = make_field('En cualquier tipo de examen o competencia me gusta comparar mis calificaciones con las de los dem??s.')
    encuesta_tabla1_pregunta10 = make_field('Pienso que no tiene sentido empe??arme en trabajar en algo que es demasiado dif??cil para m??.')

    encuesta_tabla2_pregunta1 = make_field('Podr?? alcanzar la mayor??a de los objetivos que me he propuesto.')
    encuesta_tabla2_pregunta2 = make_field('Cuando me enfrento a tareas dif??ciles, estoy seguro de que las cumplir??.')
    encuesta_tabla2_pregunta3 = make_field('En general, creo que puedo obtener resultados que son importantes para m??.')
    encuesta_tabla2_pregunta4 = make_field('Creo que puedo tener ??xito en cualquier esfuerzo que me proponga.')
    encuesta_tabla2_pregunta5 = make_field('Ser?? capaz de superar con ??xito muchos desaf??os.')
    encuesta_tabla2_pregunta6 = make_field('Conf??o en que puedo realizar eficazmente muchas tareas diferentes.')
    encuesta_tabla2_pregunta7 = make_field('Comparado con otras personas, puedo hacer la mayor??a de las tareas muy bien.')
    encuesta_tabla2_pregunta8 = make_field('Incluso cuando las cosas son dif??ciles, puedo realizarlas bastante bien.')
    encuesta_tabla2_pregunta9 = make_field('Podr?? alcanzar la mayor??a de los objetivos que me he propuesto.')

    encuesta_tabla3_pregunta1 = make_field2 ('Llegar tarde a una cita')
    encuesta_tabla3_pregunta2 = make_field2 ('Comprar a vendedores ambulantes')
    encuesta_tabla3_pregunta3 = make_field2 ('Tirar basura en la calle')
    encuesta_tabla3_pregunta4 = make_field2 ('Trabajar y recibir un pago sin que haya firmado un contrato formal (pintar una casa, realizar un reporte, etc.)')
    encuesta_tabla3_pregunta5 = make_field2 ('Silbar o decirle un piropo a un (a) desconocido (a) en la calle')
    encuesta_tabla3_pregunta6 = make_field2 ('Darle trabajo a alguien y pagarle sin pedirle que firme un contrato formal (pintar una casa, realizar un reporte, etc.)')
    encuesta_tabla3_pregunta7 = make_field2 ('Consumir cerveza, aguardiente, ron u otras bebidas alcoh??licas en un and??n o parque')
    encuesta_tabla3_pregunta8 = make_field2 ('No cotizar al sistema de pensiones')
    encuesta_tabla3_pregunta9 = make_field2 ('No aportar al sistema de salud')
    encuesta_tabla3_pregunta10 = make_field2 ('No ceder un asiento preferente a una embarazada o un(a) anciano(a) se sube al bus')
    encuesta_tabla3_pregunta11 = make_field2 ('Colarse en las filas')
    encuesta_tabla3_pregunta12 = make_field2 ('No tener cuenta bancaria')
    encuesta_tabla3_pregunta13 = make_field2 ('Pedir dinero prestado a prestamistas informales (ejemplo: gota a gota)')
    encuesta_tabla3_pregunta14 = make_field2 ('No recoger los desechos de las mascotas')
    encuesta_tabla3_pregunta15 = make_field2 ('Usar transportes alternativos como piratas o mototaxis')
    encuesta_tabla3_pregunta16 = make_field2 ('Vender cosas o hacer negocios de manera informal')
    encuesta_tabla3_pregunta17 = make_field2 ('Usar plataformas de transporte como Uber, Didi, etc.')
    encuesta_tabla3_pregunta18 = make_field2 ('No votar')
    encuesta_tabla3_pregunta19 = make_field2 ('Ir a eventos pol??ticos para conseguir empleo/beneficios personales')
    encuesta_tabla3_pregunta20 = make_field2 ('Comprar r??plicas de productos originales (lociones, bolsos, zapatos, camisas)')
    encuesta_tabla3_pregunta21 = make_field2 ('Comprar productos sin factura')
    encuesta_tabla3_pregunta22 = make_field2 ('Subarrendar una habitaci??n')
    encuesta_tabla3_pregunta23 = make_field2 ('Vivir en una habitaci??n subarrendada')
    encuesta_tabla3_pregunta24 = make_field2 ('No usar el paso cebra o los puentes peatonales para cruzar una calle')
    encuesta_tabla3_pregunta25 = make_field2 ('Cruzar caminando una calle cuando el sem??foro peatonal est?? en rojo')
    encuesta_tabla3_pregunta26 = make_field2 ('Circular en bicicleta por el and??n (no usar la cicloruta)')

# ******************************************************************************************************************** #
# *** Acceder al otro jugador
# ******************************************************************************************************************** #
    def other_player(self):
        # self.get_others_in_group() -> Vector[<Player  2>, <Player  3>, <Player  4>]
        return self.get_others_in_group()[0]
