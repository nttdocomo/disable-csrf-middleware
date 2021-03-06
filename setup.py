#!/usr/bin/env python
"""
sentry-auth-github
==================

:copyright: (c) 2016 Functional Software, Inc
"""
from setuptools import setup, find_packages

setup(name='disable_csrf_middleware',
      version='1.7',
      description='A Django middeware to generate predictable errors on sites',
      long_description=__doc__,
      author='Au Ngai',
      author_email='nttdocomo.ouyi@gmail.com',
      url='https://github.com/abarto/django_uncertainty',
      license='BSD',
      install_requires=[],
      tests_require=['Django>=1.6.11'],
      test_suite='uncertainty.tests.runtests.runtests',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Topic :: Utilities',
      ],
      packages=['discsrf'])