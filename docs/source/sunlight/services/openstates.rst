.. _sunlight.openstates:

===================
sunlight.openstates
===================

This is a thin wrapper around the `Open States <http://openstates.org/api/>`_
API, which provides data on state legislators, bills, votes, committees, districts,
events, and more!

Please consider contributing to the
`Open States project <https://github.com/sunlightlabs/openstates>`_, it's all open-source,
and community involvement is valued very much by the Open States crew.

.. note::
    If you come across data quality issues, broken code, or missing data,
    please file a report on the
    `GitHub issues page <https://github.com/sunlightlabs/openstates/issues>`_.
    Thanks!

Metadata
========

Methods for dealing with `Open States Metadata <http://openstates.org/api/metadata/#metadata-fields>`_.

.. automethod:: sunlight.services.openstates.openstates.all_metadata
.. automethod:: sunlight.services.openstates.openstates.state_metadata

Bills
=====

Methods for dealing with `Open States Bills <http://openstates.org/api/bills/#bill-fields>`_.

.. automethod:: sunlight.services.openstates.openstates.bills
.. automethod:: sunlight.services.openstates.openstates.bill_detail

Legislators
===========

Methods for dealing with `Open States Legislators <http://openstates.org/api/legislators/#legislator-fields>`_.

.. automethod:: sunlight.services.openstates.openstates.legislators
.. automethod:: sunlight.services.openstates.openstates.legislator_detail
.. automethod:: sunlight.services.openstates.openstates.legislator_geo_search

Committees
==========

Methods for dealing with `Open States Committees <http://openstates.org/api/committees/#committee-fields>`_.

.. automethod:: sunlight.services.openstates.openstates.committees
.. automethod:: sunlight.services.openstates.openstates.committee_detail

Districts
=========

Methods for dealing with `Open States Districts <http://openstates.org/api/districts/#district-fields>`_.

.. automethod:: sunlight.services.openstates.openstates.districts
.. automethod:: sunlight.services.openstates.openstates.district_boundary

Events
======

Methods for dealing with `Open States Events <http://openstates.org/api/events/#event-fields>`_.

.. automethod:: sunlight.services.openstates.openstates.events
.. automethod:: sunlight.services.openstates.openstates.event_detail


Examples
========

Bills::

    from sunlight import openstates

    vt_agro_bills = openstates.bills(
        q='agriculture',
        state='vt',
        chamber='upper'
    )

    for bill in vt_agro_bills:
        print bill['title']


Legislators::

    from sunlight import openstates
    
    ca_dems = openstates.legislators(
        state='ca',
        party='Democratic',
        first_name='Bob',
        active='true'
    )

    for dem in ca_dems:
        print "%s %s (%s)" % (
            dem['first_name'], dem['last_name'], dem['chamber'] )

Committees::

    from sunlight import openstates

    md_cttys = openstates.committees( state='md', chamber='upper' )
    for ctty in md_cttys:
        print "%s (%s)" % ( ctty['committee'], ctty['chamber'] )

Events::

    from sunlight import openstates
    
    tx_events = openstates.events( state='tx', type='committee:meeting' )
    for event in tx_events:
        print "Event @ %s" % event['when']
        for who in event['participants']:
            print "  %s (%s)" % ( who['participant'], who['chamber'] )
                        
