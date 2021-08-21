from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from mpl.config import *
import random
from random import randrange
from django import forms 
import math

author = 'Ricardo Diaz Rincon'

doc = """
Experimento 1.
"""


# ******************************************************************************************************************** #
# *** CLASS SUBSESSION
# ******************************************************************************************************************** #
class Subsession(BaseSubsession):

    def creating_session(self):
        if self.round_number == 1:

            n = Constants.num_choices
            for p in self.get_players():

                # create list of lottery indices
                # ----------------------------------------------------------------------------------------------------
                indices = [j for j in range(1, n)]
                indices.append(n) if Constants.certain_choice else None

                # create list of probabilities
                # ----------------------------------------------------------------------------------------------------
                if Constants.percentage:
                    probabilities = [
                        # "{0:.2f}".format((k-1) / (n-1) * 100) + "%"
                        (n-k)
                        for k in indices
                    ]
                else:
                    probabilities = [
                        str(k-1) + "/" + str(n-1)
                        for k in indices
                    ]

                # create list corresponding to form_field variables including all choices
                # ----------------------------------------------------------------------------------------------------
                form_fields = ['choice_' + str(k) for k in indices]
                #form_fields = ['choice_1', 'choice_2', 'choice_3', 'choice_4', 'choice_5', 'choice_6', 'choice_7', 'choice_8', 'choice_9', 'choice_10', 'choice_11']

                # create list of choices
                # ----------------------------------------------------------------------------------------------------
                p.participant.vars['mpl_choices'] = list(
                    zip(indices, form_fields, probabilities)
                )
                #p.participant.vars= [(1, 'choice_1', '0/10'), (2, 'choice_2', '1/10'), (3, 'choice_3', '2/10'), (4, 'choice_4', '3/10'), (5, 'choice_5', '4/10'), (6, 'choice_6', '5/10'), (7, 'choice_7', '6/10'), (8, 'choice_8', '7/10'), (9, 'choice_9', '8/10'), (10, 'choice_10', '9/10'), (11, 'choice_11', '10/10')]
                # randomly determine index/choice of binary decision to pay
                # ----------------------------------------------------------------------------------------------------
                p.participant.vars['mpl_index_to_pay'] = random.choice(indices) #Return a random indice 1-11. It0s the election that will pay the person. That was the winner
                p.participant.vars['mpl_choice_to_pay'] = 'choice_' + str(p.participant.vars['mpl_index_to_pay']) #-> choice_(random number). Same numer of the last line
                # randomize order of lotteries if <random_order = True>
                # ----------------------------------------------------------------------------------------------------
                if Constants.random_order:
                    random.shuffle(p.participant.vars['mpl_choices']) #Randomize choices dict
                # initiate list for choices made
                # ----------------------------------------------------------------------------------------------------
                p.participant.vars['mpl_choices_made'] = [None for j in range(1, n + 1)]
                #p.participant.vars['mpl_choices_made'] = [None, None, None, None, None, None, None, None, None, None, None]
            # generate random switching point for PlayerBot in tests.py
            # --------------------------------------------------------------------------------------------------------
            for participant in self.session.get_participants():
                participant.vars['mpl_switching_point'] = random.randint(1, n) #Only used for testing


# ******************************************************************************************************************** #
# *** CLASS GROUP
# ******************************************************************************************************************** #
class Group(BaseGroup):
    pass


# ******************************************************************************************************************** #
# *** CLASS PLAYER
# ******************************************************************************************************************** #
class Player(BasePlayer):

    # add model fields to class player
    # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    if Constants.certain_choice: #Useless
        for j in range(1, Constants.num_choices + 1):
            locals()['choice_' + str(j)] = models.StringField()
        del j
    else:
        for j in range(1, Constants.num_choices):
            locals()['choice_' + str(j)] = models.StringField()
        del j

    random_draw = models.IntegerField()
    choice_to_pay = models.StringField()
    option_to_pay = models.StringField()
    inconsistent = models.IntegerField()
    switching_row = models.IntegerField()
    ball = models.StringField()
    # ******************************************************************************************************************** #
# *** Variables Consentimiento
# ******************************************************************************************************************** #
    num_temporal = models.IntegerField(label= "Por favor, ingrese el numero de identificación temporal que le llegó en el correo de invitación")
    accepts_terms = models.BooleanField()
    # ******************************************************************************************************************** #
