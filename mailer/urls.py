from django.conf.urls import url

import mailer.views

urlpatterns = (
    url(r'^report/$', mailer.views.report, name='mailer_report'),
)
