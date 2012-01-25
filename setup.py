#!/usr/bin/env python

from sunlight import __appname__, __version__
from distutils.core import setup

long_description = open('README.rst').read()

setup(
	name       = __appname__,
	version    = __version__,
	packages   = [ 'sunlight', 'sunlight.services' ],

    author       = "Paul Tagliamonte",
    author_email = "paultag@sunlightfoundation.com",

    long_description = long_description,
    description      = 'Unified Sunlight API bindings',
    license          = "Expat",
    url              = "https://github.com/paultag/python-sunlight",

    platforms        = ['any']
)
