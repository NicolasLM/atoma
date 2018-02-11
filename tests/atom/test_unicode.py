import datetime

from dateutil.tz import tzutc

from atoma.atom import (
    AtomFeed, AtomEntry, AtomTextConstruct, AtomTextType, AtomPerson, AtomLink,
    AtomGenerator, AtomCategory, parse_atom_file
)


def test_rfc_unicode():

    expected_entry_1 = AtomEntry(
        title=AtomTextConstruct(text_type=AtomTextType.text, lang=None,
                                value='Article n°1'),
        id_='http://richard.plop/2017/6/5/article-1',
        updated=datetime.datetime(2017, 6, 5, 0, 0, tzinfo=tzutc()),
        authors=[
            AtomPerson(name='Rïchàrd Plop', uri=None, email=None)
        ],
        contributors=[],
        links=[
            AtomLink(href='http://richard.plop/2017/6/5/article-1', rel=None,
                     type_=None, hreflang=None, title=None, length=None)
        ],
        categories=[],
        published=None,
        rights=None,
        summary=None,
        content=AtomTextConstruct(text_type=AtomTextType.html, lang=None,
                                  value='<p></p>'),
        source=None
    )
    expected_entry_2 = AtomEntry(
        title=AtomTextConstruct(text_type=AtomTextType.text, lang=None,
                                value='Unicode snowman'),
        id_='http://richard.plop/2017/6/5/article-2',
        updated=datetime.datetime(2016, 12, 29, 0, 0, tzinfo=tzutc()),
        authors=[
            AtomPerson(name='Rïchàrd Plop', uri=None, email=None)
        ],
        contributors=[],
        links=[
            AtomLink(href='http://richard.plop/2017/6/5/unicode-snowman',
                     rel=None, type_=None, hreflang=None, title=None,
                     length=None)
        ],
        categories=[],
        published=None,
        rights=None,
        summary=None,
        content=AtomTextConstruct(text_type=AtomTextType.text, lang=None,
                                  value='☃'),
        source=None
    )
    source_feed = AtomFeed(
        title=AtomTextConstruct(text_type=AtomTextType.text, lang=None,
                                value='Example, Inc.'),
        id_='http://example.org/',
        updated=datetime.datetime(2003, 12, 13, 18, 30, 2, tzinfo=tzutc()),
        authors=[
            AtomPerson(name='Foo Bar', uri=None, email=None)
        ],
        contributors=[],
        links=[],
        categories=[],
        generator=None,
        subtitle=None,
        rights=None,
        icon=None,
        logo=None,
        entries=[]
    )
    expected_entry_3 = AtomEntry(
        title=AtomTextConstruct(text_type=AtomTextType.text, lang=None,
                                value='Unicode snowman 3'),
        id_='http://richard.plop/2017/6/5/article-3',
        updated=datetime.datetime(2016, 12, 29, 0, 0, tzinfo=tzutc()),
        authors=[
            AtomPerson(name='Foo Bar', uri=None, email=None)
        ],
        contributors=[],
        links=[
            AtomLink(href='http://richard.plop/2017/6/5/unicode-snowman',
                     rel=None, type_=None, hreflang=None, title=None,
                     length=None)
        ],
        categories=[],
        published=None,
        rights=None,
        summary=None,
        content=AtomTextConstruct(text_type=AtomTextType.text, lang=None,
                                  value='☃'),
        source=source_feed
    )
    expected = AtomFeed(
        title=AtomTextConstruct(text_type=AtomTextType.text, lang=None,
                                value="Rïchàrd Plop's blog"),
        id_='http://richard.plop/feed.atom',
        updated=datetime.datetime(2017, 6, 5, 0, 0, tzinfo=tzutc()),
        authors=[],
        contributors=[],
        links=[
            AtomLink(href='http://richard.plop/', rel=None, type_=None,
                     hreflang=None, title=None, length=None),
            AtomLink(href='http://richard.plop/feed.atom', rel='self',
                     type_=None, hreflang=None, title=None, length=None)
        ],
        categories=[
            AtomCategory(term='python', scheme=None, label='Python')
        ],
        generator=AtomGenerator(name='Werkzeug', uri=None, version=None),
        subtitle=AtomTextConstruct(text_type=AtomTextType.text, lang=None,
                                   value="Rïchàrd Plop's personal blog."),
        rights=None,
        icon=None,
        logo=None,
        entries=[expected_entry_1, expected_entry_2, expected_entry_3]
    )
    assert parse_atom_file('tests/atom/unicode.xml') == expected