# *** Variables Riesgo
# ******************************************************************************************************************** #
    monto = models.IntegerField(label = 
    "Por favor, indica el monto que invertirás en el activo de riesgo (sin puntos o comas)", min=0, max=10000)
    pago_total = models.IntegerField()
    # ******************************************************************************************************************** #
# *** Variables Priming
# ******************************************************************************************************************** #
    nombre_entidad = models.StringField(
        label= "¿Cuál es el nombre de la entidad en la que usted trabaja?",
        choices = [
            ["Universidad del Valle", "Universidad del Valle"],
            ["Corporación Universitaria Minuto de Dios", "Corporación Universitaria Minuto de Dios"],
            ["Universidad de Ibagué", "Universidad de Ibagué"],
            ["Universidad del Rosario", "Universidad del Rosario"],
            ["Universidad de Antioquia", "Universidad de Antioquia"],
            ["Universidad del Quindío", "Universidad del Quindío"],
            ["Universidad Autónoma Latinoamericana", "Universidad Autónoma Latinoamericana"]],
        widget=widgets.RadioSelect
        #widget=widgets.CheckboxInput
        #widget=widgets.RadioSelectHorizontal
    )
    tiempo_entidad = models.IntegerField(label="¿Cuánto tiempo (en años) lleva trabajando en esta entidad?")
    tipo_contrato =  models.StringField(
        label="Por favor, seleccione cuál es el tipo de contrato que lo vincula a esta entidad",
        choices = [
            ["Contrato a término indefinido", "Contrato a término indefinido"],
            ["Contrato a término fijo", "Contrato a término fijo"],
            ["Contrato de obra o labor", "Contrato de obra o labor"],
            ["Contrato por prestación de servicios", "Contrato por prestación de servicios"],
            ["Contrato a término fijo", "Contrato a término fijo"],
        ],
        widget=widgets.RadioSelect
    )
    horas_semanales = models.IntegerField(label="Cuántas horas a la semana trabaja normalmente en este trabajo?")    
    rango_pago = models.StringField(
        label="¿Puede decirme en cuál de los siguientes rangos está el ingreso que usted gana al mes por su trabajo?",
        choices = [
            ["Menos de 205.000", "Menos de 205.000"],
            ["Entre 205.000 y 325.000", "Entre 205.000 y 325.000"],
            ["Entre 325.0001 y 440.000", "Entre 325.0001 y 440.000"],
            ["Entre 440.001 y 565.000", "Entre 440.001 y 565.000"],
            ["Entre 650.001 y 710.000", "Entre 650.001 y 710.000"],
            ["Entre 710.001 y 750.000", "Entre 710.001 y 750.000"],
            ["Entre 810.001 y 915.000", "Entre 810.001 y 915.000"],
            ["Entre 915.001 y 1.000.00", "Entre 915.001 y 1.000.00"],
            ["Entre 1.000.001 y 1.250.000", "Entre 1.000.001 y 1.250.000"],
            ["Entre 1.250.001 y 1.365.000", "Entre 1.250.001 y 1.365.000"],
            ["Entre 1.365.001 y 1.600.000", "Entre 1.365.001 y 1.600.000"],
            ["Entre 1.600.001 y 2.000.000", "Entre 1.600.001 y 2.000.000"],
            ["Entre 2.000.001 y 3.150.000", "Entre 2.000.001 y 3.150.000"],
            ["Más de 3.150.000", "Más de 3.150.000"],
        ],
        widget=widgets.RadioSelect
    )
    satisfecho_trabajo_actual = models.BooleanField(
        label = "¿Con su trabajo actual?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ],
        widget=widgets.RadioSelect
    )
    satisfecho_beneficios = models.BooleanField(
        label = "¿Con los beneficios y las prestaciones que recibe?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ],
        widget=widgets.RadioSelect
    )
    satisfecho_jornada = models.BooleanField(
        label = "¿Con su jornada laboral actual?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ],
        widget=widgets.RadioSelect
    )
    conforme_contrato = models.BooleanField(
        label = "¿Está conforme con su tipo de contrato?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ],
        widget=widgets.RadioSelect
    )
    empleo_estable = models.BooleanField(
        label = "¿Considera que su empleo actual es estable?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ],
        widget=widgets.RadioSelect
    )
    contrato_credito_vivienda = models.BooleanField(
        label = "¿Su tipo de contrato actual le permite acceder a créditos de vivienda?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ],
        widget=widgets.RadioSelect
    )
    contrato_credito_carro = models.BooleanField(
        label = "¿Su tipo de contrato actual le permite acceder a créditos para carro o educación?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ],
        widget=widgets.RadioSelect
    )
    # ******************************************************************************************************************** #
