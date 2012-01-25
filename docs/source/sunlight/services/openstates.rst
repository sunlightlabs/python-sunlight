OpenStates -- States rule!
==========================

API Documentation
*****************

Class Documentation
*******************

.. automodule:: sunlight.services.openstates
   :members:

Examples
********

Bills::

    from sunlight import OpenStates
    os = OpenStates()

    vt_agro_bills = os.bills(
        q='agriculture',
        state='vt',
        chamber='upper'
    )

    for bill in vt_agro_bills:
        print bill['title']


Legislators::

    ca_dems = os.legislators(
        state='ca',
        party='Democratic',
        first_name='Bob',
        active='true'
    )

    for dem in ca_dems:
        print "%s %s (%s)" % (
            dem['first_name'], dem['last_name'], dem['chamber'] )

Committees::

    from sunlight import OpenStates
    os = OpenStates()

    md_cttys = os.committees( state='md', chamber='upper' )
    for ctty in md_cttys:
        print "%s (%s)" % ( ctty['committee'], ctty['chamber'] )

Events::

    from sunlight import OpenStates
    os = OpenStates()
    
    tx_events = os.events( state='tx', type='committee:meeting' )
    for event in tx_events:
        print "Event @ %s" % event['when']
        for who in event['participants']:
            print "  %s (%s)" % ( who['participant'], who['chamber'] )
                        
