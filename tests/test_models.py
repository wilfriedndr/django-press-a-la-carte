from django.test import TestCase
from app.models import Pdf
from django.utils import timezone
import pytest

import pytest

class PdfModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Pdf.objects.create(name = "test",path = "./ici",
        created_at = "2023-04-19 21:01:56"
        )
    def test_first_name_label(self):
        pdf = Pdf.objects.get(id=1)
        field_label = pdf._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')
