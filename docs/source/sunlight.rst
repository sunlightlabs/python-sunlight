__init__ -- Facade for the OpenStates API Bindings
==================================================

The module __init__ contains a number of things to help make using the API a
bit easier then it usually is. At it's core, the APIs are implemented as
subclasses of the :class:`sunlight.service.Service` class, so importing each
would require ugly imports (such as ``import sunlight.services.openstates``)

.. warning::
    Currently, the bindings are incomplete. Please keep this in mind, and
    do consider contributing some code to interface with the API in question.

Bugs with the API (as you're no doubt aware) can be filed, searched, adored
and jeered `on github <https://github.com/paultag/python-sunlight/issues>`_.
Please do note, however, that issues with the *data* that's returned by the API
should be filed with the project in question. For information on where to file
that brand of bug, please check the class that you're using.

Methods and Aliases
*******************

.. automodule:: sunlight
   :members:

Example Usage
*************

Here are some examples on how to use some of the more notable members of the
Sunlight API family. For more examples, check the doc page of the exact class
that you're using - there'll be more on them there.

.. note::
    Please do note these examples may be incomplete or break at any time.
    They're maintained as part of the documentation effort, so please report
    any breakage you find!

OpenStates in 5 seconds::

    from sunlight import OpenStates
    open_states = OpenStates()

    bills = open_states.bills(
        q="agriculture",
        state="vt",
        chamber="upper"
    )

    for bill in bills:
        print "%s: %s" % ( bill['bill_id'], bill['title'] )
