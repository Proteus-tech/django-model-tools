# -*- coding: utf-8 -*-

import unittest

from django.db import IntegrityError

from sample_app.models import SampleModel

class TestSampleModel(unittest.TestCase):
    def test_save_successfully(self):
        sample_model = SampleModel()
        sample_model.a_field = 'abc'
        sample_model.save() # this will not throw an exception

        self.assertEqual(SampleModel.objects.all().count(), 1)
        self.assertEqual(SampleModel.objects.all()[0].a_field, 'abc')

    def test_save_field_is_null(self):
        sample_model = SampleModel()
        sample_model.a_field = None
        with self.assertRaises(IntegrityError) as exc:
            sample_model.save()

        self.assertEqual(exc.exception.message, 'SampleModel.a_field may not be NULL or BLANK')

    def test_save_field_is_blank(self):
        sample_model = SampleModel()
        sample_model.a_field = None
        with self.assertRaises(IntegrityError) as exc:
            sample_model.save()

        self.assertEqual(exc.exception.message, 'SampleModel.a_field may not be NULL or BLANK')