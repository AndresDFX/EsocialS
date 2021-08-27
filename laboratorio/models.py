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
#
from random import shuffle
#import itertools
# Trabajar con fechas utilizando Python haremos uso de la librería datetime
from datetime import datetime, date, timedelta
import pytz

author = 'Victor Hugo Ortega Gomez'

doc = """
EL EFECTO DE LOS TIPOS DE CONTRATO EN EL CONSUMO: UN ANÁLISIS EXPERIMENTAL
"""
""
class Constants(BaseConstants):
    name_in_url = 'laboratorio'
    players_per_group = None
    num_rounds = 15

    #
    contrato_formal_fijo = 'Contrato formal a tiempo fijo'
    contrato_formal_indefinido = 'Contrato formal a tiempo indefinido'
    contrato_formal_servicios = 'Contrato formal por prestación de servicios'
    contrato_informal_fijo = 'Contrato informal a tiempo fijo'
    contrato_informal_indefinido = 'Contrato informal a tiempo indefinido'
    contrato_informal_servicios = 'Contrato informal por prestación de servicios'

    #
    texto1= "Los mercados de energía son mercados de productos básicos que se ocupan específicamente del comercio y el suministro de energía. El mercado de la energía puede referirse a un mercado de la electricidad, pero también puede referirse a otras fuentes de energía. Normalmente, el desarrollo energético es el resultado de un gobierno que crea una política energética que fomenta el desarrollo de una industria energética de manera competitiva.\n Hasta la década de 1970, cuando los mercados de energía experimentaron cambios drásticos, se caracterizaron por estructuras organizativas basadas en monopolios. La mayoría de las reservas de petróleo del mundo estaban controladas por the Seven Sisters. Las circunstancias cambiaron considerablemente en 1973 a medida que crecía la influencia de la OPEP y las repercusiones de la crisis del petróleo de 1973 afectaron a los mercados energéticos mundiales."
    texto2= "Los mercados de energía se han liberalizado en algunos países; están regulados por autoridades nacionales e internacionales (incluidos los mercados liberalizados) para proteger los derechos del consumidor y evitar oligopolios. Los reguladores incluyen la Comisión Australiana del Mercado de la Energía en Australia, la Autoridad del Mercado de la Energía en Singapur, la Comunidad de la Energía en Europa, reemplazando el Mercado Energético Regional de Europa Sudoriental y el mercado energético nórdico para los países nórdicos. Los miembros de la Unión Europea deben liberalizar sus mercados energéticos.\n Los reguladores buscan desalentar la volatilidad de los precios, reformar los mercados si es necesario y buscar evidencia de comportamiento anticompetitivo como la formación de un monopolio."
    texto3= "Los mercados de energía sustentan nuestras economías y nuestra vida diaria. Toda empresa y cada hogar necesita energía. Los mercados de energía están regulados en muchas partes del mundo. Los proveedores de energía disfrutan de un monopolio y las tarifas las fija el gobierno. Sin embargo, existe un fuerte impulso hacia la liberalización. En un mercado energético abierto, las leyes de la oferta y la demanda determinan el precio de la energía. Comprender cómo funcionan es necesario si quiere ser un comprador de energía exitoso y convertirse en un “emprendedor energético”.\n La desregulación no es la única fuerza transformadora que cambia el panorama de los mercados energéticos. La actual revolución de las energías renovables está remodelando toda la industria."
    texto4= "El análisis de los mercados energéticos mundiales es fundamental para comprender la fluctuación de los precios locales de la energía. La mayoría de los observadores del mercado están acostumbrados a observar el Medio Oriente, Venezuela o China para comprender qué impulsa el precio del petróleo. Pero el análisis de los mercados de gas natural o electricidad a menudo carece de esta perspectiva global. El aumento en el comercio de GNL ha provocado la convergencia de los precios del gas. Si desea saber qué está impulsando el precio de la gasolina, tendrá que mirar más allá de su mercado local.\n Dado que los precios se basan en gran medida en combustibles que se comercializan en todo el mundo, una perspectiva global puede proporcionar una visión más profunda de los fundamentos de la oferta y la demanda."
    texto5= "El ecoturismo está dirigido a turistas que desean experimentar el medio ambiente natural sin dañarlo o alterar sus hábitats. Es una forma de turismo que implica la visita de áreas naturales frágiles, vírgenes y relativamente tranquilas, concebida como una alternativa de bajo impacto y, a menudo, a pequeña escala al turismo de masas comercial estándar. Significa viajar responsablemente a áreas naturales, conservando el medio ambiente y mejorando el bienestar de la población local. Su propósito puede ser educar al viajero, proporcionar fondos para la conservación ecológica, beneficiar directamente el desarrollo económico y el empoderamiento político de las comunidades locales, o fomentar el respeto por las diferentes culturas y los derechos humanos."
    texto6= 'Según la Sociedad Internacional de Ecoturismo (TIES), el ecoturismo puede definirse como “viajes responsables a áreas naturales que conservan el medio ambiente, sustentan el bienestar de la población local e implican interpretación y educación”. Estos viajes se pueden crear gracias a una red internacional de personas, instituciones y la industria del turismo donde los turistas y los profesionales del turismo se educan sobre temas ecológicos.\n Al mismo tiempo, el Ecoturismo Nacional de Australia define el ecoturismo como "turismo ecológicamente sostenible con un enfoque principal en la experiencia de áreas naturales que fomenta el entendimiento, la apreciación y la conservación ambiental y cultural".'
    texto7= "Las ventajas que ofrece el ecoturismo a los viajeros son personales, pero sus efectos son generalizados. Al visitar áreas de impresionante belleza natural, ver animales en sus hábitats nativos y conocer a miembros de las comunidades locales, los viajeros pueden aumentar su conciencia sobre la importancia de conservar los recursos y evitar el desperdicio. Se les anima a vivir de manera más sostenible en casa y también pueden aumentar su comprensión y sensibilidad hacia otras culturas. Además, los viajeros aprenden cómo ayudar a apoyar a otras comunidades, no entregando obsequios como juguetes y papelería, sino comprando productos y productos locales. Cuando los ecoturistas regresan a casa, transmiten el mensaje a sus familias, amigos y compañeros de trabajo.\n El ecoturismo permite a los países y comunidades construir sus economías sin dañar el medio ambiente, lo que significa que la vida silvestre local puede prosperar y los visitantes pueden disfrutar de destinos naturales."
    texto8= "Colombia es mundialmente famosa por su biodiversidad. Desde sus densas selvas, exuberantes selvas tropicales y playas de arena blanca hasta sus impresionantes cadenas montañosas e interminables desiertos y llanuras, el país está lleno de aves y animales raros. Los viajeros conscientes del medio ambiente pueden disfrutar del ecoturismo y los viajes de aventura de bajo impacto en Colombia y difundir estas especies.\n Los Andes colombianos albergan muchos de los ecosistemas más ricos e inusuales del país y el Parque Nacional Chingaza es uno de los mejores lugares para el ecoturismo en el país. Este enorme parque, cercano a la capital, Bogotá, se extiende en altitudes de 800 a 4.000 metros sobre el nivel del mar y es hogar de osos de anteojos, jaguares, pumas, monos lanudos, tucanes y el imponente cóndor andino."
    texto9= 'Una nebulosa es una nube gigante de polvo y gas en el espacio. Algunas nebulosas (más de una nebulosa) provienen del gas y el polvo arrojados por la explosión de una estrella moribunda, como una supernova. Otras nebulosas son regiones donde comienzan a formarse nuevas estrellas. Por esta razón, algunas nebulosas se denominan "viveros de estrellas". Las nebulosas están formadas por polvo y gases, principalmente hidrógeno y helio. El polvo y los gases en una nebulosa están muy dispersos, pero la gravedad puede comenzar a juntar lentamente acumulaciones de polvo y gas. A medida que estos grupos se hacen cada vez más grandes, su gravedad se vuelve cada vez más fuerte.\n Eventualmente, el grupo de polvo y gas se vuelve tan grande que colapsa por su propia gravedad. El colapso hace que el material en el centro de la nube se caliente, y este núcleo caliente es el comienzo de una estrella.'
    texto10= "Las nebulosas existen en el espacio entre las estrellas, también conocido como espacio interestelar. La nebulosa conocida más cercana a la Tierra se llama Nebulosa Helix. Es el remanente de una estrella moribunda, posiblemente una como el Sol. Se encuentra aproximadamente a 700 años luz de la Tierra. Eso significa que incluso si pudiera viajar a la velocidad de la luz, ¡aún le tomaría 700 años llegar allí!\n Los astrónomos usan telescopios muy poderosos para tomar fotografías de nebulosas lejanas. Telescopios espaciales como el Telescopio Espacial Spitzer de la NASA y el Telescopio Espacial Hubble han capturado muchas imágenes de nebulosas lejanas."
    texto11= "Una supernova ocurre cuando una estrella de gran masa llega al final de su vida. Cuando se detiene la fusión nuclear en el núcleo de la estrella, la estrella colapsa. El gas que cae hacia adentro rebota o se calienta con tanta fuerza que se expande hacia afuera desde el núcleo, lo que hace que la estrella explote. La capa de gas en expansión forma un remanente de supernova, una nebulosa difusa especial. Aunque gran parte de la emisión óptica y de rayos X de los remanentes de supernova se origina a partir de gas ionizado, una gran cantidad de la emisión de radio es una forma de emisión no térmica llamada emisión de sincrotrón. Esta emisión se origina a partir de electrones de alta velocidad que oscilan dentro de campos magnéticos."
    texto12= "PK164+31.1, conocida también como Jones-Emberson 1, es una nebulosa planetaria poco brillante que se encuentra a unos 1.600 años luz de distancia hacia la constelación del Lince (Lynx). Debido a su magnitud 17 es sólo visible en telescopios de tamaño considerable. Cerca del centro de la nebulosa se puede ver una estrella enana blanca azul caliente que es lo que queda del núcleo ya que el gas es expulsado en diferentes etapas al final de la vida de la estrella. La nebulosa en expansión se desvanecerá durante los próximos miles de años mientras la estrella central puede sobrevivir durante miles de millones de años"


