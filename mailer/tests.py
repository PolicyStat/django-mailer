from contextlib import contextmanager

from django.core import management
from django.core.urlresolvers import reverse
from django.test import TestCase

from mailer import send_mail
from mailer.models import Message


class TestMailerEmailBackend(object):
    outbox = []

    def __init__(self, **kwargs):
        self.outbox = []

    def open(self):
        pass

    def close(self):
        pass

    def send_messages(self, email_messages):
        self.outbox.extend(email_messages)


class MailerTestCase(TestCase):
    def setUp(self):
        super(MailerTestCase, self).setUp()
        TestMailerEmailBackend.outbox = []

    @contextmanager
    def assert_num_messages_created(self, num_messages):
        before_count = Message.objects.count()
        yield
        after_count = Message.objects.count()
        self.assertEqual(after_count - before_count, num_messages)

    def test_send_mail_creates_message(self):
        with self.assert_num_messages_created(1):
            send_mail(
                subject='Subject',
                message='Foobar',
                from_email='jason.ward@policystat.com',
                recipient_list=['development@policystat.com'],
            )

    def test_send_mail_command_actually_sends_message(self):
        send_mail(
            subject='Subject',
            message='Foobar',
            from_email='jason.ward@policystat.com',
            recipient_list=['development@policystat.com'],
        )
        with self.assert_num_messages_created(-1):
            management.call_command('send_mail')

    def test_view_smoke_test(self):
        r = self.client.get(reverse('mailer_report'))
        self.assertEqual(r.status_code, 302)


class RetryDeferredCommandTestCase(TestCase):
    def test_command_can_run(self):
        args = []
        opts = {}

        management.call_command('retry_deferred', *args, **opts)
