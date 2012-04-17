# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='django-model-tools',
    version='0.2',
    description='Utility functions or decorators to be used with Django model classes',
    author='Proteus Technologies Co. Ltd.',
    author_email='team@proteus-tech.com',
    url='https://github.com/Proteus-tech/django-model-tools',
    requires=['django'], # should be able to support all django version
    packages=['django_model_tools'])