class Subsession(BaseSubsession):

    #
    def creating_session(self):


        if self.round_number == 1:

            # pylint: disable=E1101
            self.session.vars['distribucion'] = [[12,7,1],[12,7,1]]

            self.session.vars['Contrato formal a tiempo fijo'] = [[0,0,0],[0,0,0]]
            self.session.vars['Contrato formal a tiempo indefinido'] = [[0,0,0],[0,0,0]]
            self.session.vars['Contrato formal por prestación de servicios'] = [[0,0,0],[0,0,0]]
            self.session.vars['Contrato informal a tiempo fijo'] = [[0,0,0],[0,0,0]]
            self.session.vars['Contrato informal a tiempo indefinido'] = [[0,0,0],[0,0,0]]
            self.session.vars['Contrato informal por prestación de servicios'] = [[0,0,0],[0,0,0]]

#40
            lista = 2 * [
            'Contrato formal a tiempo fijo',
            'Contrato formal a tiempo indefinido',
            'Contrato formal por prestación de servicios',
            'Contrato informal a tiempo fijo',
            'Contrato informal a tiempo indefinido',
            'Contrato informal por prestación de servicios']

            shuffle(lista)


            self.session.vars['treatments'] = lista

            # 'Contrato formal a tiempo fijo',
            #     'Contrato formal a tiempo indefinido',
            #     'Contrato formal por prestación de servicios',
            #     'Contrato informal a tiempo fijo',
            #     'Contrato informal a tiempo indefinido',
            #     'Contrato informal por prestación de servicios'



            # contratos = itertools.cycle([
            #     Constants.contrato_formal_fijo,
            #     Constants.contrato_formal_indefinido,
            #     Constants.contrato_formal_servicios,
            #     Constants.contrato_informal_fijo,
            #     Constants.contrato_informal_indefinido,
            #     Constants.contrato_informal_servicios
            # ])
            import itertools
            contratos = itertools.cycle([
                'Contrato formal a tiempo fijo',
                'Contrato formal a tiempo indefinido',
                'Contrato formal por prestación de servicios',
                'Contrato informal a tiempo fijo',
                'Contrato informal a tiempo indefinido',
                'Contrato informal por prestación de servicios'
            ])
            for p in self.get_players():
                p.participant.vars['contrato'] = next(contratos)
                # p.participant.vars['comparacion2'] = []


