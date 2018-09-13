"""Simple API that abstracts away the differences between feed types."""

from datetime import datetime
from typing import Optional, List, Tuple

import attr

from . import atom, rss, json_feed
from .utils import FeedParseError, FeedXMLError, FeedJSONError


@attr.s
class Article:
    id: str = attr.ib()
    title: str = attr.ib()
    link: str = attr.ib()
    content: str = attr.ib()
    published_at: Optional[datetime] = attr.ib()
    updated_at: Optional[datetime] = attr.ib()


@attr.s
class Feed:
    title: str = attr.ib()
    subtitle: Optional[str] = attr.ib()
    link: Optional[str] = attr.ib()
    updated_at: Optional[datetime] = attr.ib()
    articles: List[Article] = attr.ib()


def _adapt_atom_feed(atom_feed: atom.AtomFeed) -> Feed:
    articles = list()
    for entry in atom_feed.entries:
        if entry.content is not None:
            content = entry.content.value
        elif entry.summary is not None:
            content = entry.summary.value
        else:
            content = ''
        published_at, updated_at = _get_article_dates(entry.published,
                                                      entry.updated)
        articles.append(Article(
            entry.id_,
            entry.title.value,
            entry.links[0].href,
            content,
            published_at,
            updated_at
        ))

    try:
        link = atom_feed.links[0].href
    except IndexError:
        link = None

    return Feed(
        atom_feed.title.value if atom_feed.title else atom_feed.id_,
        atom_feed.subtitle.value if atom_feed.subtitle else None,
        link,
        atom_feed.updated,
        articles
    )


def _adapt_rss_channel(rss_channel: rss.RSSChannel) -> Feed:
    articles = list()
    for item in rss_channel.items:
        articles.append(Article(
            item.guid or item.link,
            item.title,
            item.link,
            item.content_encoded or item.description or '',
            item.pub_date,
            None
        ))

    if rss_channel.title is None and rss_channel.link is None:
        raise FeedParseError('RSS feed does not have a title nor a link')

    return Feed(
        rss_channel.title if rss_channel.title else rss_channel.link,
        rss_channel.description,
        rss_channel.link,
        rss_channel.pub_date,
        articles
    )


def _adapt_json_feed(json_feed: json_feed.JSONFeed) -> Feed:
    articles = list()
    for item in json_feed.items:
        articles.append(Article(
            item.id_,
            item.title,
            item.url,
            item.content_html or item.content_text or '',
            item.date_published,
            item.date_modified
        ))

    return Feed(
        json_feed.title,
        json_feed.description,
        json_feed.feed_url,
        None,
        articles
    )


def _get_article_dates(published_at: Optional[datetime],
                       updated_at: Optional[datetime]
                       ) -> Tuple[Optional[datetime], Optional[datetime]]:
    if published_at and updated_at:
        return published_at, updated_at

    if updated_at:
        return updated_at, None

    if published_at:
        return published_at, None

    raise FeedParseError('Article does not have proper dates')


def simple_parse_file(filename: str) -> Feed:
    """Parse an Atom, RSS or JSON feed from a local file."""
    pairs = (
        (rss.parse_rss_file, _adapt_rss_channel),
        (atom.parse_atom_file, _adapt_atom_feed),
        (json_feed.parse_json_feed_file, _adapt_json_feed)
    )
    for parser, adapter in pairs:
        try:
            return adapter(parser(filename))
        except (FeedParseError, FeedXMLError, FeedJSONError):
            continue

    raise FeedParseError('File is not a valid supported feed')


def simple_parse_bytes(data: bytes) -> Feed:
    """Parse an Atom, RSS or JSON feed from a byte-string containing data."""
    pairs = (
        (rss.parse_rss_bytes, _adapt_rss_channel),
        (atom.parse_atom_bytes, _adapt_atom_feed),
        (json_feed.parse_json_feed_bytes, _adapt_json_feed)
    )
    for parser, adapter in pairs:
        try:
            return adapter(parser(data))
        except (FeedParseError, FeedXMLError, FeedJSONError):
            continue

    raise FeedParseError('Data is not a valid supported feed')
