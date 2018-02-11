import datetime

from dateutil.tz import tzutc

from atoma.atom import (
    AtomFeed, AtomEntry, AtomTextConstruct, AtomTextType, AtomPerson, AtomLink,
    parse_atom_file
)


def test_rfc_minimal():
    expected_entry = AtomEntry(
        title=AtomTextConstruct(text_type=AtomTextType.text, lang=None,
                                value='Atom-Powered Robots Run Amok'),
        id_='urn:uuid:1225c695-cfb8-4ebb-aaaa-80da344efa6a',
        updated=datetime.datetime(2003, 12, 13, 18, 30, 2, tzinfo=tzutc()),
        authors=[
            AtomPerson(name='John Doe', uri=None, email=None)
        ],
        contributors=[],
        links=[
            AtomLink(href='http://example.org/2003/12/13/atom03', rel=None,
                     type_=None, hreflang=None, title=None, length=None)
        ],
        categories=[],
        published=None,
        rights=None,
        summary=AtomTextConstruct(text_type=AtomTextType.text, lang=None,
                                  value='Some text.'),
        content=None,
        source=None
    )
    expected = AtomFeed(
        title=AtomTextConstruct(text_type=AtomTextType.text, lang=None,
                                value='Example Feed'),
        id_='urn:uuid:60a76c80-d399-11d9-b93C-0003939e0af6',
        updated=datetime.datetime(2003, 12, 13, 18, 30, 2, tzinfo=tzutc()),
        authors=[
            AtomPerson(name='John Doe', uri=None, email=None)
        ],
        contributors=[],
        links=[
            AtomLink(href='http://example.org/', rel=None, type_=None,
                     hreflang=None, title=None, length=None)
        ],
        categories=[],
        generator=None,
        subtitle=None,
        rights=None,
        icon=None,
        logo=None,
        entries=[
            expected_entry
        ]
    )
    assert parse_atom_file('tests/atom/rfc-minimal.xml') == expected
