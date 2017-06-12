#!/usr/bin/env python
# -*- coding: utf8 -*-

from setuptools import find_packages
from setuptools import setup
import os.path


VERSION = ('0', '0', '1')
__version__ = '.'.join(VERSION)

root = os.path.abspath(os.path.dirname(__file__))

setup(
    author='Josh Granberry',
    author_email='jdgranberry@gmail.com',
    description='Farmer\'s Market Application',
    include_package_data=True,
    install_requires=[
        'click==6.7',
        'Flask==0.12.2',
        'itsdangerous==0.24',
        'Jinja2==2.9.6',
        'MarkupSafe==1.0',
        'pluggy==0.4.0',
        'py==1.4.34',
        'pytest==3.1.2',
        'pytest-pep8==1.0.6',
        'tox==2.7.0',
        'virtualenv==15.1.0',
        'Werkzeug==0.12.2]'
    ],
    name='market-cart',
    packages=find_packages(exclude=['tests*']),
    url='https://github.com/jdgranberry/market-cart/',
    version=__version__,
    classifiers=(
        'Natural Language :: English',
        'Operating System :: Linux',
        'Programming Language :: Python :: 2.7',
    )
)
