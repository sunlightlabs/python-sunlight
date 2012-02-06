.. _sunlight.congress:

=================
sunlight.congress
=================

The `Sunlight Labs Congress API
<http://services.sunlightlabs.com/docs/Sunlight_Congress_API/>`_
provides methods for obtaining basic information on Members of Congress,
legislator IDs used by various websites, and geographical lookups between
places and the politicians that represent them. The primary purpose of
the API is to facilitate mashups involving politicians and the various
other APIs that are out there.


Legislators
===========

This set of Congress API methods deal with federal legislators.
For detailed documentaion on the return value of these methods see
`legislator fields <http://services.sunlightlabs.com/docs/congressapi/legislators.get(List)/>`_.

.. automethod:: sunlight.services.congress.congress.legislators
.. automethod:: sunlight.services.congress.congress.legislator_search
.. automethod:: sunlight.services.congress.congress.legislators_for_zip
.. automethod:: sunlight.services.congress.congress.legislators_for_lat_lon

Districts
=========

Pair of methods for retrieving districts.  District dictionaries have a `'state'` and `'number'` key
(ex. `{'state': 'NC', 'number': '3'}`)


.. automethod:: sunlight.services.congress.congress.districts_for_zip
.. automethod:: sunlight.services.congress.congress.districts_for_lat_lon

Committees
==========

Methods for dealing with committees.

.. automethod:: sunlight.services.congress.congress.committees
.. automethod:: sunlight.services.congress.congress.committee_detail
.. automethod:: sunlight.services.congress.congress.committees_for_legislator
