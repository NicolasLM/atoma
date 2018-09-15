from datetime import timedelta
from atoma.json_feed import (
    parse_json_feed_file, parse_json_feed_bytes, JSONFeedAttachment
)


def test_attachments():
    parsed = parse_json_feed_file('tests/json_feed/podcast.json')
    expected = JSONFeedAttachment(
        url='http://therecord.co/downloads/The-Record-sp1e1-ChrisParrish.m4a',
        mime_type='audio/x-m4a',
        title=None,
        size_in_bytes=89970236,
        duration=timedelta(seconds=6629)
    )
    assert parsed.items[0].attachments == [expected]


def test_parse_bytes():
    with open('tests/json_feed/jsonfeed.org.json', mode='rb') as f:
        data = f.read()
    parsed = parse_json_feed_bytes(data)
    assert parsed.title == 'JSON Feed'
