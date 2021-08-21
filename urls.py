# urls.py
from django.conf.urls import url
from otree.urls import urlpatterns
from real_effort_numbers2.pages import AddNumbers


urlpatterns.append(url(r'^AddNumbers/$', AddNumbers.answer_me))
# urlpatterns = url(r'^AddNumbers/$', AddNumbers.as_view())