# *** Múltiples variables 1
# ******************************************************************************************************************** #
    recibe_prima =  models.BooleanField(
        label="Prima de navidad",
        widget=widgets.CheckboxInput,
        blank=True
    )
    recibe_cesantias =  models.BooleanField(
        label="Cesantias",
        widget=widgets.CheckboxInput,
        blank=True
    )
    recibe_vacaciones_sueldo =  models.BooleanField(
        label="Vacaciones con sueldo",
        widget=widgets.CheckboxInput,
        blank=True
    )
    # ******************************************************************************************************************** #
# *** Múltiples variables 2. Qué hace para la vejez?
# ******************************************************************************************************************** #
    aporte_pension = models.BooleanField(
        label="Aportar en un fondo de pensiones obligatorias",
        widget=widgets.CheckboxInput,
        blank = True
    )
    aporte_ahorro = models.BooleanField(
        label="Ahorrando",
        widget=widgets.CheckboxInput,
        blank = True
    )
    aporte_inversiones = models.BooleanField(
        label="Haciendo inversiones",
        widget=widgets.CheckboxInput,
        blank = True
    )
    aporte_seguro = models.BooleanField(
        label="Pagando un seguro por su cuenta",
        widget=widgets.CheckboxInput,
        blank = True
    )
    aporte_hijos_vejez = models.BooleanField(
        label="Preparando a sus hijos para que pueda mantenerlo en su vejez",
        widget=widgets.CheckboxInput,
        blank = True
    )
    aporte_otro = models.BooleanField(
        label="Otro",
        widget=widgets.CheckboxInput,
        blank = True
    )
    aporte_nada = models.BooleanField(
        label="Nada",
        widget=widgets.CheckboxInput,
        blank = True
    )
    # ******************************************************************************************************************** #
# *** Termina Múltiples variables 2.
# ******************************************************************************************************************** #
    cambiar_empresa = models.BooleanField(
        label = "¿Desearía trabajar en otra organización/empresa?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ],
        widget=widgets.RadioSelect
    )
    cambiar_trabajo = models.BooleanField(
        label = "¿Desea cambiar el tipo de trabajo que realiza actualmente?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ],
        widget=widgets.RadioSelect
    )
    # ******************************************************************************************************************** #
