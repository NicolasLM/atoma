from datetime import datetime

from dateutil.tz import tzutc
import pytest

from atoma.opml import (
    parse_opml_file, parse_opml_bytes, get_feed_list, OPML, OPMLOutline
)
from atoma import FeedXMLError

data = b"""\
<?xml version="1.0" encoding="ISO-8859-1"?>
<opml version="2.0">
    <head>
        <title>states.opml</title>
    </head>
    <body>
        <outline text="United States"/>
    </body>
</opml>
"""


def test_read_bytes():
    assert isinstance(parse_opml_bytes(data), OPML)


def test_nested_subscription_list():
    o = parse_opml_file('tests/opml/nested-subscription-list.xml')
    assert get_feed_list(o) == [
        'http://1.com/rss.xml',
        'http://2.com/rss.xml',
        'http://3.com/rss.xml',
        'http://4.com/rss.xml',
        'http://5.com/rss.xml',
    ]


def test_missing_outline_title():
    o = parse_opml_file('tests/opml/broken-no-title.xml')
    assert get_feed_list(o) == [
        'https://xkcd.com/rss.xml',
        'http://antirez.com/rss',
        'https://what-if.xkcd.com/feed.atom',
    ]


def test_subscription_list():
    expected = OPML(
        title='mySubscriptions.opml',
        owner_name='Dave Winer',
        owner_email='dave@scripting.com',
        date_created=datetime(2005, 6, 18, 12, 11, 52, tzinfo=tzutc()),
        date_modified=datetime(2005, 8, 2, 21, 42, 48, tzinfo=tzutc()),
        expansion_state=None,
        vertical_scroll_state=1,
        window_top=61,
        window_left=304,
        window_bottom=562,
        window_right=842,
        outlines=[
            OPMLOutline(
                text='CNET News.com',
                type='rss',
                xml_url='http://news.com.com/2547-1_3-0-5.xml',
                description='Tech news and business reports by CNET News.com.',
                html_url='http://news.com.com/',
                language='unknown',
                title='CNET News.com',
                version='RSS2',
                outlines=[]
            ),
            OPMLOutline(
                text='washingtonpost.com - Politics',
                type='rss',
                xml_url='http://www.washingtonpost.com/wp-srv/'
                        'politics/rssheadlines.xml',
                description='Politics',
                html_url='http://www.washingtonpost.com/wp-dyn/'
                         'politics?nav=rss_politics',
                language='unknown',
                title='washingtonpost.com - Politics',
                version='RSS2',
                outlines=[]
            )
        ]
    )
    assert parse_opml_file('tests/opml/subscription-list.xml') == expected


def test_broken_not_xml():
    with pytest.raises(FeedXMLError):
        parse_opml_bytes(b'This is not an XML document')
