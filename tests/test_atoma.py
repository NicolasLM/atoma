import pytest

from atoma import (
    AtomFeed, AtomEntry, AtomTextConstruct, AtomTextType, AtomPerson, AtomLink,
    parse_atom_file, parse_atom_bytes, AtomParseError
)

data = b"""\
<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
    <title>Example Feed</title>
    <id>foo</id>
    <updated>2003-12-13T18:30:02Z</updated>
</feed>
"""


def test_read_bytes():
    assert isinstance(parse_atom_bytes(data), AtomFeed)


def test_broken_missing_id():
    with pytest.raises(AtomParseError):
        parse_atom_file('tests/documents/broken-missing-id.xml')


def test_broken_missing_author():
    with pytest.raises(AtomParseError):
        parse_atom_file('tests/documents/broken-missing-author.xml')


def test_broken_missing_author_name():
    with pytest.raises(AtomParseError):
        parse_atom_file('tests/documents/broken-missing-author-name.xml')
