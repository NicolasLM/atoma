import pytest

from atoma.rss import (
    parse_rss_file, parse_rss_bytes, RSSChannel, FeedParseError
)
from atoma import FeedXMLError

data = b"""\
<?xml version="1.0"?>
<rss version="2.0">
    <channel>
        <title>Foo</title>
        <link>http://foo.bar</link>
        <description>Foo bar.</description>
        <item>
            <title>Baz item</title>
        </item>
    </channel>
</rss>
"""

cdata_description = """\
I'm headed for France. I wasn't gonna go this year, but then last week \
<a href="http://www.imdb.com/title/tt0086525/">Valley Girl</a> came out and I \
said to myself, Joe Bob, you gotta get out of the country for a while."""


def test_read_bytes():
    assert isinstance(parse_rss_bytes(data), RSSChannel)


def test_broken_missing_title():
    # RSS feed title is mandatory by specs, but some feeds in the wild
    # do not provide it
    p = parse_rss_file('tests/rss/broken-missing-title.xml')
    assert p.title is None


def test_broken_missing_description():
    # RSS feed description is mandatory by specs, but some feeds in the wild
    # do not provide it
    p = parse_rss_file('tests/rss/broken-missing-description.xml')
    assert p.description is None


def test_broken_missing_link():
    # RSS feed link is mandatory by specs, but some feeds in the wild
    # do not provide it
    p = parse_rss_file('tests/rss/broken-missing-link.xml')
    assert p.link is None
    assert p.items[0].link is None
    assert p.items[0].guid is None
    assert p.items[1].link == 'http://link1'
    assert p.items[1].guid == 'http://link1'
    assert p.items[2].link == 'http://link2'
    assert p.items[2].guid == '646326554'


def test_broken_missing_source_url():
    # The URL of a source is mandatory by specs, but some feeds in the wild
    # do not provide it
    p = parse_rss_file('tests/rss/broken-missing-source-url.xml')
    assert p.items[0].source.title == 'New York Times'
    assert p.items[0].source.url is None


def test_broken_enclosure():
    # The length and type of an enclosure are mandatory by specs,
    # but some feeds in the wild do not provide them
    p = parse_rss_file('tests/rss/broken-enclosure.xml')
    for i in range(0, 3):
        assert p.items[i].enclosures[0].url == 'https://foo.com/test.mp3'
        assert p.items[i].enclosures[0].length is None
        assert p.items[i].enclosures[0].type is None


def test_broken_version():
    with pytest.raises(FeedParseError):
        parse_rss_file('tests/rss/broken-version.xml')


def test_broken_no_channel():
    with pytest.raises(FeedParseError):
        parse_rss_file('tests/rss/broken-no-channel.xml')


def test_broken_not_xml():
    with pytest.raises(FeedXMLError):
        parse_rss_bytes(b'This is not an XML document')


def test_encoding():
    parsed = parse_rss_file('tests/rss/encoding.xml')
    assert parsed.items[0].title == 'The &amp; entity'
    assert parsed.items[1].title == "Nice <gorilla> what's he weigh?"
    assert parsed.items[2].title == "Rïchàrd Plop's ☃"
    assert parsed.items[2].description == cdata_description
    assert parsed.items[3].description is None
