#!/usr/bin/env python
import sys
from django.conf import settings
from django.core.management import execute_from_command_line

if not settings.configured:
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
            }
        },
        INSTALLED_APPS=(
            'django.contrib.sessions',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sites',
            'mailer',
            'django_nose',
        ),
        MIDDLEWARE_CLASSES=(
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
        ),
        ROOT_URLCONF='mailer.urls',
        TEST_RUNNER='django_nose.NoseTestSuiteRunner',
        SITE_ID=1,
        MAILER_EMAIL_BACKEND='mailer.tests.TestMailerEmailBackend',
    )


def runtests():
    argv = sys.argv[:1] + ['test', 'mailer', '--traceback'] + sys.argv[1:]  # noqa
    execute_from_command_line(argv)

if __name__ == '__main__':
    runtests()