class Group(BaseGroup):
    pass

#
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

#
def make_field2(label):
    return models.IntegerField(
        choices=[-2,-1,0,1,2],
        label=label,
    )


class Player(BasePlayer):

    treatment = models.StringField()

    def set_treatment(self):
        print("")

    def live_treatment(self, data):
        disponible = False
        sexo = data['sexo']
        estrato = data['estrato']
        print("sexo:", sexo)
        print("estrato:", estrato)
        print('received a data from', ':', data)
        # pylint: disable=E1101

        print("antes ", self.treatment)


        for i in range (0,len(self.session.vars['treatments'])):
            contrato = self.session.vars['treatments'][i]
            print(contrato)



            if sexo == 'Mujer' and estrato >= 1 and estrato <= 2:
                print("condicion 1")
                if self.session.vars[contrato][0][0] <= 12:
                    print(self.session.vars[contrato][0][0])
                    self.session.vars[contrato][0][0] = self.session.vars[contrato][0][0] + 1
                    print(self.session.vars[contrato][0][0])
                    self.treatment = contrato
                    self.session.vars['treatments'].pop(i)
                    disponible = True
                    break

            elif sexo == 'Mujer' and estrato >= 3 and estrato <= 4:
                print("condicion 2")
                if self.session.vars[contrato][0][1] <= 7:
                    print(self.session.vars[contrato][0][1])
                    self.session.vars[contrato][0][1] = self.session.vars[contrato][0][1] + 1
                    print(self.session.vars[contrato][0][1])
                    self.treatment = contrato
                    self.session.vars['treatments'].pop(i)
                    disponible = True
                    break
            elif sexo == 'Mujer' and estrato >= 5 and estrato <= 6:
                print("condicion 3")
                if self.session.vars[contrato][0][2] <= 1:
                    print(self.session.vars[contrato][0][2])
                    self.session.vars[contrato][0][2] = self.session.vars[contrato][0][2] + 1
                    print(self.session.vars[contrato][0][2])
                    self.treatment = contrato
                    self.session.vars['treatments'].pop(i)
                    disponible = True
                    break
            elif sexo == 'Hombre' and estrato >= 1 and estrato <= 2:
                print("condicion 4")
                if self.session.vars[contrato][1][0] <= 12:
                    print(self.session.vars[contrato][1][0])
                    self.session.vars[contrato][1][0] = self.session.vars[contrato][1][0] + 1
                    print(self.session.vars[contrato][1][0])
                    self.treatment = contrato
                    self.session.vars['treatments'].pop(i)
                    disponible = True
                    break
            elif sexo == 'Hombre' and estrato >= 3 and estrato <= 4:
                print("condicion 5")
                if self.session.vars[contrato][1][1] <= 7:
                    print(self.session.vars[contrato][1][1])
                    self.session.vars[contrato][1][1] = self.session.vars[contrato][1][1] + 1
                    print(self.session.vars[contrato][1][1])
                    self.treatment = contrato
                    self.session.vars['treatments'].pop(i)
                    disponible = True
                    break
            elif sexo == 'Hombre' and estrato >= 5 and estrato <= 6:
                print("condicion 6")
                if self.session.vars[contrato][1][2] <= 1:
                    print(self.session.vars[contrato][1][2])
                    self.session.vars[contrato][1][2] = self.session.vars[contrato][1][2] + 1
                    print(self.session.vars[contrato][1][2])
                    self.treatment = contrato
                    self.session.vars['treatments'].pop(i)
                    disponible = True
                    break

     #   disponible = False
        return {0: disponible}

    def live_test(self, data):
        print('el dato es', data)
        print(self.actividad_2)
        inversion = data['inversion']
        if data['moneda'] == 'Cara':
            pago = inversion * 2 + (2000 - inversion)
            print('el pago de la actividad 2 es:', pago)
            self.payoff = c(pago)
        else:
            pago = inversion * 0 + (2000 - inversion)
            self.payoff = c(pago)
            print('el pago de la actividad 2 es:', pago)

    # Variables que contienen la fecha de inicio y las fechas de espera
    start_date = models.StringField() #get time of participant when welcome page is submitted
    next_date = models.StringField()
    date_after_next = models.StringField()

    # Funcion que determina las fechas de espera
    def get_time(self):
      #  self.starttime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        zona_horaria = datetime.now(pytz.timezone('America/Bogota'))
        fecha_actual = zona_horaria.date()
        cadena_fecha_actual = fecha_actual.strftime('%Y-%m-%d')
        fecha_siguiente = fecha_actual + timedelta(days=1)
        cadena_fecha_siguiente = fecha_siguiente.strftime('%Y-%m-%d')
        fecha_despues_siguiente = fecha_actual + timedelta(days=2)
        cadena_fecha_despues_siguiente = fecha_despues_siguiente.strftime('%Y-%m-%d')
        self.start_date = cadena_fecha_actual
        self.next_date =  cadena_fecha_siguiente
        self.date_after_next = cadena_fecha_despues_siguiente

    consentimiento = models.BooleanField(
        label='¿Autoriza el uso de los datos recolectados para futuros estudios (con previa autorización de un Comité)?',
        choices=[
            [True, "Sí"],
            [False, "No"],
        ],
        widget=widgets.RadioSelectHorizontal
    )

    sexo = models.StringField(
        blank=True,
        label='¿Cuál es su sexo? ',
        choices=['Mujer', 'Hombre'],
        widget= widgets.RadioSelect,
    )

    estrato = models.IntegerField(
        blank=True,
        label='¿Cuál es el estrato de la vivienda en la cual habita actualmente?',
        choices=[1,2,3,4,5,6],
        widget= widgets.RadioSelect,
    )

    terminos_actividad = models.BooleanField(
        label='¿Acepta los términos de esta actividad?',
        choices=[
            [True, "Sí"],
            [False, "No"],
        ],
        widget=widgets.RadioSelectHorizontal
    )

    codigo = models.StringField(label='Por favor, escriba el código de identificación que se les envió en el mensaje de la encuesta.')
    confirmacion_codigo = models.StringField(label='Por favor confirme el código de identificación')

    #
    texto_digitado1 = models.TextField(label='',)
    texto_digitado2 = models.TextField(label='',)
    texto_digitado3 = models.TextField(label='',)
    texto_digitado4 = models.TextField(label='',)
    texto_digitado5 = models.TextField(label='',)
    texto_digitado6 = models.TextField(label='',)
    texto_digitado7 = models.TextField(label='',)
    texto_digitado8 = models.TextField(label='',)
    texto_digitado9 = models.TextField(label='',)
    texto_digitado10 = models.TextField(label='',)
    texto_digitado11 = models.TextField(label='',)
    texto_digitado12 = models.TextField(label='',)

    porcentaje1 = models.DecimalField(max_digits=5, decimal_places=2)

    #Productos
    productos_alimentos = models.CurrencyField(initial=0)
    productos_snack = models.CurrencyField(initial=0)
    productos_aseo = models.CurrencyField(initial=0)
    productos_electronicos = models.CurrencyField(initial=0)
    productos_servicios = models.CurrencyField(initial=0)
    productos_transporte = models.CurrencyField(initial=0)
    productos_diversion = models.CurrencyField(initial=0)
    productos_ahorro = models.CurrencyField(initial=0)
    productos_deudas = models.CurrencyField(initial=0)

    productos_post_alimentos = models.CurrencyField(initial=0)
    productos_post_snack = models.CurrencyField(initial=0)
    productos_post_aseo = models.CurrencyField(initial=0)
    productos_post_electronicos = models.CurrencyField(initial=0)
    productos_post_servicios = models.CurrencyField(initial=0)
    productos_post_transporte = models.CurrencyField(initial=0)
    productos_post_diversion = models.CurrencyField(initial=0)
    productos_post_ahorro = models.CurrencyField(initial=0)
    productos_post_deudas = models.CurrencyField(initial=0)

    total = models.CurrencyField(initial=0)

    actividad_2 =  models.IntegerField(min=0, max=2000,label='Por favor, indica el monto que invertirás en el activo de riesgo')

    #Encuesta

    edad = models.IntegerField(label='¿Cuántos años cumplidos tiene?')
    ciudad = models.StringField(label='¿En qué ciudad vive actualmente?')

    rol_hogar = models.StringField(
        label='¿Cuál es su rol en su hogar? (Por favor, escoja una opción)',
        choices=['Padre / Madre', 'Espos@', 'Hij@', 'Otro']
    )

    estado_civil = models.StringField(
        label='¿Cuál es su estado civil? (Por favor, escoja una opción)',
        choices=['Soltero', 'casado', 'Unión libre', 'Divorciado', 'Viudo', 'Prefiero no decir']
    )

    hijos = models.IntegerField(label='¿Cuántos hijos tiene usted?')

    etnia = models.StringField(
        label='De acuerdo con su cultura o rasgos físicos, usted es o se reconoce como:(Por favor, escoja una opción)',
        choices=['Afrocolombiano', 'Indigena', 'Mestizo', 'Mulato', 'Blanco', 'Raizal del archipielago', 'Palenquero', 'Otro', 'Prefiero no decir']
    )

    religion = models.StringField(
        label='¿En cuál de los siguientes grupos se identifica usted?(Por favor, escoja una opción)',
        choices=['Católico', 'Cristiano', 'Testigo de Jehová', 'Ateo', 'Agnóstico', 'Judío', 'Musulmán', 'Hinduista', 'Otro', 'Prefiero no decir' ]
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
        choices=['Estudiar', 'Trabajar', 'Oficios del hogar', 'Buscar trabajo' ,'Otra actividad']
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
    diversion  = models.IntegerField(label="Diversión y ocio")
    ahorro = models.IntegerField(label="Ahorro")
    deudas = models.IntegerField(label="Pago de deudas")

    #Esacala Likert
    offer_1 = models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7,8,9,10], label= "")

    Estabilidad = models.IntegerField(choices=[1,2,3,4,5], label='Mantenerse invariable o inalterable en el mismo lugar, estado o situación.')
    Independencia = models.IntegerField(choices=[1,2,3,4,5], label='Autonomía de tomar las decisiones propias.')
    Descanso = models.IntegerField(choices=[1,2,3,4,5], label='Reposar fuerzas a través de un estado inactivo')
    Lucro = models.IntegerField(choices=[1,2,3,4,5], label='Ganancia o provecho de algún actividad u objeto.')
    Protección = models.IntegerField(choices=[1,2,3,4,5], label='Seguridad o respaldo frente a un acontecimiento.')

    encuesta_tabla1_pregunta1 = make_field('Por lo general, cuando consigo lo que quiero es porque me he esforzado por lograrlo.')
    encuesta_tabla1_pregunta2 = make_field('Cuando hago planes estoy casi seguro (a) que conseguiré que lleguen a buen término.')
    encuesta_tabla1_pregunta3 = make_field('Prefiero los juegos que entrañan algo de suerte que los que sólo requieren habilidad.')
    encuesta_tabla1_pregunta4 = make_field('Si me lo propongo, puedo aprender casi cualquier cosa.')
    encuesta_tabla1_pregunta5 = make_field('Mis mayores logros se deben más que nada a mi trabajo arduo y a mi capacidad.')
    encuesta_tabla1_pregunta6 = make_field('Por lo general no establezco metas porque se me dificulta mucho hacer lo necesario para alcanzarlas.')
    encuesta_tabla1_pregunta7 = make_field('La competencia desalienta la excelencia.')
    encuesta_tabla1_pregunta8 = make_field('Las personas a menudo salen adelante por pura suerte.')
    encuesta_tabla1_pregunta9 = make_field('En cualquier tipo de examen o competencia me gusta comparar mis calificaciones con las de los demás.')
    encuesta_tabla1_pregunta10 = make_field('Pienso que no tiene sentido empeñarme en trabajar en algo que es demasiado difícil para mí.')

    encuesta_tabla2_pregunta1 = make_field('Podré alcanzar la mayoría de los objetivos que me he propuesto.')
    encuesta_tabla2_pregunta2 = make_field('Cuando me enfrento a tareas difíciles, estoy seguro de que las cumpliré.')
    encuesta_tabla2_pregunta3 = make_field('En general, creo que puedo obtener resultados que son importantes para mí.')
    encuesta_tabla2_pregunta4 = make_field('Creo que puedo tener éxito en cualquier esfuerzo que me proponga.')
    encuesta_tabla2_pregunta5 = make_field('Seré capaz de superar con éxito muchos desafíos.')
    encuesta_tabla2_pregunta6 = make_field('Confío en que puedo realizar eficazmente muchas tareas diferentes.')
    encuesta_tabla2_pregunta7 = make_field('Comparado con otras personas, puedo hacer la mayoría de las tareas muy bien.')
    encuesta_tabla2_pregunta8 = make_field('Incluso cuando las cosas son difíciles, puedo realizarlas bastante bien.')
    encuesta_tabla2_pregunta9 = make_field('Podré alcanzar la mayoría de los objetivos que me he propuesto.')

    encuesta_tabla3_pregunta1 = make_field2 ('Llegar tarde a una cita')
    encuesta_tabla3_pregunta2 = make_field2 ('Comprar a vendedores ambulantes')
    encuesta_tabla3_pregunta3 = make_field2 ('Tirar basura en la calle')
    encuesta_tabla3_pregunta4 = make_field2 ('Trabajar y recibir un pago sin que haya firmado un contrato formal (pintar una casa, realizar un reporte, etc.)')
    encuesta_tabla3_pregunta5 = make_field2 ('Silbar o decirle un piropo a un (a) desconocido (a) en la calle')
    encuesta_tabla3_pregunta6 = make_field2 ('Darle trabajo a alguien y pagarle sin pedirle que firme un contrato formal (pintar una casa, realizar un reporte, etc.)')
    encuesta_tabla3_pregunta7 = make_field2 ('Consumir cerveza, aguardiente, ron u otras bebidas alcohólicas en un andén o parque')
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
    encuesta_tabla3_pregunta19 = make_field2 ('Ir a eventos políticos para conseguir empleo/beneficios personales')
    encuesta_tabla3_pregunta20 = make_field2 ('Comprar réplicas de productos originales (lociones, bolsos, zapatos, camisas)')
    encuesta_tabla3_pregunta21 = make_field2 ('Comprar productos sin factura')
    encuesta_tabla3_pregunta22 = make_field2 ('Subarrendar una habitación')
    encuesta_tabla3_pregunta23 = make_field2 ('Vivir en una habitación subarrendada')
    encuesta_tabla3_pregunta24 = make_field2 ('No usar el paso cebra o los puentes peatonales para cruzar una calle')
    encuesta_tabla3_pregunta25 = make_field2 ('Cruzar caminando una calle cuando el semáforo peatonal está en rojo')
    encuesta_tabla3_pregunta26 = make_field2 ('Circular en bicicleta por el andén (no usar la cicloruta)')



    color = models.StringField()