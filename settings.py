from os import environ


SESSION_CONFIGS = [
    dict(
        name='Cuestionario',
        display_name='Cuestionario',
        num_demo_participants=1,
        app_sequence=['Cuestionario', 'payment_info'],
    ),   
    dict(
        name='mpl',
        display_name="Contratos y consumo: una aproximación cuasi-experimental",
        num_demo_participants=1,
        app_sequence=['mpl'],
    ),
    dict(
        name='lideres_sociales',
        display_name="La desensibilización de la violencia: el efecto de las noticias en la percepción del asesinato de líderes sociales en Colombia",
        num_demo_participants=1,
        app_sequence=['lideres_sociales'],
    ),
    #dict(
    #     name='myprisoners_dilemma',
    #     display_name="Gift-exchange game",
    #     num_demo_participants=4,
    #     app_sequence=['myprisoners_dilemma'],
    #),
    #dict(
    #     name='prisoner',
    #     display_name="Epa",
    #     num_demo_participants=4,
    #     app_sequence=['prisoner'],
    #),
    #dict(
    #    name='experimiento_1',
    #    display_name="Experimento Leidy",
    #    num_demo_participants=3,
    #    app_sequence=['experimiento_1']
    #),
    dict(
        name='laboratorio',
        display_name="Experimento Nicolas",
        num_demo_participants=1,
        app_sequence=['laboratorio'],
    ),
    dict(
        name='real_effort_numbers',
        display_name="Gift-exchange General",
        num_demo_participants=12,
        app_sequence=['real_effort_numbers']
    ),
    dict(
        name='real_effort_numbers_t_t',
        display_name="Gift-exchange Game T-T",
        num_demo_participants=12,
        app_sequence=['real_effort_numbers_t_t']
    ),
    dict(
        name='real_effort_numbers_t_nt',
        display_name="Gift-exchange Game T-NT",
        num_demo_participants=12,
        app_sequence=['real_effort_numbers_t_nt']
    ),
    dict(
        name='real_effort_numbers_nt_t',
        display_name="Gift-exchange Game NT-T",
        num_demo_participants=12,
        app_sequence=['real_effort_numbers_nt_t']
    ),
    dict(
        name='real_effort_numbers_nt_nt',
        display_name="Gift-exchange Game NT-NT",
        num_demo_participants=12,
        app_sequence=['real_effort_numbers_nt_nt']
    ),
    #dict(
    #     name='public_goods',
    #     display_name="Public Goods",
    #     num_demo_participants=6,
    #     app_sequence=['public_goods', 'payment_info'],
    # ),
    #dict(
    #     name='guess_two_thirds',
    #     display_name="Guess 2/3 of the Average",
    #     num_demo_participants=3,
    #     app_sequence=['guess_two_thirds', 'payment_info'],
    # ),
    #dict(
    #     name='public_goods',
    #     display_name='PGasa',
    #     num_demo_participants=4,
    #     app_sequence=['public_goods'],
    # ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1, participation_fee=0.00, doc=""
)

ROOT_URLCONF = 'urls'

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'es'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

# don't share this with anybody.
SECRET_KEY = 'gu0-t&wo*2un8j93kesnb5!6t2=py8uap9d4qyl)y@u(mp-&w-'

INSTALLED_APPS = ['otree','multiselectfield']

# inactive session configs
# dict(name='trust', display_name="Trust Game", num_demo_participants=2, app_sequence=['trust', 'payment_info']),
# dict(name='prisoner', display_name="Prisoner's Dilemma", num_demo_participants=2,
#      app_sequence=['prisoner', 'payment_info']),
# dict(name='volunteer_dilemma', display_name="Volunteer's Dilemma", num_demo_participants=3,
#      app_sequence=['volunteer_dilemma', 'payment_info']),
# dict(name='cournot', display_name="Cournot Competition", num_demo_participants=2, app_sequence=[
#     'cournot', 'payment_info'
# ]),
# dict(name='dictator', display_name="Dictator Game", num_demo_participants=2,
#      app_sequence=['dictator', 'payment_info']),
# dict(name='matching_pennies', display_name="Matching Pennies", num_demo_participants=2, app_sequence=[
#     'matching_pennies',
# ]),
# dict(name='traveler_dilemma', display_name="Traveler's Dilemma", num_demo_participants=2,
#      app_sequence=['traveler_dilemma', 'payment_info']),
# dict(name='bargaining', display_name="Bargaining Game", num_demo_participants=2,
#      app_sequence=['bargaining', 'payment_info']),
# dict(name='common_value_auction', display_name="Common Value Auction", num_demo_participants=3,
#      app_sequence=['common_value_auction', 'payment_info']),
# dict(name='bertrand', display_name="Bertrand Competition", num_demo_participants=2, app_sequence=[
#     'bertrand', 'payment_info'
# ]),
# dict(name='public_goods_simple', display_name="Public Goods (simple version from tutorial)",
#      num_demo_participants=3, app_sequence=['public_goods_simple', 'payment_info']),
# dict(name='trust_simple', display_name="Trust Game (simple version from tutorial)", num_demo_participants=2,
#      app_sequence=['trust_simple']),
