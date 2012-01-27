#!/usr/bin/env python
# Copyright (c) Sunlight Labs, 2012 under the terms and conditions
# of the LICENSE file.

from sunlight import __appname__, __version__
from setuptools import setup

long_description = open('README.rst').read()

setup(
    name       = __appname__,
    version    = __version__,
    packages   = [ 'sunlight', 'sunlight.services' ],

    author       = "Paul Tagliamonte",
    author_email = "paultag@sunlightfoundation.com",

    long_description = long_description,
    description      = 'Unified Sunlight API bindings',
    license          = "BSD",
    url              = "https://github.com/sunlightlabs/python-sunlight",

    platforms        = ['any']
)
