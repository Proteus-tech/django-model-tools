# -*- coding: utf-8 -*-

from django.test import TestCase
from django.db import IntegrityError

from sample_app.models import SampleModel

class TestSampleModel(TestCase):
    def test_save_successfully(self):
        sample_model = SampleModel()
        sample_model.a_field = 'abc'
        sample_model.b_field = 'def'
        sample_model.save() # this will not throw an exception

        self.assertEqual(SampleModel.objects.all().count(), 1)
        self.assertEqual(SampleModel.objects.all()[0].a_field, 'abc')

    def test_save_field_is_null(self):
        sample_model = SampleModel()
        sample_model.a_field = None
        sample_model.b_field = 'def'
        with self.assertRaises(IntegrityError) as exc:
            sample_model.save()

        self.assertEqual(exc.exception.message, 'SampleModel.a_field may not be NULL or BLANK')

    def test_save_field_is_blank(self):
        sample_model = SampleModel()
        sample_model.a_field = ''
        sample_model.b_field = 'def'
        with self.assertRaises(IntegrityError) as exc:
            sample_model.save()

        self.assertEqual(exc.exception.message, 'SampleModel.a_field may not be NULL or BLANK')

    def test_save_field_is_False(self):
        sample_model = SampleModel()
        sample_model.a_field = False
        sample_model.b_field = 'def'
        sample_model.save()  # should be able to save False

    def test_save_field_is_True(self):
        sample_model = SampleModel()
        sample_model.a_field = True
        sample_model.b_field = 'def'
        sample_model.save()  # should be able to save True

    def test_save_field_not_assigning(self):
        sample_model = SampleModel()
        sample_model.a_field = 'abc'
        # not assigning anything makes b_field blank
        with self.assertRaises(IntegrityError) as exc:
            sample_model.save()

        self.assertEqual(exc.exception.message, 'SampleModel.b_field may not be NULL or BLANK')

    def test_save_field_is_spaces(self):
        sample_model = SampleModel()
        sample_model.a_field = ' '
        sample_model.b_field = 'I am not space'
        with self.assertRaises(IntegrityError) as exc:
            sample_model.save()

        self.assertEqual(exc.exception.message, 'SampleModel.a_field may not be NULL or BLANK')