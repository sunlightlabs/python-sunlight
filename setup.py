#!/usr/bin/env python

from sunlight import __appname__, __version__

from distutils.core import setup

setup(
	name       = __appname__,
	version    = __version__,
	packages   = [ 'sunlight', 'sunlight.services' ]
)
