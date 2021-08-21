from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from .models import Player


class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass

class Consent(Page):
    form_model = 'player' 
    form_fields = ['num_temporal','genero', 'accepts_terms']

class Survey(Page):
    form_model = 'player'    
    form_fields = ['calidad_noticia', 'informacion_noticia', 'noticia_incompleta', 'noticia_credibilidad', 'noticia_tiempo',
    'noticia_calidad', 'noticia_imagenes', 'noticia_publico_general', 'noticia_informacion_importante',
    'noticia_informacion_importante_politicos', 'noticia_lenguaje', 'noticia_lideres_similar',
    'noticia_impactante', 'noticia_angustiante', 'noticia_violenta', 'lider_necesario', 'acuerdo_paz', 
    'gobierno_responsable_lideres', 'conflicto_armado_cesado', 'frase_identificado_1', 'frase_identificado_2', 'frase_identificado_3',
    'victima_responsable', 'siente_compasion', 'entristece_persona_solitaria', 'importancia_sentimientos',
    'muestras_afecto', 'molestan_personas_infelices', 'ponerse_nervioso', 'llorar_felicidad', 'involucrarse_emocionalmente', 
    'cancion_conmueve', 'perder_control_malas_noticias', 'gente_influencia_estado_animo', 'extrajeros_geniales', 'trabajador_social',
    'enfado_amigo', 'abrir_regalos', 'gente_solitaria_no_amistosa', 'llorar_molesta', 'canciones_feliz', 'sentimientos_personajes_novela',
    'enfado_maltrato', 'mantener_calma', 'amigo_problemas', 'risa_otro', 'llanto_divierte', 'decisiones_sin_sentimientos', 'gente_deprimida_alrededor', 
    'irritar_gente', 'disgusto_animal_sufriendo', 'involucrarse_libros_tonto', 'ancianos_indefensos', 'irrita_lagrimas_otros', 'involucrar_pelicula', 
    'mantener_calma_emocion', 'ninos_lloran_sin_razon']


class SocioDemSurvey(Page):
    form_model = 'player'
    form_fields = ['edad', 'ciudad', 'estrato', 'estado_civil', 'numero_hijos', 'identifica_cultura',
    'identifica_religion','nivel_estudios', 'tendencia_politica', 'disposicion_riesgos', 'victima_violencia_farc_eln', 
    'victima_violencia_auc_otros', 'victima_violencia_otros_delicuencia', 'victima_no_violencia', 'familia_victima_farc_eln', 
    'familia_victima_auc_otros', 'familia_victima_otros_delincuencia', 'familia_victima_no_violencia',
    'conseguir_esfuerzo','planes_termino', 'juego_suerte', 'propongo_aprender', 'mayores_logros', 'establecer_metas', 'competencia_excelencia',
    'salir_adelante', 'comparar_calificaciones', 'empeno_trabajo', 'alcanzar_objetivos', 'cumplir_tareas', 'obtener_resultados',
    'exito_esfuerzo','superar_desafios', 'confianza_tareas', 'tareas_excelencia', 'tareas_dificiles']

class Invitation(Page):
    form_model = 'player'

class Video(Page):
    form_model = 'player'
    # print(Player.objects.get(pk=1))
    # print(Player.objects.all())
    # for p in Player.objects.raw('SELECT id, genero FROM lideres_sociales_player'):
    #     print(p)
    # print(list(Player.objects.raw('SELECT id, genero FROM lideres_sociales_player'))[0])
    # print(len(Player.objects.filter(genero__exact='Masculino')))

    #Here is where each treatment is assigned based on the participant's gender and the number of registers in the DB

    def vars_for_template(self):
        self.player.contador_masculino = Player.objects.filter(genero__exact='Masculino').count()
        self.player.contador_femenino = Player.objects.filter(genero__exact='Femenino').count()
        link = ""
        if self.player.genero == 'Masculino':
            if self.player.contador_masculino >= 1 and self.player.contador_masculino <= 46:
                self.player.tratamiento = "Empatía"
                link = "https://drive.google.com/file/d/1G2QVdfV6rorWWN7bEnR7CWgK3v1ga8nD/preview"

            if self.player.contador_masculino >= 47 and self.player.contador_masculino <= 92:
                self.player.tratamiento = "Expectativa Normativa"
                link = "https://drive.google.com/file/d/1VMIP4xuGVDLpujrHuH5AqWyRHK7hLaYs/preview"

            if self.player.contador_masculino >= 93 and self.player.contador_masculino <= 138:
                self.player.tratamiento = "Expectativa Empírica"
                link = "https://drive.google.com/file/d/1p6GEkyC4hnrMF_2kfjlCrfa2myktLWEU/preview"

            if self.player.contador_masculino >= 139 and self.player.contador_masculino <= 184:
                self.player.tratamiento = "Informacional"
                link = "https://drive.google.com/file/d/19xw56Bwt9Ea8Fhy_M88nTsj5YHZutbWp/preview"

            if self.player.contador_masculino >= 185 and self.player.contador_masculino <= 230:
                self.player.tratamiento = "Línea Base"
                link = "https://drive.google.com/file/d/1QV5g_iR9a5zDO62W7-sEafQaRNHkGNwm/preview"
                
        else:
            if self.player.contador_femenino >= 1 and self.player.contador_femenino <= 46:
                self.player.tratamiento = "Empatía"
                link = "https://drive.google.com/file/d/1G2QVdfV6rorWWN7bEnR7CWgK3v1ga8nD/preview"

            if self.player.contador_femenino >= 47 and self.player.contador_femenino <= 92:
                self.player.tratamiento = "Expectativa Normativa"
                link = "https://drive.google.com/file/d/1VMIP4xuGVDLpujrHuH5AqWyRHK7hLaYs/preview"

            if self.player.contador_femenino >= 93 and self.player.contador_femenino <= 138:
                self.player.tratamiento = "Expectativa Empírica"
                link = "https://drive.google.com/file/d/1p6GEkyC4hnrMF_2kfjlCrfa2myktLWEU/preview"
                
            if self.player.contador_femenino >= 139 and self.player.contador_femenino <= 184:
                self.player.tratamiento = "Informacional"
                link = "https://drive.google.com/file/d/19xw56Bwt9Ea8Fhy_M88nTsj5YHZutbWp/preview"

            if self.player.contador_femenino >= 185 and self.player.contador_femenino <= 230:
                self.player.tratamiento = "Línea Base"
                link = "https://drive.google.com/file/d/1QV5g_iR9a5zDO62W7-sEafQaRNHkGNwm/preview"    

                
        return {
            'contador_masculino' : self.player.contador_masculino,
            'contador_femenino' : self.player.contador_femenino,
            'genero': self.player.genero,
            'link' : link
        }

page_sequence = [Consent, Video, Survey, SocioDemSurvey, Invitation]
