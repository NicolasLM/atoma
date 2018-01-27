Atoma
=====

.. image:: https://travis-ci.org/NicolasLM/atoma.svg?branch=master
    :target: https://travis-ci.org/NicolasLM/atoma
.. image:: https://coveralls.io/repos/github/NicolasLM/atoma/badge.svg?branch=master
    :target: https://coveralls.io/github/NicolasLM/atoma?branch=master

Atom feed parser for Python 3.

Quickstart
----------

Install Atoma with pip::

   pip install atoma

Load and parse an Atom XML file:

.. code:: python

    >>> import atoma
    >>> feed = atoma.parse_atom_file('atom-feed.xml')
    >>> feed.title.value
    "Richard Plop's news"
    >>> feed.authors
    [AtomPerson(name='Richard Plop', uri=None, email='richard@plop.org')]
    >>> len(feed.entries)
    5

Features
--------

* Atom Syndication Format v1 - `RFC4287 <https://tools.ietf.org/html/rfc4287>`_
* Typed: atom feed decomposed into meaningful Python objects
* Secure: uses defusedxml to load untrusted feeds
* Compatible with Python 3.6+

Non-implemented Atom Features
-----------------------------

Some seldom used Atom features are not implemented:

* XML signature and encryption
* Atom Extensions
* Content other than `text`, `html` and `xhtml`

License
-------

MIT
