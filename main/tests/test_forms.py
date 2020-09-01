from django.test import TestCase
from django.core import mail
from main import forms

class TestForm(TestCase):
    def test_valid_contact_us_form_sends_email(self):
        form = forms.ContactForm(
            'name':"Frank",
            'message': "Hello everyone"
        )

        self.asserTrue(form.is_valid())

        with self.assertLogs('main.forms',level='INFO') as cm:
            form.send_mail()

        self.assertEqual(len)