from datetime import datetime, timedelta

from otree.views.admin import AdminReport

from ._builtin import Page, WaitPage


class MyPage(Page):
    form_model = 'player'


class Results(WaitPage):
    
    pass

class SessionBase(object):

    def post(self, *args, **kwargs):
        session_payoff = 4000
        percentage_saved = self.player.percentage_saved
        saved = 0
        if self.player.money_decision == 0:
            disbursement = 4000
        elif self.player.money_decision == 1:
            saved = (percentage_saved / 100) * session_payoff
            disbursement = session_payoff - saved
        else:
            saved = session_payoff
            disbursement = 0
        if saved:
            money = 50 if self.player.intermedio_actual == 1 else 25
            saved += int((saved / 100) * money)
        self.player.payoff = self.player.payoff + saved
        self.player.disbursement = self.player.disbursement + disbursement
        self.player.save()
        return super(SessionBase, self).post(*args, **kwargs)


class EncuestaSocioEconomica(Page):
    template_name = 'experimiento_1/encuesta_economica.html'
    form_model = 'player'
    form_fields = [
        'survey'
        ]


class Session1(SessionBase, Page):
    template_name = 'experimiento_1/session_1.html'
    form_model = 'player'
    form_fields = ['file_session_1']
    document = 'experimento_1/session_1.pdf'
    title= 'Sesión 1'
    text_info = "Las siguientes páginas hacen parte del libro: La Era del Desarrollo Sostenible (2014), y es necesario para nosotros transcribir la información contenida en el documento. El tiempo aproximado del siguiente trabajo es de 15 min, por favor transcriba la información en el espacio disponible. "

    def get_context_data(self, *args, **kwargs):
        context = super(Session1, self).get_context_data(*args, **kwargs)
        context['text_info'] = self.text_info
        context['document_url'] = self.document
        return context


class Session2(SessionBase, Page):
    template_name = 'experimiento_1/session_1.html'
    form_model = 'player'
    form_fields = ['file_session_2']
    document = 'experimento_1/session_2.pdf'

    text_info = "Las siguientes páginas hacen parte del libro: Decrecimiento. Vocabulario ara la nueva era (2015), y es necesario para nosotros transcribir la información contenida en el documento. El tiempo aproximado del siguiente trabajo es de 15 min, por favor transcriba la información en el espacio disponible. "

    def get_context_data(self, *args, **kwargs):
        context = super(Session2, self).get_context_data(*args, **kwargs)
        context['text_info'] = self.text_info
        context['document_url'] = self.document
        return context


class Session3(SessionBase, Page):
    template_name = 'experimiento_1/session_1.html'
    form_model = 'player'
    form_fields = ['file_session_3']
    document = 'experimento_1/session_3.pdf'
    text_info = "Las siguientes páginas hacen parte del libro: Prosperidad sin crecimiento (2011), y es necesario para nosotros transcribir la información contenida en el documento. El tiempo aproximado del siguiente trabajo es de 15 min, por favor transcriba la información en el espacio disponible. "

    def get_context_data(self, *args, **kwargs):
        context = super(Session3, self).get_context_data(*args, **kwargs)
        context['text_info'] = self.text_info
        context['document_url'] = self.document
        return context


class Session4(Page):
    template_name = 'experimiento_1/session_2.html'
    form_model = 'player'
    form_fields = ['monto_session_2', 'coin_select']

    def post(self, *args, **kwargs):
        monto = int(self.request.POST.get('monto_session_2'))
        if self.request.POST.get('coin_select') == '0':
            self.player.payoff += (5000 - monto) + monto + (monto * 0.5)
        elif self.request.POST.get('coin_select') == '1':
            self.player.payoff += (5000 - monto)
        self.player.save()
        return super(Session4, self).post(*args, **kwargs)

class Informacion(Page):

    def js_vars(self):
        return dict(
            intermedio_actual = self.player.intermedio_actual,
        )

    def vars_for_template(self):

        money = 50 if self.player.intermedio_actual == 1 else 25

        return {
            "price_session" : money,
        }

class Informacion_moneda(Page):
    def vars_for_template(self):
        return {
            "1" : 2,
        }

class IntermedioSession(Page):
    template_name = 'experimiento_1/intermedio.html'
    form_model = 'player'
    form_fields = ['money_decision', 'percentage_saved']

    def get_context_data(self, *args, **kwargs):
        context = super(IntermedioSession, self).get_context_data(*args, **kwargs)
        return context

    def get_form(self, *args, **kwargs):
        form = super(IntermedioSession, self).get_form(*args, **kwargs)
        new_decisions = []
        money = 50 if self.player.intermedio_actual == 1 else 25
        for field in form.fields['money_decision'].choices:
            new_decisions.append((field[0], field[1].format(price_session=money)))
        form.fields['money_decision'].choices = new_decisions
        return form

    def post(self, *args, **kwargs):
        money_decision = self.request.POST.get('money_decision')
        percentage_saved = self.request.POST.get('percentage_saved')

        self.player.intermedio = self.player.intermedio + 1
        self.player.save()
        return super(IntermedioSession, self).post(*args, **kwargs)


class SevenDaysWaitPage(Page):
    template_name = 'experimiento_1/wait_page.html'
   
    def get_context_data(self, *args, **kwargs):
        day_available = self.player.updated_at.replace(hour=0, tzinfo=None) + timedelta(days=7)
        today = datetime.now()
        context = super(SevenDaysWaitPage, self).get_context_data(*args, **kwargs)
        context['day_available'] = day_available
        context['can_access'] = today > day_available
        return context


class Consent(Page):
    form_model = 'player'  # Le dice que es un jugador
    form_fields = ['num_temporal', 'accepts_terms']


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


class Expectations(Page):
    template_name = 'experimiento_1/Expectations.html'
    form_model = 'player'
    form_fields = [
        'expectations'
        ]
   

class sesion_3(Page):
    template_name= 'experimiento_1/sesion_3.html'
    form_model = 'player'  

class Results(Page):
    pass




page_sequence = [
    #Expectations,
    #Consent,
    #MyPage,
    #IntermedioSession,
    #Expectations,
    #Session1,
    #SevenDaysWaitPage,
    Informacion,
    IntermedioSession,
    Session2,
    #SevenDaysWaitPage,
    #sesion_3,
    #Session3,
    #EncuestaSocioEconomica,
    Informacion_moneda,
    Session4,
    Results
]