# *** Se despliegan cuando se responde a "sí" en la pregunta anterior. 
# La pregunta general sería: ¿Por qué motivos desea cambiar de trabajo o empleo?
# ******************************************************************************************************************** #
    mejorar_capacidades = models.BooleanField(
        label = "¿Para mejorar la utilización de sus capacidades o formación?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ],
        blank = True
    )
    mejorar_ingresos = models.BooleanField(
        label = "¿Desea mejorar sus ingresos?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ],
        blank = True
    )
    trabajar_menos = models.BooleanField(
        label = "¿Desea trabajar menos horas?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ],
        blank = True
    )
    trabajo_temporal = models.BooleanField(
        label = "¿Porque el trabajo actual es temporal?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ],
        blank = True
    )
    trabajo_estable = models.BooleanField(
        label = "¿Porque su trabajo no es estable?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ],
        blank = True
    )
    crecimiento_profesional = models.BooleanField(
        label = "¿Porque no ve posibilidades de crecimiento profesional?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ],
        blank = True
    )
    dinero_compra_vivienda = models.BooleanField(
        label = "¿Porque con el dinero que gana no puede realizar planes de compra de vivienda, carro o educación?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ],
        blank = True
    )
    contrato_compra_vivienda = models.BooleanField(
        label = "¿Porque su tipo de contrato no le permite realizar planes de compra de vivienda, carro o educación?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ],
        blank = True
    )
    problemas_companeros = models.BooleanField(
        label = "¿Problemas con sus compañeros de trabajo?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ],
        blank = True
    )
    problemas_jefe = models.BooleanField(
        label = "¿Problemas con su jefe?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ],
        blank = True
    )
    labor_desempenada = models.BooleanField(
        label = "¿Se siento a gusto o cómodo con la labor que desempeña?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ],
        blank = True
    )
    esfuerzo_fisico = models.BooleanField(
        label = "¿Su trabajo actual exige mucho esfuerzo físico o mental?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ],
        blank = True
    )
    problemas_ambientales = models.BooleanField(
        label = "¿Problemas ambientales (aire, olores, ruidos, temperatura, etc.)?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ],
        blank = True
    )
    otro_problema = models.BooleanField(
        label = "¿Otro?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ],
        blank = True
    )
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
# *** Preguntas Consejos (Tips)
# ******************************************************************************************************************** #
    pregunta_uno = models.StringField(
        label="¿A qué correo deberían solicitar dicha información?", 
    )
    pregunta_dos = models.StringField(
        label="¿A quién deberían dirigirse para que este problema se solucione? ", 
    )
    pregunta_tres = models.StringField(
        label="¿Con quién(es) debría comunicarse para poder tener acceso a lo que necesita?", 
    )
    pregunta_cuatro = models.StringField(
        label="¿Con quién debe comunicarse para solucionar este problema y por qué?", 
    )
    pregunta_cinco = models.StringField(
        label="¿Está ella en lo correcto? ¿Por qué?", 
    )
    pregunta_seis = models.StringField(
        label="¿A qué oficina los remitiría y por qué?", 
    )
    pregunta_siete = models.StringField(
        label="¿A quién(es) le deben preguntar y por qué?", 
    )
    # set player's payoff
    # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    def set_payoffs(self):

        # random draw to determine whether to pay the "high" or "low" outcome of the randomly picked lottery
        # Randomnly decides wheter to pay the high or low value
        # ------------------------------------------------------------------------------------------------------------
        self.random_draw = randrange(1, len(self.participant.vars['mpl_choices'])) #Selects rando number 1-11
        # set <choice_to_pay> to participant.var['choice_to_pay'] determined creating_session
        # ------------------------------------------------------------------------------------------------------------
        self.choice_to_pay = self.participant.vars['mpl_choice_to_pay'] 
        #self.choice_to_pay = choice_(random number 1-11). Here the choce is selected

        # elicit whether lottery "A" or "B" was chosen for the respective choice
        # ------------------------------------------------------------------------------------------------------------
        self.option_to_pay = getattr(self, self.choice_to_pay)
        #self.option_to_pay = A or B. Here the lottery is selected
        

        # set player's payoff
        # ------------------------------------------------------------------------------------------------------------
        print("Choice to play model" + str(self.choice_to_pay))
        print(self.option_to_pay)
        print(self.random_draw)
        print(self.participant.vars['mpl_index_to_pay'])
        if self.option_to_pay == 'A': #A Toma la opción a ganar y la compara con con un número aleatorio. Si es menor escoge el mayor pago
            if self.random_draw <= self.participant.vars['mpl_index_to_pay']:
                self.payoff = Constants.lottery_a_hi
                self.ball = "Azul"
            else:
                self.payoff = Constants.lottery_a_lo
                self.ball = "Rosada"
        else:
            if self.random_draw <= self.participant.vars['mpl_index_to_pay']:
                self.payoff = Constants.lottery_b_hi
                self.ball = "Azul"
            else:
                self.payoff = Constants.lottery_b_lo
                self.ball = "Rosada"
        print("Salió la pelota" + self.ball)
        # set payoff as global variable
        # ------------------------------------------------------------------------------------------------------------
        self.participant.vars['mpl_payoff'] = self.payoff

    # determine consistency
    # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    def set_consistency(self):

        n = Constants.num_choices

        # replace A's by 1's and B's by 0's
        self.participant.vars['mpl_choices_made'] = [
            1 if j == 'A' else 0 for j in self.participant.vars['mpl_choices_made']
        ]
        print("Choices Model" + str(self.participant.vars['mpl_choices_made']))
        # check for multiple switching behavior
        for j in range(1, n):
            choices = self.participant.vars['mpl_choices_made']
            self.inconsistent = 1 if choices[j] > choices[j - 1] else 0
            if self.inconsistent == 1:
                break

    # determine switching row
    # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    def set_switching_row(self):

        # set switching point to row number of first 'B' choice
        if self.inconsistent == 0:
            self.switching_row = sum(self.participant.vars['mpl_choices_made']) + 1

    def set_total_payoff(self):
        self.pago_total = math.trunc(self.payoff) + self.monto + 20000
