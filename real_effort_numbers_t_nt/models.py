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
from multiselectfield import MultiSelectField

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
        choices=[-2, -1, 0, 1, 2],
        label=label,
    )
class Constants(BaseConstants):
    name_in_url = 'real_effort_numbers_t_nt'
    players_per_group = 2
    num_rounds = 100
    fixed_payment = 5000

    #Stage 1
    payment_per_correct_answer = 50
    num_seconds_stage_1 = 60
    sub_rounds_stage_1 = 10
    num1_random_stage_1 = 1000
    num2_random_stage_1 = 2000

    #Stage 2
    payment_per_correct_answer_2 = 50
    num_seconds_stage_2 = 10*60
    restas_obligatorias_contrato = 50
    num1_random_stage_2 = 1000
    num2_random_stage_2 = 2000


class Subsession(BaseSubsession):
    def creating_session(self):

        team_label = ['AB', 'CD', 'EF', 'GH', 'IJ', 'KL']
        labels = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10', 'P11', 'P12']
        number_of_groups = self.session.num_participants // Constants.players_per_group

        for i, player in enumerate(self.get_players()):
            player.cara_sello_value = random.random()
            player.participant.label = labels[i]

        
        if self.round_number >= 1 and self.round_number <= (Constants.num_rounds/2):
            for i in range(0,number_of_groups):
                for j in range(0,Constants.players_per_group):
                    self.get_group_matrix()[i][j].team = team_label[i]
            # print("Matriz del grupo: " + str(self.get_group_matrix()))

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
    team = models.StringField()
