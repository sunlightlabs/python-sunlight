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
__version__ = "1.0.2"

import sunlight.services.openstates
import sunlight.services.capitolwords
import sunlight.services.congress
import sunlight.services.influenceexplorer

openstates = sunlight.services.openstates.openstates()
capitolwords = sunlight.services.capitolwords.capitolwords()
congress = sunlight.services.congress.congress()
influenceexplorer = sunlight.services.influenceexplorer.InfluenceExplorer()

import os.path
import warnings
import sunlight.config
import sunlight.service

def _attempt_to_load_apikey():
    """
    This function (which will be auto-called on import of :mod:`sunlight`),
    will attempt to pull the Sunlight API Key from a few places (to offload
    complexity of apps using these bindings) before getting too far.

    .. note::
        This function is implemented to let the enviroment variable override
        the file read key. Keep this in mind when debugging silly issues.
    """

    try:
        fp = os.path.expanduser(sunlight.config.KEY_LOCATION)
        fd = open(fp, 'r')
        sunlight.config.API_KEY = fd.read().strip()
    except IOError as e:
        if e.errno != 2:
            warnings.warn('key file %s exists but could not be opened: %s' % (
                sunlight.config.KEY_LOCATION, str(e)))
    try:
        sunlight.config.API_KEY = \
                os.environ[sunlight.config.KEY_ENVVAR].strip()
    except KeyError as e:
        pass

_attempt_to_load_apikey()
