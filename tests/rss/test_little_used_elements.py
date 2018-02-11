from atoma.rss import (
    RSSChannel, RSSItem, RSSEnclosure, RSSSource, RSSImage, parse_rss_file
)


def test_little_used_elements():
    item = RSSItem(
        title='Baz item',
        link=None,
        description=None,
        author=None,
        categories=['Photo', 'Video'],
        comments=None,
        enclosures=[
            RSSEnclosure(
                url='http://dallas.example.com/joebob_050689.mp3',
                length=24986239,
                type='audio/mpeg'
            ),
            RSSEnclosure(
                url='http://dallas.example.com/foo.json',
                length=0,
                type='application/json')
        ],
        guid=None,
        pub_date=None,
        source=RSSSource(
            title='Los Angeles Herald-Examiner',
            url='http://la.example.com/rss.xml'
        ),
        content_encoded='<p>What a <em>beautiful</em> day!</p>'
    )
    expected = RSSChannel(
        title='Foo',
        link='http://foo.bar',
        description='Foo bar.',
        language=None,
        copyright='Public domain',
        managing_editor=None,
        web_master=None,
        pub_date=None,
        last_build_date=None,
        categories=['Media'],
        generator=None,
        docs=None,
        ttl=60,
        image=RSSImage(
            url='http://dallas.example.com/masthead.gif',
            title='Dallas Times-Herald',
            link='http://dallas.example.com',
            width=96,
            height=32,
            description='Read the Dallas Times-Herald'
        ),
        items=[item],
        content_encoded=None
    )
    assert parse_rss_file('tests/rss/little-used-elements.xml') == expected
