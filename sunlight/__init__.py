# Copyright (C) 2012, Paul Tagliamonte <paultag@sunlightfoundation.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sunlight.services.openstates
import sunlight.services.capitolwords

OpenStates   = sunlight.services.openstates.OpenStates
CapitolWords = sunlight.services.capitolwords

import os.path
import sunlight.common
import sunlight.service

def attempt_to_load_apikey():
    try:
        fd = open(os.path.expanduser(sunlight.common.KEY_LOCATION), 'r')
        API_KEY = fd.read().strip()
    except IOError as e:
        if e.errno != 2:
            print "W: Warning! " + e
    try:
        sunlight.service.API_KEY = \
            os.environ[sunlight.common.KEY_ENVVAR].strip()
    except KeyError as e:
        pass

attempt_to_load_apikey()
