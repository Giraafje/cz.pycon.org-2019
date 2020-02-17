from django.conf.urls import url
from django.views.generic import TemplateView

from pyconcz.proposals.views import (
    proposal_success, proposal_create, proposal_about)

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='proposals/talks_about.html'), name='proposals'),
    url('^(?P<key>[^/]*)/$', proposal_about, name='proposal_about'),
    url(r'financial-aid/grantees/$', TemplateView.as_view(template_name='proposals/financial_aid_grantees.html'), name='finaid_grantees'),
    url('^(?P<key>[^/]*)/form/$', proposal_create, name='proposal_form'),
    url('^(?P<key>[^/]*)/sent/$', proposal_success, name='proposal_success'),
]
