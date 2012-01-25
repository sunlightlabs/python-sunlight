#!/usr/bin/env python

from sunlight import __appname__, __version__

import os
from os.path import join
from distutils.core import setup

def dirls(d):
	ret = []
	for root, dirs, files in os.walk(d):
		if files != []:
			for f in files:
				ret.append(root + "/" + f)
	return ret

setup(
	name       = __appname__,
	version    = __version__,
	packages   = [ 'sunlight', 'sunlight.services' ],
	scripts    = dirls('bin')
)
