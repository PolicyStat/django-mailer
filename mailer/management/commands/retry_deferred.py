import logging

from django.core.management.base import NoArgsCommand

from mailer.models import Message


class Command(NoArgsCommand):
    help = "Attempt to resend any deferred mail."
    
    def handle_noargs(self, **options):
        log_levels = {
            '0': logging.WARNING,
            '1': logging.INFO,
            '2': logging.DEBUG,
        }
        # in case of 1.4 compatibility, where a string would be passed in

        verbosity = str(options['verbosity'])
        level = log_levels[verbosity]
        logging.basicConfig(level=level, format="%(message)s")
        count = Message.objects.retry_deferred() # @@@ new_priority not yet supported
        logging.info("%s message(s) retried" % count)
