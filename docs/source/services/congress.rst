.. _sunlight.congress:

=================
sunlight.congress
=================

The `Sunlight Congress API
<http://sunlightlabs.github.io/congress/>`_
provides methods for obtaining information for the people and work of
Congress. Information on legislators, districts, committees, bills,
votes, as well as real-time notice of hearings, floor activity and
upcoming bills.

.. autoclass:: sunlight.services.congress.Congress

    Class methods that do not specify positional arguments accept `filtering <http://sunlightlabs.github.io/congress/index.html#filtering>`_, `pagination <http://sunlightlabs.github.io/congress/index.html#pagination>`_, and `sorting <http://sunlightlabs.github.io/congress/index.html#sorting>`_ parameters as keyword arguments. See each method's API page for specfic filtering arguments.

Legislators
===========

This set of method provides various ways to search or look up federal legislators.
For detailed documentaion on the return value of these methods see
`legislator fields <http://sunlightlabs.github.io/congress/legislators.html#fields>`_.

.. automethod:: sunlight.services.congress.Congress.legislators
.. automethod:: sunlight.services.congress.Congress.legislator
.. automethod:: sunlight.services.congress.Congress.all_legislators_in_office
.. automethod:: sunlight.services.congress.Congress.locate_legislators_by_lat_lon
.. automethod:: sunlight.services.congress.Congress.locate_legislators_by_zip

Bills
=====

This set of method provides various ways to search or look up Congressional bills.
For detailed documentaion on the return value of these methods see
`bill fields <http://sunlightlabs.github.io/congress/bills.html#fields>`_.

.. automethod:: sunlight.services.congress.Congress.bills
.. automethod:: sunlight.services.congress.Congress.bill
.. automethod:: sunlight.services.congress.Congress.search_bills
.. automethod:: sunlight.services.congress.Congress.upcoming_bills

Districts
=========

Pair of methods for retrieving districts.  District dictionaries have a `'state'` and `'district'` key
(ex. `{'state': 'NC', 'district': '4'}`).


.. automethod:: sunlight.services.congress.Congress.locate_districts_by_lat_lon
.. automethod:: sunlight.services.congress.Congress.locate_districts_by_zip

Committees
==========

The following methods search legislative committees.
For detailed documentaion on the return value of these methods see
`committee fields <http://sunlightlabs.github.io/congress/committees.html#fields>`_.

.. automethod:: sunlight.services.congress.Congress.committees

Amendments
==========

The following methods search amendments.
For detailed documentaion on the return value of these methods see
`committee fields <http://sunlightlabs.github.io/congress/amendments.html#fields>`_.

.. automethod:: sunlight.services.congress.Congress.amendments

Votes
=====

The following methods search votes.
For detailed documentaion on the return value of these methods see
`vote fields <http://sunlightlabs.github.io/congress/votes.html#fields>`_.

.. automethod:: sunlight.services.congress.Congress.votes

Floor Updates
=============

The following methods search floor updates.
For detailed documentaion on the return value of these methods see
`floor update fields <http://sunlightlabs.github.io/congress/floor_updates.html#fields>`_.

.. automethod:: sunlight.services.congress.Congress.floor_updates

Hearings
========

The following methods search committee hearings.
For detailed documentaion on the return value of these methods see
`hearing fields <http://sunlightlabs.github.io/congress/hearings.html#fields>`_.

.. automethod:: sunlight.services.congress.Congress.hearings

Nominations
===========

The following methods search nominations made by the President of the United States.
For detailed documentaion on the return value of these methods see
`nominations fields <http://sunlightlabs.github.io/congress/nominations.html#fields>`_.

.. automethod:: sunlight.services.congress.Congress.nominations

Congressional Documents
=======================

The following methods search congressional documents including House witness documents and
House committee reports.
For detailed documentaion on the return value of these methods see
`congressional documents fields <http://sunlightlabs.github.io/congress/congressional_documents.html#fields>`_.

.. automethod:: sunlight.services.congress.Congress.congressional_documents

Documents
=========

The following methods search a wide range of documents including Government Accountability
Office (GAO) Reports and Inspector General Reports. These government oversight documents investigate
misconduct, waste and programs.
For detailed documentaion on the return value of these methods see
`documents fields <http://sunlightlabs.github.io/congress/documents.html#fields>`_.

.. automethod:: sunlight.services.congress.Congress.documents