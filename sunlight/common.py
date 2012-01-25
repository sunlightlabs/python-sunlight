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

"""
.. module:: sunlight
    :platform: Linux, Unix, Windows
    :synopsis: Constants and other Globally read things

.. warning::
    If you're using these directly in your app, you might be doing something
    wrong.
"""

API_SIGNUP_PAGE = "http://services.sunlightlabs.com/accounts/register/"
"""
This is a link to the API Key signup page - so that we can sanely direct people
to register for a key (if they don't already have one) -- after all, signing up
for a Sunlight API key is fun for the whole family!
"""

KEY_LOCATION    = "~/.sunlight.key"
"""
This is the location of the api key that's stored on the filesystem. Currently,
it uses a file directly under a tilde, so that windows users don't have to feel
as much pain when using the API. Usually this is something like
``~/.sunlight.key``
"""

KEY_ENVVAR      = "SUNLIGHT_API_KEY"
"""
This is the name of the ``os.environ`` key to look for. It's usually something
stupid simple, like ``SUNLIGHT_API_KEY``.
"""
