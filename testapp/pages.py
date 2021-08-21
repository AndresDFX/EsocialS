from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

#Seria como el forms.py del tutorial
#Aca de definen las clases los campos que tiene tiene models.py
#Los archivos html deben tener el mismo nombre de la clase
class TestAppQuestions(Page):
    form_model = 'player' #Le dice que es un jugador
    form_fields = ['age', 'gender', 'is_lef_handed'] #Los campos de models.py



page_sequence = [TestAppQuestions] #Aca van los nombres de las clases definidas en pages.py

#Class Concent