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

        More information on searches can be found in the API
        `refdoc <http://openstates.org/api/bills/#bill-search>`_
        """
        return self.get( "bills", **kwargs )

    def bill_lookup( self, state_abbr, session,
            bill_id, chamber=None, **kwargs ):
        """
        Query the OpenStates server for data relating to a very exact bill
        lookup path.

        The ``chamber`` argument is optional, and should be used in cases
        where it's ambiguous.

        Doing `lookups <http://openstates.org/api/bills/#bill-lookup>`_,
        should match the documentation.
        """
        lss = "bills/%s/%s/" % ( state_abbr, session )
        if chamber != None:
            lss += chamber + "/"
        lss += bill_id + "/"
        return self.get( lss, **kwargs )

    def legislators(self, **kwargs):
        """
        Query the OpenStates server for data relating to the state-level
        legislators.

        The `Legislator <http://openstates.org/api/legislators/>`_ API docs are
        complete and detailed for general use.

        Check out the API docs on preforming
        `searches <http://openstates.org/api/legislators/#legislator-search>`_
        on the site.
        """
        return self.get( "legislators", **kwargs )

    def legislator_lookup( self, leg_id, **kwargs ):
        """
        Query the OpenStates server for data relating to a single legislator.

        the ``leg_id`` argument is a legislator ID code, such as ``MDL000210``

        `lookups <http://openstates.org/api/legislators/#legislator-lookup>`_
        should match the docs pretty closely.
        """
        lss = "legislators/%s/" % leg_id
        return self.get( lss, **kwargs )

    def legislator_geo_lookup( self, **kwargs ):
        """
        Query the OpenStates server for data on all legislators that serve
        districts containing a given geographical point.

        This method takes two kwargs, one for Latitude (``lat``), and
        another for Longitude (``long``) (as documented on the API refdoc
        below)

        `geo-searching <http://openstates.org/api/legislators/#geo-lookup>`_
        is on the API docs for the OpenStates site.
        """
        return self.get( "legislators/geo/", **kwargs )

    def committees(self, **kwargs):
        """
        Query the OpenStates server for information regarding state-level
        legislative committees.

        For information regarding it's use, please read the API documentation
        on the `OpenStates site <http://openstates.org/api/committees/>`_.
        """
        return self.get( "committees", **kwargs )

    def committee_lookup( self, committee_id, **kwargs ):
        """
        Query the OpenStates server for information regarding a single
        state-level legislative committee.

        ``committee_id`` is the committee ID code, such as ``MDC000065``.

        For more information (such as what kwargs make sense), please
        read up on the API documentation relating to
        `lookups <http://openstates.org/api/committees/#committee-lookup>`_
        """

        lss = "committees/%s/" % ( committee_id )
        return self.get( lss, **kwargs )

    def events(self, **kwargs):
        """
        Query the OpenStates server for information regarding upcoming events
        taken from a state-level legislative calendar.

        Please do take a look at the fantastic documentation on the
        `OpenStates site <http://openstates.org/api/events/>`_
        """
        return self.get( "events", **kwargs )

    def event_lookup( self, event_id, **kwargs ):
        """
        Query the OpenStates server for information regarding a single event.

        ``event_id`` is an OpenStates event ID, such as ``TXE00000990``.

        Read more on how this is used in the API docs for OpenStates on
        `events <http://openstates.org/api/events/#event-lookup>`_.
        """
        lss = "events/%s/" % ( event_id )
        return self.get( lss, **kwargs )

    def districts(self, **kwargs):
        """
        Query the OpenStates server for information regarding state-level
        legislative districts.

        Check out the `docs <http://openstates.org/api/districts/>`_.
        """
        return self.get( "districts", **kwargs )

    def district_boundary_lookup( self, boundary_id, **kwargs ):
        """
        Query the OpenStates server for information regarding state-level
        legislative district boundaries.

        ``boundary_id`` is something like ``sldl-tx-state-house-district-35``.

        For more information on this method, please check up on the OpenStates
        API doc on
        ``boundray lookups <http://openstates.org/api/districts/#district-boundary-lookup>`_
        """
        lss = "districts/boundary/%s/" % ( boundary_id )
        return self.get( lss, **kwargs )

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
