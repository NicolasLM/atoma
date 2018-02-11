import pytest

from atoma.rss import (
    parse_rss_file, parse_rss_bytes, RSSChannel, FeedParseError
)

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
    with pytest.raises(FeedParseError):
        parse_rss_file('tests/rss/broken-missing-title.xml')


def test_broken_version():
    with pytest.raises(FeedParseError):
        parse_rss_file('tests/rss/broken-version.xml')


def test_encoding():
    parsed = parse_rss_file('tests/rss/encoding.xml')
    assert parsed.items[0].title == 'The &amp; entity'
    assert parsed.items[1].title == "Nice <gorilla> what's he weigh?"
    assert parsed.items[2].title == "Rïchàrd Plop's ☃"
    assert parsed.items[2].description == cdata_description
    assert parsed.items[3].description is None
