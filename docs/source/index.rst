===============
python-sunlight
===============

Overview
========

python-sunlight serves as a unified API wrapper for the various `open government data
APIs <http://services.sunlightlabs.com>`_ made available by `Sunlight Foundation <http://sunlightfoundation.com>`_
projects.

Currently this library supports the following APIs:

* `Sunlight Congress API <http://services.sunlightlabs.com/docs/Sunlight_Congress_API/>`_ (via :ref:`sunlight.congress`)
* `Open States API <http://openstates.org/api/>`_ (via :ref:`sunlight.openstates`)
* `Capitol Words API <http://capitolwords.org/api/>`_ (via :ref:`sunlight.capitolwords`)

Support is pending for the `Influence Explorer API <http://data.influenceexplorer.com/api/>`_ and the
`Real Time Congress API <http://services.sunlightlabs.com/docs/Real_Time_Congress_API/>`_,
though these currently have their own Python wrappers.

Installation
============

The simplest way to install python-sunlight is via `pip <http://www.pip-installer.org/>`_::

    pip install python-sunlight

You may also wish to check the project out from `GitHub <http://github.com/sunlightlabs/python-sunlight>`_::

    git clone git://github.com/sunlightlabs/python-sunlight.git

Now all you need is a `Sunlight API Key <http://services.sunlightlabs.com/accounts/register/>`_ and you can get started!

.. note::
    After obtaining a key you can use it without exposing it in your code by placing it in a file at :file:`~/.sunlight.key` or in an
    environment variable named :envvar:`SUNLIGHT_API_KEY`.  Alternatively you can set :data:`sunlight.service.API_KEY`.

import sunlight
===============

After setting your API key simply ``import sunlight`` and start using the APIs::

    import sunlight
    nc_legs = sunlight.openstates.legislators(state='nc')

You can also import a specific API client::

    from sunlight import congress
    pelosi = congress.legislators(lastname='Pelosi')[0]

APIs
----

.. toctree::
   :maxdepth: 2

   sunlight/services/congress.rst
   sunlight/services/openstates.rst
   sunlight/services/capitolwords.rst

Internals
=========

Implementation details, for extending python-sunlight or more untraditional uses.

.. toctree::
   :maxdepth: 2

   sunlight.rst
   sunlight/service.rst
   sunlight/common.rst
   sunlight/errors.rst

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
