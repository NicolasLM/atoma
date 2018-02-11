from datetime import datetime

from dateutil.tz import tzutc

from atoma.rss import RSSChannel, RSSItem, parse_rss_file


def test_specification():
    item_1 = RSSItem(
        title='Star City',
        link='http://liftoff.msfc.nasa.gov/news/2003/news-starcity.asp',
        description='How do Americans get ready to work with Russians aboard\n'
                    '                the International Space Station? They tak'
                    'e a crash course in\n                culture, language'
                    ' and protocol at Russia\'s <a\n                '
                    'href="http://howe.iki.rssi.ru/GCTC/gctc_e.htm">Star '
                    'City</a>.',
        author=None,
        categories=[],
        comments=None,
        enclosures=[],
        guid='http://liftoff.msfc.nasa.gov/2003/06/03.html#item573',
        pub_date=datetime(2003, 6, 3, 9, 39, 21, tzinfo=tzutc()),
        source=None,
        content_encoded=None
    )
    item_2 = RSSItem(
        title=None,
        link=None,
        description='Sky watchers in Europe, Asia, and parts of Alaska and\n  '
                    '              Canada will experience a <a\n              '
                    '  href="http://science.nasa.gov/headlines/y2003/30may_sol'
                    'areclipse.htm">partial\n                eclipse of the '
                    'Sun</a> on Saturday, May 31st.',
        author=None,
        categories=[],
        comments=None,
        enclosures=[],
        guid='http://liftoff.msfc.nasa.gov/2003/05/30.html#item572',
        pub_date=datetime(2003, 5, 30, 11, 6, 42, tzinfo=tzutc()),
        source=None,
        content_encoded=None
    )
    item_3 = RSSItem(
        title='The Engine That Does More',
        link='http://liftoff.msfc.nasa.gov/news/2003/news-VASIMR.asp',
        description='Before man travels to Mars, NASA hopes to design new\n   '
                    '             engines that will let us fly through the '
                    'Solar System more\n                quickly.\n          '
                    '      The proposed VASIMR engine would do that.',
        author=None,
        categories=[],
        comments=None,
        enclosures=[],
        guid='http://liftoff.msfc.nasa.gov/2003/05/27.html#item571',
        pub_date=datetime(2003, 5, 27, 8, 37, 32, tzinfo=tzutc()),
        source=None,
        content_encoded=None
    )
    item_4 = RSSItem(
        title="Astronauts' Dirty Laundry",
        link='http://liftoff.msfc.nasa.gov/news/2003/news-laundry.asp',
        description='Compared to earlier spacecraft, the International Space\n'
                    '                Station has many luxuries, but laundry '
                    'facilities are not one of\n                them. Instead,'
                    ' astronauts have other options.',
        author=None,
        categories=[],
        comments=None,
        enclosures=[],
        guid='http://liftoff.msfc.nasa.gov/2003/05/20.html#item570',
        pub_date=datetime(2003, 5, 20, 8, 56, 2, tzinfo=tzutc()),
        source=None,
        content_encoded=None
    )

    expected = RSSChannel(
        title='Liftoff News',
        link='http://liftoff.msfc.nasa.gov/',
        description='Liftoff to Space Exploration.',
        language='en-us',
        copyright=None,
        managing_editor='editor@example.com',
        web_master='webmaster@example.com',
        pub_date=datetime(2003, 6, 10, 4, 0, tzinfo=tzutc()),
        last_build_date=datetime(2003, 6, 10, 9, 41, 1, tzinfo=tzutc()),
        categories=[],
        generator='Weblog Editor 2.0',
        docs='http://blogs.law.harvard.edu/tech/rss',
        ttl=None,
        image=None,
        items=[item_1, item_2, item_3, item_4],
        content_encoded=None
    )
    assert parse_rss_file('tests/rss/specification.xml') == expected
