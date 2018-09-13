import datetime

from dateutil.tz import tzoffset

from atoma.json_feed import (
    parse_json_feed_file, JSONFeed, JSONFeedAuthor, JSONFeedItem
)

content_html = (
    '<p>We —\xa0Manton Reece and Brent Simmons —\xa0have noticed that JSON '
    'has become the developers’ choice for APIs, and that developers will '
    'often go out of their way to avoid XML. JSON is simpler to read and '
    'write, and it’s less prone to bugs.</p>\n\n<p>So we developed JSON Feed, '
    'a format similar to <a href="http://cyber.harvard.edu/rss/rss.html">'
    'RSS</a> and <a href="https://tools.ietf.org/html/rfc4287">Atom</a> but '
    'in JSON. It reflects the lessons learned from our years of work reading '
    'and publishing feeds.</p>\n\n<p><a href="https://jsonfeed.org/version/1">'
    'See the spec</a>. It’s at version 1, which may be the only version ever '
    'needed. If future versions are needed, version 1 feeds will still be '
    'valid feeds.</p>\n\n<h4>Notes</h4>\n\n<p>We have a <a href="https://'
    'github.com/manton/jsonfeed-wp">WordPress plugin</a> and, coming soon, a '
    'JSON Feed Parser for Swift. As more code is written, by us and others, '
    'we’ll update the <a href="https://jsonfeed.org/code">code</a> page.</p>'
    '\n\n<p>See <a href="https://jsonfeed.org/mappingrssandatom">Mapping RSS '
    'and Atom to JSON Feed</a> for more on the similarities between the '
    'formats.</p>\n\n<p>This website —\xa0the Markdown files and supporting '
    'resources —\xa0<a href="https://github.com/brentsimmons/JSONFeed">is up '
    'on GitHub</a>, and you’re welcome to comment there.</p>\n\n<p>This '
    'website is also a blog, and you can subscribe to the <a href="https://'
    'jsonfeed.org/xml/rss.xml">RSS feed</a> or the <a href="https://'
    'jsonfeed.org/feed.json">JSON feed</a> (if your reader supports it).'
    '</p>\n\n<p>We worked with a number of people on this over the course of '
    'several months. We list them, and thank them, at the bottom of the <a '
    'href="https://jsonfeed.org/version/1">spec</a>. But — most importantly — '
    '<a href="http://furbo.org/">Craig Hockenberry</a> spent a little time '
    'making it look pretty. :)</p>\n'
)


def test_rfc_minimal():
    expect = JSONFeed(
        version='https://jsonfeed.org/version/1',
        title='JSON Feed',
        home_page_url='https://jsonfeed.org/',
        feed_url='https://jsonfeed.org/feed.json',
        description='JSON Feed is a pragmatic syndication format for blogs, '
                    'microblogs, and other time-based content.',
        user_comment='This feed allows you to read the posts from this site '
                     'in any feed reader that supports the JSON Feed format. '
                     'To add this feed to your reader, copy the following URL '
                     '— https://jsonfeed.org/feed.json — and add it your '
                     'reader.',
        next_url=None,
        icon=None,
        favicon=None,
        author=JSONFeedAuthor(
            name='Brent Simmons and Manton Reece',
            url='https://jsonfeed.org/',
            avatar=None
        ),
        expired=False,
        items=[JSONFeedItem(
            id_='https://jsonfeed.org/2017/05/17/announcing_json_feed',
            url='https://jsonfeed.org/2017/05/17/announcing_json_feed',
            external_url=None,
            title='Announcing JSON Feed',
            content_html=content_html,
            content_text=None,
            summary=None,
            image=None,
            banner_image=None,
            date_published=datetime.datetime(2017, 5, 17, 8, 2, 12,
                                             tzinfo=tzoffset(None, -25200)),
            date_modified=None,
            author=None,
            tags=[],
            attachments=[])]
    )
    assert parse_json_feed_file('tests/json_feed/jsonfeed.org.json') == expect
