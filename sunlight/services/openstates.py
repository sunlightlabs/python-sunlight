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
.. module:: sunlight.services.openstates
    :platform: Linux, Unix, Windows
    :synopsis: OpenStates API Implementation

OpenStates API Implementation inside ``python-sunlight``.
"""

import sunlight.service
import json

module_name = "openstates"
service_url = "http://openstates.org/api/v1"

class OpenStates(sunlight.service.Service):
    """
    Bindings into the `OpenStates project <http://openstates.org/>`_. Keep in
    mind this is a *very* thin wrapper around the
    `OpenStates API <http://openstates.org/api/>`_, so most of this should be
    super predictable and easy to pick up. Just as a little extra help, we've
    included docs on each of the major methods.
    """

    def metadata(self, **kwargs):
        """
        Query the OpenStates searver for metadata relating to state-level
        assemblies, legislators and bills.

        The docs for the
        `Overview <http://openstates.org/api/metadata/#metadata-overview>`_
        access method, as well as the
        `State-local <http://openstates.org/api/metadata/#state-metadata>`_
        access method can be found on the OpenStates site linked.
        """
        return self.get( "metadata", **kwargs )

    def bills(self, **kwargs):
        """
        Query the OpenStates server for data relating to state-level
        legislative instruments, such as bills, memoranda, or resolutions.

        The keyword arguments can be found on the
        `OpenStates Website <http://openstates.org/api/bills/>`_.

        Doing `lookups <http://openstates.org/api/bills/#bill-lookup>`_,
        as well as `searches <http://openstates.org/api/bills/#bill-search>`_
        should match the documentation.
        """
        return self.get( "bills", **kwargs )

    def legislators(self, **kwargs):
        """
        Query the OpenStates server for data relating to the state-level
        legislators.

        The `Legislator <http://openstates.org/api/legislators/>`_ API docs are
        complete and detailed for general use.

        That page details
        `lookups <http://openstates.org/api/legislators/#legislator-lookup>`_,
        `searches <http://openstates.org/api/legislators/#legislator-search>`_,
        as well as the
        `geo-searching <http://openstates.org/api/legislators/#geo-lookup>`_,
        all of which should be usable from here.
        """
        return self.get( "legislators", **kwargs )

    def committees(self, **kwargs):
        """
        Query the OpenStates server for information regarding state-level
        legislative committees.

        For information regarding it's use, please read the API documentation
        on the `OpenStates site <http://openstates.org/api/committees/>`_.
        """
        return self.get( "committees", **kwargs )

    def events(self, **kwargs):
        """
        Query the OpenStates server for information regarding upcoming events
        taken from a state-level legislative calendar.

        Please do take a look at the fantastic documentation on the
        `OpenStates site <http://openstates.org/api/events/>`_
        """
        return self.get( "events", **kwargs )

    def districts(self, **kwargs):
        """
        Query the OpenStates server for information regarding state-level
        legislative districts.

        Check out the `docs <http://openstates.org/api/districts/>`_.
        """
        return self.get( "districts", **kwargs )

    # API impl methods

    def _get_url( self, obj, apikey, **kwargs ):
        ret = "%s/%s?apikey=%s" % (
            service_url,
            obj,
            apikey
        )
        for arg in kwargs:
            ret += "&%s=%s" % ( arg, kwargs[arg] )
        return ret

    def _decode_response( self, response ):
        return json.loads( response )

    def _handle_bad_http_code( self, code ):
        # This will most likely be removed when we can get a read on the
        # errorful page. For now, this.

        messages = {
            400 : "Error with your request. Perhaps too many results?",
            404 : "Object doesn't exist."
        }
        try:
            return messages[code]
        except KeyError as e:
            return "Unknown error code!!! Recieved a %s from the server." % (
                str( code )
            )
