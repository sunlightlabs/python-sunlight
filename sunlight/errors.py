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
.. module:: sunlight.errors
    :platform: Linux, Unix, Windows
    :synopsis: Exceptions and Errors
"""

class SunlightException(Exception):
    """
    :class:`sunlight.errors.SunlightException` is the base exception,
    all other sunlight exceptions (such as
    :class:`sunlight.errors.NoAPIKeyException`) all inherit from this. This
    makes it easy to catch all sunlight errors if you really really need to
    (not that you should)
    """
    def __init__(self, value):
        """
        This is just your basic __init__ method, nothing special here.

        Args:
            value (str): Message to report with the Exception
        """
        self.value = value

    def __str__(self):
        """
        Return the string-ular representation of the exception - this makes it
        super easy to just run something like ``print e`` (given ``e`` is a
        SunlightException instance)
        """
        return repr(self.value)

class BadRequestException(SunlightException):
    """
    This gets thrown when the underlying url request has recieved an abnormal
    response code. 
    """
    pass

class NoAPIKeyException(SunlightException):
    """
    This gets thrown if the bindings are asked to issue a requst, but the
    ``sunlight.service.API_KEY`` variable is ``None``.
    """
    pass
