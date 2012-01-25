# Copyright (c) Sunlight Labs, 2012 under the terms and conditions
# of the LICENSE file.

"""
.. module:: sunlight
    :synopsis: Sunlight API Entry Point

Sunlight API __init__ entry. This package includes and defines
a few aliases, so that folks can just use the facade here, rather then
fight with finding the right module to use.
"""

__appname__ = "sunlight"
__version__ = "0.1~pre1"

import sunlight.services.openstates
import sunlight.services.capitolwords

OpenStates   = sunlight.services.openstates.OpenStates
"""
See :class:`sunlight.services.openstates.OpenStates`
"""

CapitolWords = sunlight.services.capitolwords.CapitolWords
"""
See :class:`sunlight.services.capitolwords.CapitolWords`
"""

import os.path
import sunlight.common
import sunlight.service

def attempt_to_load_apikey():
    """
    This function (which will be auto-called on import of :mod:`sunlight`),
    will attempt to pull the Sunlight API Key from a few places (to offload
    complexity of apps using these bindings) before getting too far.

    .. note::
        This function is implemented to let the enviroment variable override
        the file read key. Keep this in mind when debugging silly issues.
    """

    try:
        fp = os.path.expanduser(sunlight.common.KEY_LOCATION)
        fd = open(fp, 'r')
        sunlight.service.API_KEY = fd.read().strip()
        # print "D: Read API key from: %s" % fp
    except IOError as e:
        # print "D: No API key found at: %s" % fp
        if e.errno != 2:
            print "W: Warning! " + e
    try:
        sunlight.service.API_KEY = \
            os.environ[sunlight.common.KEY_ENVVAR].strip()
        #print "D: Found API key in the env: %s" % sunlight.common.KEY_ENVVAR
    except KeyError as e:
        pass
        #print "D: No API key in the environ: %s" % sunlight.common.KEY_ENVVAR
    #print "D: API key: %s" % sunlight.service.API_KEY

attempt_to_load_apikey()
