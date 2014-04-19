# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import redditclone
version = redditclone.__version__

setup(
    name='Reddit Clone',
    version=version,
    author='',
    author_email='mvrmoreira@gmail.com',
    packages=[
        'redditclone',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['redditclone/manage.py'],
)