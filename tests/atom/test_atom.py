import pytest

from atoma.atom import (
    AtomFeed, parse_atom_file, parse_atom_bytes, FeedParseError
)
from atoma import FeedXMLError

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
    with pytest.raises(FeedParseError):
        parse_atom_file('tests/atom/broken-missing-id.xml')


def test_broken_missing_author():
    # The RFC mandates that at least one of feed or entries must have an author
    # but this is rarely the case in practice.
    parsed = parse_atom_file('tests/atom/broken-xkcd.xml')
    assert parsed.authors == list()
    assert parsed.entries[0].authors == list()


def test_broken_missing_updated():
    # The RFC mandates that feed and entries have an updated date
    # but this is rarely the case in practice.
    parsed = parse_atom_file('tests/atom/broken-missing-updated.xml')
    assert parsed.updated is None
    assert parsed.entries[0].updated is None


def test_broken_empty_fields():
    # As a general rule, XML tags should not be empty. In practice optional
    # fields are sometimes present in the feed but with an empty tag
    parsed = parse_atom_file('tests/atom/broken-empty-summary.xml')
    assert parsed.entries[0].summary is None

    parsed = parse_atom_file('tests/atom/broken-empty-title.xml')
    assert parsed.title is None

    parsed = parse_atom_file('tests/atom/broken-empty-updated.xml')
    assert parsed.updated is None

    parsed = parse_atom_file('tests/atom/broken-empty-author.xml')
    assert parsed.authors == []
    assert parsed.entries[0].authors == []

    parsed = parse_atom_file('tests/atom/broken-missing-author-name.xml')
    assert parsed.authors == []
    assert parsed.entries[0].authors == []

    # Require fields (id...) that have empty tags should throw an error
    with pytest.raises(FeedParseError):
        parse_atom_file('tests/atom/broken-empty-id.xml')


def test_broken_not_xml():
    with pytest.raises(FeedXMLError):
        parse_atom_bytes(b'This is not an XML document')
