import datetime

from dateutil.tz import tzutc, tzoffset

from atoma.atom import (
    AtomFeed, AtomEntry, AtomTextConstruct, AtomTextType, AtomPerson, AtomLink,
    AtomGenerator, parse_atom_file
)


def test_rfc_more_extensive():
    expected_entry = AtomEntry(
        title=AtomTextConstruct(text_type=AtomTextType.text, lang=None,
                                value='Atom draft-07 snapshot'),
        id_='tag:example.org,2003:3.2397',
        updated=datetime.datetime(2005, 7, 31, 12, 29, 29, tzinfo=tzutc()),
        authors=[
            AtomPerson(name='Mark Pilgrim', uri='http://example.org/',
                       email='f8dy@example.com')
        ],
        contributors=[
            AtomPerson(name='Sam Ruby', uri=None, email=None),
            AtomPerson(name='Joe Gregorio', uri=None, email=None)
        ],
        links=[
            AtomLink(href='http://example.org/2005/04/02/atom',
                     rel='alternate', type_='text/html', hreflang=None,
                     title=None, length=None),
            AtomLink(href='http://example.org/audio/ph34r_my_podcast.mp3',
                     rel='enclosure', type_='audio/mpeg', hreflang=None,
                     title=None, length=1337)
        ],
        categories=[],
        published=datetime.datetime(2003, 12, 13, 8, 29, 29,
                                    tzinfo=tzoffset(None, -14400)),
        rights=None,
        summary=None,
        content=AtomTextConstruct(text_type=AtomTextType.xhtml, lang=None,
                                  value=''),
        source=None
    )
    expected = AtomFeed(
        title=AtomTextConstruct(text_type=AtomTextType.text, lang=None,
                                value='dive into mark'),
        id_='tag:example.org,2003:3',
        updated=datetime.datetime(2005, 7, 31, 12, 29, 29, tzinfo=tzutc()),
        authors=[],
        contributors=[],
        links=[
            AtomLink(href='http://example.org/', rel='alternate',
                     type_='text/html', hreflang='en', title=None,
                     length=None),
            AtomLink(href='http://example.org/feed.atom', rel='self',
                     type_='application/atom+xml', hreflang=None, title=None,
                     length=None)
        ],
        categories=[],
        generator=AtomGenerator(name='Example Toolkit',
                                uri='http://www.example.com/', version='1.0'),
        subtitle=AtomTextConstruct(text_type=AtomTextType.html, lang=None,
                                   value='A <em>lot</em> of effort\n        '
                                         'went into making this effortless'),
        rights=AtomTextConstruct(text_type=AtomTextType.text, lang=None,
                                 value='Copyright (c) 2003, Mark Pilgrim'),
        icon=None,
        logo=None,
        entries=[
            expected_entry
        ]
    )
    assert (
        parse_atom_file('tests/atom/rfc-more-extensive.xml') == expected
    )
