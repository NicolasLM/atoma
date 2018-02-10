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
    >>> feed.authors
    [AtomPerson(name='Richard Plop', uri=None, email='richard@plop.org')]
    >>> len(feed.entries)
    5

Parsing feeds from the Internet is easy as well:

.. code:: python

    >>> import atoma, requests
    >>> response = requests.get('http://lucumr.pocoo.org/feed.atom')
    >>> feed = atoma.parse_atom_bytes(response.content)
    >>> feed.title.value
    "Armin Ronacher's Thoughts and Writings"

Features
--------

* Atom Syndication Format v1 - `RFC4287 <https://tools.ietf.org/html/rfc4287>`_
* Typed: atom feed decomposed into meaningful Python objects
* Secure: uses defusedxml to load untrusted feeds
* Compatible with Python 3.6+

Security warning
----------------

If you use this library to display content from feeds in a web page, you NEED
to clean the HTML contained in the feeds to prevent `Cross-site scripting (XSS)
<https://en.wikipedia.org/wiki/Cross-site_scripting>`_. The `bleach
<https://github.com/mozilla/bleach>`_ library is recommended for cleaning feeds.

Useful Resources
----------------

To use this library a basic understanding of Atom feeds is required. The
`Introduction to Atom <https://validator.w3.org/feed/docs/atom.html>`_ is a must
read. The `RFC 4287 <https://tools.ietf.org/html/rfc4287>`_ can help lift some
ambiguities. Finally the `feed validator <https://validator.w3.org/feed/>`_ is
great to test hand-crafted feeds.

Non-implemented Atom Features
-----------------------------

Some seldom used Atom features are not implemented:

* XML signature and encryption
* Atom Extensions
* Content other than `text`, `html` and `xhtml`

License
-------

MIT
