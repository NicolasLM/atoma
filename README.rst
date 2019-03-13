Atoma
=====

.. image:: https://travis-ci.org/NicolasLM/atoma.svg?branch=master
    :target: https://travis-ci.org/NicolasLM/atoma
.. image:: https://coveralls.io/repos/github/NicolasLM/atoma/badge.svg?branch=master
    :target: https://coveralls.io/github/NicolasLM/atoma?branch=master

Atom, RSS and JSON feed parser for Python 3.

Quickstart
----------

Install Atoma with pip::

   pip install atoma

Load and parse an Atom XML file:

.. code:: python

    >>> import atoma
    >>> feed = atoma.parse_rss_file('rss-feed.xml')
    >>> feed.description
    'The blog relating the daily life of web agency developers'
    >>> len(feed.items)
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

* RSS 2.0 - `RSS 2.0 Specification <http://cyber.harvard.edu/rss/rss.html>`_
* Atom Syndication Format v1 - `RFC4287 <https://tools.ietf.org/html/rfc4287>`_
* JSON Feed v1 - `JSON Feed specification <https://jsonfeed.org/version/1>`_
* OPML 2.0, to share lists of feeds - `OPML 2.0 <http://dev.opml.org/spec2.html>`_
* Typed: feeds decomposed into meaningful Python objects
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

To use this library a basic understanding of feeds is required. For Atom, the
`Introduction to Atom <https://validator.w3.org/feed/docs/atom.html>`_ is a must
read. The `RFC 4287 <https://tools.ietf.org/html/rfc4287>`_ can help lift some
ambiguities. Finally the `feed validator <https://validator.w3.org/feed/>`_ is
great to test hand-crafted feeds.

For RSS, the `RSS specification <http://cyber.harvard.edu/rss/rss.html>`_ and
`rssboard.org <http://www.rssboard.org>`_ have a ton of information and
examples.

For OPML, the `OPML specification
<http://dev.opml.org/spec2.html#subscriptionLists>`_ has a paragraph dedicated
to its usage for syndication

Non-implemented Features
------------------------

Some seldom used features are not implemented:

* XML signature and encryption
* Some Atom and RSS extensions
* Atom content other than `text`, `html` and `xhtml`

License
-------

MIT
