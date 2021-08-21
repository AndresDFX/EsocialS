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

import math

author = 'Ricardo Diaz Rincon'

doc = """
Experimento 2
"""


class Constants(BaseConstants):
    name_in_url = 'lideres_sociales'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
     # ******************************************************************************************************************** #
# *** Variables Consentimiento
# ******************************************************************************************************************** #
    num_temporal = models.IntegerField(label= "Por favor, ingrese el numero de identificación temporal que le llegó en el correo de invitación")
    accepts_terms = models.BooleanField()
    tratamiento = models.StringField()
    # ******************************************************************************************************************** #
# *** Variables Cuestionario
# ******************************************************************************************************************** #
    calidad_noticia = models.StringField(
        label="En términos generales, la calidad de la noticia es buena.",
        choices = [
            ["Totalmente en acuerdo", "Totalmente en acuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ni en desacuerdo, ni en acuerdo", "Ni en desacuerdo, ni en acuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Totalmente de acuerdo", "Totalmente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    informacion_noticia = models.StringField(
        label="La noticia proporciona información precisa y exacta.",
        choices = [
            ["Totalmente en acuerdo", "Totalmente en acuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ni en desacuerdo, ni en acuerdo", "Ni en desacuerdo, ni en acuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Totalmente de acuerdo", "Totalmente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    noticia_incompleta = models.StringField(
        label="La información de la noticia está incompleta.",
        choices = [
            ["Totalmente en acuerdo", "Totalmente en acuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ni en desacuerdo, ni en acuerdo", "Ni en desacuerdo, ni en acuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Totalmente de acuerdo", "Totalmente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    noticia_credibilidad = models.StringField(
        label="La noticia proporciona información creíble.",
        choices = [
            ["Totalmente en acuerdo", "Totalmente en acuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ni en desacuerdo, ni en acuerdo", "Ni en desacuerdo, ni en acuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Totalmente de acuerdo", "Totalmente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    noticia_tiempo = models.StringField(
        label="El tiempo de duración de la noticia es adecuado.",
        choices = [
            ["Totalmente en acuerdo", "Totalmente en acuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ni en desacuerdo, ni en acuerdo", "Ni en desacuerdo, ni en acuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Totalmente de acuerdo", "Totalmente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    noticia_calidad = models.StringField(
        label="La información transmitida goza de calidad informativa.",
        choices = [
            ["Totalmente en acuerdo", "Totalmente en acuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ni en desacuerdo, ni en acuerdo", "Ni en desacuerdo, ni en acuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Totalmente de acuerdo", "Totalmente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    noticia_imagenes = models.StringField(
        label="Las imágenes usadas son las más adecuadas en relación con la noticia.",
        choices = [
            ["Totalmente en acuerdo", "Totalmente en acuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ni en desacuerdo, ni en acuerdo", "Ni en desacuerdo, ni en acuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Totalmente de acuerdo", "Totalmente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    noticia_publico_general = models.StringField(
        label="La noticia proporciona información que debe ser conocida por el público en general.",
        choices = [
            ["Totalmente en acuerdo", "Totalmente en acuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ni en desacuerdo, ni en acuerdo", "Ni en desacuerdo, ni en acuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Totalmente de acuerdo", "Totalmente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    noticia_informacion_importante = models.StringField(
        label="La noticia proporciona información que debo saber.",
        choices = [
            ["Totalmente en acuerdo", "Totalmente en acuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ni en desacuerdo, ni en acuerdo", "Ni en desacuerdo, ni en acuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Totalmente de acuerdo", "Totalmente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    noticia_informacion_importante_politicos = models.StringField(
        label="La noticia proporciona información que debe ser conocida por los dirigentes políticos.",
        choices = [
            ["Totalmente en acuerdo", "Totalmente en acuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ni en desacuerdo, ni en acuerdo", "Ni en desacuerdo, ni en acuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Totalmente de acuerdo", "Totalmente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    noticia_lenguaje = models.StringField(
        label="El lenguaje usado para informar es correcto.",
        choices = [
            ["Totalmente en acuerdo", "Totalmente en acuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ni en desacuerdo, ni en acuerdo", "Ni en desacuerdo, ni en acuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Totalmente de acuerdo", "Totalmente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    noticia_lideres_similar = models.StringField(
        label="Las noticias sobre el asesinato de líderes sociales son similares a la que acabo de ver.",
        choices = [
            ["Totalmente en acuerdo", "Totalmente en acuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ni en desacuerdo, ni en acuerdo", "Ni en desacuerdo, ni en acuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Totalmente de acuerdo", "Totalmente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    # ******************************************************************************************************************** #
# *** Variables Cuestionario - 2
# ******************************************************************************************************************** #
    noticia_impactante = models.StringField(
        label="¿Usted cree que esta noticia es impactante?",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    noticia_angustiante = models.StringField(
        label="¿Esta noticia te hace sentir angustiado?",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    noticia_violenta = models.StringField(
        label="¿Cree que los eventos descritos en esta noticia son demasiado violentos?",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    lider_necesario = models.StringField(
        label="¿Usted cree que este líder era necesario para su comunidad?",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    acuerdo_paz = models.StringField(
        label="¿Cree que las consecuencias del conflicto armado han cesado después de la firma del Acuerdo de Paz?",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    gobierno_responsable_lideres = models.StringField(
        label="¿En general, ¿Cree que el gobierno es responsable de la agresión a líderes sociales?",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    conflicto_armado_cesado = models.StringField(
        label="¿Cree que las consecuencias del conflicto armado han cesado después de la firma del Acuerdo de Paz?",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
     # ******************************************************************************************************************** #
# *** Variables Cuestionario - 3
# ******************************************************************************************************************** #
    frase_identificado_1 = models.StringField(
        label="¿Por favor, elija la frase con la que se sienta más identificado:",
        choices = [
            ["Cosas como esta suceden todo el tiempo y no me molesto cada vez que leo sobre ello.", "Cosas como esta suceden todo el tiempo y no me molesto cada vez que leo sobre ello."],
            ["Cosas como esta son muy raras y me molesto cada vez que leo sobre ellas.", "Cosas como esta son muy raras y me molesto cada vez que leo sobre ellas."],
        ],
        widget=widgets.RadioSelect,
    )
    frase_identificado_2 = models.StringField(
        label="¿Por favor, elija la frase con la que se sienta más identificado:",
        choices = [
            ["Cuando leo una historia como esta, me resulta difícil sacarla de mi mente.", "Cuando leo una historia como esta, me resulta difícil sacarla de mi mente."],
            ["Cuando leo una historia como esta, usualmente soy capaz de olvidarla poco después.", "Cuando leo una historia como esta, usualmente soy capaz de olvidarla poco después."],
        ],
        widget=widgets.RadioSelect,
    )
    frase_identificado_3 = models.StringField(
        label="¿Por favor, elija la frase con la que se sienta más identificado:",
        choices = [
            ["Leer esta historia no afecta mucho mis emociones.", "Leer esta historia no afecta mucho mis emociones."],
            ["Leer esta historia tiene un profundo efecto emocional en mí.", "Leer esta historia tiene un profundo efecto emocional en mí."],
        ],
        widget=widgets.RadioSelect,
    )
    # ******************************************************************************************************************** #
# *** Variables Cuestionario - 4
# ******************************************************************************************************************** #
    victima_responsable = models.StringField(
        label="La víctima fue responsable de su propia agresión porque se involucró en problemáticas violentas",
        choices = [
            ["Totalmente en desacuerdo", "Totalmente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ni en desacuerdo, ni en acuerdo", "Ni en desacuerdo, ni en acuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Totalmente de acuerdo", "Totalmente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    siente_compasion = models.StringField(
        label="Después de escuchar los hechos del caso, sentí cierta compasión por la víctima",
        choices = [
            ["Totalmente en desacuerdo", "Totalmente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ni en desacuerdo, ni en acuerdo", "Ni en desacuerdo, ni en acuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Totalmente de acuerdo", "Totalmente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    # ******************************************************************************************************************** #
# *** Variables Cuestionario - 5
# ******************************************************************************************************************** #
    entristece_persona_solitaria = models.StringField(
        label="Me entristece ver a una persona solitaria en un grupo",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    importancia_sentimientos = models.StringField(
        label="La gente le da demasiada importancia a los sentimientos y a la sensibilidad de los animales",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    muestras_afecto = models.StringField(
        label="A menudo encuentro molestas las muestras de afecto en público",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    molestan_personas_infelices = models.StringField(
        label="Me molestan las personas infelices que se compadecen de sí mismas.",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    ponerse_nervioso = models.StringField(
        label="Me pongo nervioso si los demás a mi alrededor parecen estarlo.",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    llorar_felicidad = models.StringField(
        label="Me parece una tontería que la gente llore de felicidad.",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    involucrarse_emocionalmente = models.StringField(
        label="Tiendo a involucrarme emocionalmente con los problemas de un amigo",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    cancion_conmueve = models.StringField(
        label="A veces las palabras de una canción de amor pueden conmoverme profundamente",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    perder_control_malas_noticias = models.StringField(
        label="Tiendo a perder el control cuando le traigo malas noticias a la gente",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    gente_influencia_estado_animo = models.StringField(
        label="La gente que me rodea tiene una gran influencia en mi estado de ánimo.",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    extrajeros_geniales = models.StringField(
        label="La mayoría de los extranjeros que he conocido parecían geniales y poco emotivos",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    trabajador_social = models.StringField(
        label="Prefiero ser un trabajador social que trabajar en un centro de formación profesional.",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    enfado_amigo = models.StringField(
        label="No me enfado sólo porque un amigo esté actuando molesto.",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    abrir_regalos = models.StringField(
        label="Me gusta ver a la gente abrir regalos.",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    gente_solitaria_no_amistosa = models.StringField(
        label="La gente solitaria probablemente no sea amistosa",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    llorar_molesta = models.StringField(
        label="Ver a la gente llorar me molesta.",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    canciones_feliz = models.StringField(
        label="Algunas canciones me hacen feliz.",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    sentimientos_personajes_novela = models.StringField(
        label="Realmente me involucro con los sentimientos de los personajes de una novela.",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    enfado_maltrato = models.StringField(
        label="Me enfado mucho cuando veo a alguien siendo maltratado.",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    mantener_calma = models.StringField(
        label="Soy capaz de mantener la calma aunque los que me rodean se preocupen.",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    amigo_problemas = models.StringField(
        label="Cuando un amigo empieza a hablar de sus problemas, trato de dirigir la conversación hacia otra cosa.",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    risa_otro = models.StringField(
        label="La risa de otro no es contagiosa para mí.",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    llanto_divierte = models.StringField(
        label="A veces en el cine me divierte la cantidad de llanto y sollozos que hay a mi alrededor.",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    decisiones_sin_sentimientos = models.StringField(
        label="Soy capaz de tomar decisiones sin ser influenciado por los sentimientos de la gente.",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    gente_deprimida_alrededor = models.StringField(
        label="No puedo seguir sintiéndome bien si la gente a mi alrededor está deprimida.",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    irritar_gente = models.StringField(
        label="Es difícil para mí ver cómo algunas cosas molestan tanto a la gente.",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    disgusto_animal_sufriendo = models.StringField(
        label="Me disgusta mucho cuando veo a un animal sufriendo.",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    involucrarse_libros_tonto = models.StringField(
        label="Involucrarse en libros o películas es un poco tonto.",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    ancianos_indefensos = models.StringField(
        label="Me molesta ver a los ancianos indefensos.",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    irrita_lagrimas_otros = models.StringField(
        label="Me irrita más que compadecerme cuando veo las lágrimas de alguien..",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    involucrar_pelicula = models.StringField(
        label="Me involucro mucho cuando veo una película.",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    mantener_calma_emocion = models.StringField(
        label="A menudo descubro que puedo mantener la calma a pesar de la emoción que me rodea.",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
    )
    ninos_lloran_sin_razon = models.StringField(
        label="Los niños pequeños a veces lloran sin razón aparente.",
        choices = [
            ["Sí", "Sí"],
            ["No", "No"],
        ],
        widget=widgets.RadioSelect,
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
    contador_masculino = models.IntegerField(initial=0)
    contador_femenino = models.IntegerField(initial=0)
    edad = models.IntegerField(label="¿Cuántos años cumplidos tiene usted?")
    ciudad = models.StringField(label="¿En qué ciudad vive actualmente?")
    estrato = models.IntegerField(label="¿Cuál es el estrato de la vivienda en la cual habita actualmente?", min=0, max=6)
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
        widget=widgets.RadioSelect,
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
        widget=widgets.RadioSelect,
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
        widget=widgets.RadioSelect,
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
        widget=widgets.RadioSelect,
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
# *** Variables Preguntas especificas (victima de violencia grupos armados)
# ******************************************************************************************************************** #
    victima_violencia_farc_eln = models.StringField(
        label="¿Ha sido testigo o víctima de algún tipo de violencia impartida por las FARC, ELN o alguna guerrilla?",
        choices = [
            ["Nunca", "Nunca"],
            ["Una vez ", "Una vez "],
            ["Entre 2 y 3 veces", "Entre 2 y 3 veces"],
            ["Más de 3 veces", "Más de 3 veces"],
            ["No sabe", "No sabe"],
        ],
        widget=widgets.RadioSelect,
    )
    victima_violencia_auc_otros = models.StringField(
        label="¿Ha sido testigo o víctima de algún tipo de violencia impartida por las AUC o otros grupos paramilitares?",
        choices = [
            ["Nunca", "Nunca"],
            ["Una vez ", "Una vez "],
            ["Entre 2 y 3 veces", "Entre 2 y 3 veces"],
            ["Más de 3 veces", "Más de 3 veces"],
            ["No sabe", "No sabe"],
        ],
        widget=widgets.RadioSelect,
    )
    victima_violencia_otros_delicuencia = models.StringField(
        label="¿Ha sido testigo o víctima de algún tipo de violencia impartida por otros grupos de delincuencia común?",
        choices = [
            ["Nunca", "Nunca"],
            ["Una vez ", "Una vez "],
            ["Entre 2 y 3 veces", "Entre 2 y 3 veces"],
            ["Más de 3 veces", "Más de 3 veces"],
            ["No sabe", "No sabe"],
        ],
        widget=widgets.RadioSelect,
    )
    victima_no_violencia = models.StringField(
        label="¿Ha sido testigo o víctima de robo, hurto, extorsión u otro crimen que no haya incluido violencia?",
        choices = [
            ["Nunca", "Nunca"],
            ["Una vez ", "Una vez "],
            ["Entre 2 y 3 veces", "Entre 2 y 3 veces"],
            ["Más de 3 veces", "Más de 3 veces"],
            ["No sabe", "No sabe"],
        ],
        widget=widgets.RadioSelect,
    )
    familia_victima_farc_eln = models.StringField(
        label="¿Alguien en su familia o entorno cercano ha sido testigo o víctima de algún tipo de violencia impartida por las FARC, ELN o alguna guerrilla?",
        choices = [
            ["Nunca", "Nunca"],
            ["Una vez ", "Una vez "],
            ["Entre 2 y 3 veces", "Entre 2 y 3 veces"],
            ["Más de 3 veces", "Más de 3 veces"],
            ["No sabe", "No sabe"],
        ],
        widget=widgets.RadioSelect,
    )
    familia_victima_auc_otros = models.StringField(
        label="¿Alguien en su familia o entorno cercano ha sido testigo o víctima de algún tipo de violencia impartida por las AUC u otros grupos paramilitares?",
        choices = [
            ["Nunca", "Nunca"],
            ["Una vez ", "Una vez "],
            ["Entre 2 y 3 veces", "Entre 2 y 3 veces"],
            ["Más de 3 veces", "Más de 3 veces"],
            ["No sabe", "No sabe"],
        ],
        widget=widgets.RadioSelect,
    )
    familia_victima_otros_delincuencia = models.StringField(
        label="¿Alguien en su familia o entorno cercano ha sido testigo o víctima de algún tipo de violencia impartida por otros grupos de delincuencia común?",
        choices = [
            ["Nunca", "Nunca"],
            ["Una vez ", "Una vez "],
            ["Entre 2 y 3 veces", "Entre 2 y 3 veces"],
            ["Más de 3 veces", "Más de 3 veces"],
            ["No sabe", "No sabe"],
        ],
        widget=widgets.RadioSelect,
    )
    familia_victima_no_violencia = models.StringField(
        label="¿Alguien en su familia o entorno cercano ha sido testigo o víctima de robo, hurto, extorsión u otro crimen que no haya incluido violencia?",
        choices = [
            ["Nunca", "Nunca"],
            ["Una vez ", "Una vez "],
            ["Entre 2 y 3 veces", "Entre 2 y 3 veces"],
            ["Más de 3 veces", "Más de 3 veces"],
            ["No sabe", "No sabe"],
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
    # def set_contador(self):
    #     # print(self.genero)
    #     if self.genero == 'Masculino':
    #         self.contador_masculino +=  1
    #     else:
    #         self.contador_femenino +=  1
