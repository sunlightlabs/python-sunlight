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
        
