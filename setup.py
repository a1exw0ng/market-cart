#!/usr/bin/env python
# -*- coding: utf8 -*-

from setuptools import find_packages
from setuptools import setup


# TODO Fix this
READ_PATH = "/home/jdgranberry/PycharmProjects/market-cart/README.md"
REQ_PATH = "/home/jdgranberry/PycharmProjects/market-cart/requirements.txt"

VERSION = ('0', '0', '1')
__version__ = '.'.join(VERSION)

with open(READ_PATH) as f:
    readme = f.read()

with open(REQ_PATH) as f:
    requirements = f.read()

setup(
    author='Josh Granberry',
    author_email='jdgranberry@gmail.com',
    description='Farmer\'s Market Application',
    include_package_data=True,
    install_requires=requirements,
    long_description=readme,
    name='market-cart',
    packages=find_packages(exclude=['tests*']),
    url='https://github.com/jdgranberry/TODO/',
    version=__version__,
    classifiers=(
        'Natural Language :: English',
        'Operating System :: Linux',
        'Programming Language :: Python :: 2.7',
    )
)