# ******************************************************************************************************************** #
# *** Variables Etapa 1
# ******************************************************************************************************************** #
    number_entered = models.IntegerField(label="")
    sum_of_numbers = models.IntegerField()
    correct_answers = models.IntegerField(initial=0)
    wrong_sums = models.IntegerField(initial=0)
    total_sums = models.IntegerField(initial=0)
    payment_stage_1 = models.IntegerField(initial=0)
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
# *** Variables Etapa 3
# ******************************************************************************************************************** #
    countFlips = models.IntegerField(initial=0)
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
        label="Si en la ronda 1, mi compañero(a) y yo logramos 20 restas correctas, cada uno ganará:",
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
        label="En la Etapa 2 usted estará emparejado con:",
        choices=[
            [1, "Nadie, es un juego individual"],
            [2, "Con la misma persona de la Etapa 1"],
            [3, "Con una persona distinta a la de la Etapa 1"],
        ],
        widget=widgets.RadioSelect,
    )

    control_question_4 = models.IntegerField(
        label="El Jugador X puede rechazar el contrato",
        choices=[
            [1, "Verdadero"],
            [2, "Falso"],
        ],
        widget=widgets.RadioSelect,
    )

    control_question_5 = models.IntegerField(
        label="¿Cuánto gana el Jugador X cuando NO hay un contrato?",
        choices=[
            [1, "$15,000 siempre"],
            [2, "$8,000 si el Jugador Y sólo le pagan una cuota y $15,000 si el Jugador Y le paga ambas cuotas"],
            [3, "Máximo $8,000"],
            [4, "Todos los jugadores reciben $8,000 al iniciar la Etapa 2."],
        ],
        widget=widgets.RadioSelect,
    )

    control_question_6 = models.IntegerField(
        label="¿Cuánto gana el Jugador Y cuando SÍ hay un contrato?",
        choices=[
            [1, "$10,000 siempre"],
            [2, "$10,000 si el Jugador X realiza la tarea completa, y $0 si no lo hace"],
            [3, "$30,000"],
            [4, "Todos los jugadores ganan $15,000 en la Etapa 2"],
        ],
        widget=widgets.RadioSelect,
    )

    control_question_7 = MultiSelectField(
        choices=[
            ["1", "Sólo le pagarían la primera cuota de $8,000"],
            ["2", "Debe pagar el costo del contrato de $3,000"],
            ["3", "Debe pagar el costo del contrato de $5,000"],
            ["4", "Debe realizar la tarea completa o pagar $30,000 al Jugador Y"],
            ["5", "Sólo le pagarán la primera cuota de $7,000"],
        ]
    )

    control_question_8 = MultiSelectField(
        choices=[
            ["6", "Debe pagarle las dos cuotas al Jugador X: $15,000"],
            ["7", "Debe pagar el costo del contrato de $3,000"],
            ["8", "Debe pagar el costo del contrato de $5,000"],
            ["9", "Debe realizar la tarea completa"],
            ["10", "Sólo le pagarán si el Jugador X realiza la tarea completa"],
        ]
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
        if value != 3:
            return 'Recuerde que usted será emparejado con una persona distinta a la de la Etapa 1.'

    def control_question_4_error_message(self, value):
        if value != 2:
            return 'Por favor, lea nuevamente las instrucciones'

    def control_question_5_error_message(self, value):
        if value != 2:
            return 'Por favor, lea nuevamente las instrucciones'

    def control_question_7_error_message(self, value):
        if value != ['2','4']:
            return 'Por favor, lea nuevamente las instrucciones'

    def control_question_8_error_message(self, value):
        if value != ['6', '8']:
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
    pay_second_quote = models.BooleanField(
        label="",
        choices=[
            [True, "Sí"],
            [False, "No"],
        ],
        widget=widgets.RadioSelect,
        default=True,
        blank=True
    )
# ******************************************************************************************************************** #
# *** Variables Encuesta sociodemográfica
# ******************************************************************************************************************** #
    edad = models.IntegerField(label='¿Cuántos años cumplidos tiene?')
    ciudad = models.StringField(label='¿En qué ciudad vive actualmente?')

    rol_hogar = models.StringField(
        label='¿Cuál es su rol en su hogar? (Por favor, escoja una opción)',
        choices=['Padre / Madre', 'Espos@', 'Hij@', 'Otro']
    )

    estado_civil = models.StringField(
        label='¿Cuál es su estado civil? (Por favor, escoja una opción)',
        choices=['Soltero', 'casado', 'Unión libre',
                 'Divorciado', 'Viudo', 'Prefiero no decir']
    )

    hijos = models.IntegerField(label='¿Cuántos hijos tiene usted?')

    etnia = models.StringField(
        label='De acuerdo con su cultura o rasgos físicos, usted es o se reconoce como:(Por favor, escoja una opción)',
        choices=['Afrocolombiano', 'Indigena', 'Mestizo', 'Mulato', 'Blanco',
                 'Raizal del archipielago', 'Palenquero', 'Otro', 'Prefiero no decir']
    )

    religion = models.StringField(
        label='¿En cuál de los siguientes grupos se identifica usted?(Por favor, escoja una opción)',
        choices=['Católico', 'Cristiano', 'Testigo de Jehová', 'Ateo', 'Agnóstico',
                 'Judío', 'Musulmán', 'Hinduista', 'Otro', 'Prefiero no decir']
    )

    estudios = models.StringField(
        label='¿Cuál es el máximo nivel de estudios alcanzado a la fecha? (Por favor, escoja una opción)',
        choices=[
            'Primaria incompleta',
            'Primaria completa',
            'Básica secundaria (9º grado completo)',
            'Media secundaria (11º grado completo)',
            'Técnico incompleto',
            'Técnico completo',
            'Tecnológico incompleto',
            'Tecnológico completo',
            'Pregrado incompleto',
            'Pregrado completo',
            'Postgrado incompleto',
            'Posgrado completo'
        ]
    )

    actividad_actual = models.StringField(
        label='Actualmente, ¿cuál es su actividad principal? (Por favor, escoja una opción)',
        choices=['Estudiar', 'Trabajar', 'Oficios del hogar',
                 'Buscar trabajo', 'Otra actividad']
    )

    esta_laborando = models.BooleanField(
        label='¿Se encuentra usted laborando actualmente? (Por favor, escoja una opción)',
        choices=[
            [True, "Sí"],
            [False, "No"],
        ]
    )

    ingreso_mensual = models.StringField(
        label='¿Cuál es su nivel aproximado de ingresos mensuales (incluya mesadas, subsidios y remesas)?',
        choices=[
            'De 1 a $200.000',
            'De $200.001 a $400.000',
            'De $400.001 a $700.000',
            'De $700.001 a $1.000.000',
            'De $1.000.001 a $2.000.000',
            'De $2.000.001 a $5.000.000',
            'Más de 5.000.001',
            'Prefiero no decir'
        ]
    )

    gasto_mensual = models.StringField(
        label='¿Cuál es su nivel aproximado de gastos mensuales?',
        choices=[
            'De 1 a $200.000',
            'De $200.001 a $400.000',
            'De $400.001 a $700.000',
            'De $700.001 a $1.000.000',
            'De $1.000.001 a $2.000.000',
            'De $2.000.001 a $5.000.000',
            'Más de 5.000.001',
            'Prefiero no decir'
        ]
    )

    #
    alimentos = models.IntegerField(label="Alimentos")
    aseo = models.IntegerField(label="Productos de aseo")
    electronicos = models.IntegerField(label="Artículos electrónicos")
    transporte = models.IntegerField(label="Transporte")
    servicios = models.IntegerField(label="Pago de servicios")
    diversion = models.IntegerField(label="Diversión y ocio")
    ahorro = models.IntegerField(label="Ahorro")
    deudas = models.IntegerField(label="Pago de deudas")

    #Esacala Likert
    offer_1 = models.IntegerField(widget=widgets.RadioSelect, choices=[
                                  1, 2, 3, 4, 5, 6, 7, 8, 9, 10], label="")

    Estabilidad = models.IntegerField(choices=[
                                      1, 2, 3, 4, 5], label='Mantenerse invariable o inalterable en el mismo lugar, estado o situación.')
    Independencia = models.IntegerField(
        choices=[1, 2, 3, 4, 5], label='Autonomía de tomar las decisiones propias.')
    Descanso = models.IntegerField(
        choices=[1, 2, 3, 4, 5], label='Reposar fuerzas a través de un estado inactivo')
    Lucro = models.IntegerField(
        choices=[1, 2, 3, 4, 5], label='Ganancia o provecho de algún actividad u objeto.')
    Protección = models.IntegerField(
        choices=[1, 2, 3, 4, 5], label='Seguridad o respaldo frente a un acontecimiento.')

    encuesta_tabla1_pregunta1 = make_field(
        'Por lo general, cuando consigo lo que quiero es porque me he esforzado por lograrlo.')
    encuesta_tabla1_pregunta2 = make_field(
        'Cuando hago planes estoy casi seguro (a) que conseguiré que lleguen a buen término.')
    encuesta_tabla1_pregunta3 = make_field(
        'Prefiero los juegos que entrañan algo de suerte que los que sólo requieren habilidad.')
    encuesta_tabla1_pregunta4 = make_field(
        'Si me lo propongo, puedo aprender casi cualquier cosa.')
    encuesta_tabla1_pregunta5 = make_field(
        'Mis mayores logros se deben más que nada a mi trabajo arduo y a mi capacidad.')
    encuesta_tabla1_pregunta6 = make_field(
        'Por lo general no establezco metas porque se me dificulta mucho hacer lo necesario para alcanzarlas.')
    encuesta_tabla1_pregunta7 = make_field(
        'La competencia desalienta la excelencia.')
    encuesta_tabla1_pregunta8 = make_field(
        'Las personas a menudo salen adelante por pura suerte.')
    encuesta_tabla1_pregunta9 = make_field(
        'En cualquier tipo de examen o competencia me gusta comparar mis calificaciones con las de los demás.')
    encuesta_tabla1_pregunta10 = make_field(
        'Pienso que no tiene sentido empeñarme en trabajar en algo que es demasiado difícil para mí.')

    encuesta_tabla2_pregunta1 = make_field(
        'Podré alcanzar la mayoría de los objetivos que me he propuesto.')
    encuesta_tabla2_pregunta2 = make_field(
        'Cuando me enfrento a tareas difíciles, estoy seguro de que las cumpliré.')
    encuesta_tabla2_pregunta3 = make_field(
        'En general, creo que puedo obtener resultados que son importantes para mí.')
    encuesta_tabla2_pregunta4 = make_field(
        'Creo que puedo tener éxito en cualquier esfuerzo que me proponga.')
    encuesta_tabla2_pregunta5 = make_field(
        'Seré capaz de superar con éxito muchos desafíos.')
    encuesta_tabla2_pregunta6 = make_field(
        'Confío en que puedo realizar eficazmente muchas tareas diferentes.')
    encuesta_tabla2_pregunta7 = make_field(
        'Comparado con otras personas, puedo hacer la mayoría de las tareas muy bien.')
    encuesta_tabla2_pregunta8 = make_field(
        'Incluso cuando las cosas son difíciles, puedo realizarlas bastante bien.')
    encuesta_tabla2_pregunta9 = make_field(
        'Podré alcanzar la mayoría de los objetivos que me he propuesto.')

    encuesta_tabla3_pregunta1 = make_field2('Llegar tarde a una cita')
    encuesta_tabla3_pregunta2 = make_field2('Comprar a vendedores ambulantes')
    encuesta_tabla3_pregunta3 = make_field2('Tirar basura en la calle')
    encuesta_tabla3_pregunta4 = make_field2(
        'Trabajar y recibir un pago sin que haya firmado un contrato formal (pintar una casa, realizar un reporte, etc.)')
    encuesta_tabla3_pregunta5 = make_field2(
        'Silbar o decirle un piropo a un (a) desconocido (a) en la calle')
    encuesta_tabla3_pregunta6 = make_field2(
        'Darle trabajo a alguien y pagarle sin pedirle que firme un contrato formal (pintar una casa, realizar un reporte, etc.)')
    encuesta_tabla3_pregunta7 = make_field2(
        'Consumir cerveza, aguardiente, ron u otras bebidas alcohólicas en un andén o parque')
    encuesta_tabla3_pregunta8 = make_field2(
        'No cotizar al sistema de pensiones')
    encuesta_tabla3_pregunta9 = make_field2('No aportar al sistema de salud')
    encuesta_tabla3_pregunta10 = make_field2(
        'No ceder un asiento preferente a una embarazada o un(a) anciano(a) se sube al bus')
    encuesta_tabla3_pregunta11 = make_field2('Colarse en las filas')
    encuesta_tabla3_pregunta12 = make_field2('No tener cuenta bancaria')
    encuesta_tabla3_pregunta13 = make_field2(
        'Pedir dinero prestado a prestamistas informales (ejemplo: gota a gota)')
    encuesta_tabla3_pregunta14 = make_field2(
        'No recoger los desechos de las mascotas')
    encuesta_tabla3_pregunta15 = make_field2(
        'Usar transportes alternativos como piratas o mototaxis')
    encuesta_tabla3_pregunta16 = make_field2(
        'Vender cosas o hacer negocios de manera informal')
    encuesta_tabla3_pregunta17 = make_field2(
        'Usar plataformas de transporte como Uber, Didi, etc.')
    encuesta_tabla3_pregunta18 = make_field2('No votar')
    encuesta_tabla3_pregunta19 = make_field2(
        'Ir a eventos políticos para conseguir empleo/beneficios personales')
    encuesta_tabla3_pregunta20 = make_field2(
        'Comprar réplicas de productos originales (lociones, bolsos, zapatos, camisas)')
    encuesta_tabla3_pregunta21 = make_field2('Comprar productos sin factura')
    encuesta_tabla3_pregunta22 = make_field2('Subarrendar una habitación')
    encuesta_tabla3_pregunta23 = make_field2(
        'Vivir en una habitación subarrendada')
    encuesta_tabla3_pregunta24 = make_field2(
        'No usar el paso cebra o los puentes peatonales para cruzar una calle')
    encuesta_tabla3_pregunta25 = make_field2(
        'Cruzar caminando una calle cuando el semáforo peatonal está en rojo')
    encuesta_tabla3_pregunta26 = make_field2(
        'Circular en bicicleta por el andén (no usar la cicloruta)')

# ******************************************************************************************************************** #
# *** Acceder al otro jugador
# ******************************************************************************************************************** #

    def other_player(self):
        # self.get_others_in_group() -> Vector[<Player  2>, <Player  3>, <Player  4>]
        return self.get_others_in_group()[0]
