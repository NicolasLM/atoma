"""Simple API that abstracts away Atom and RSS feeds."""

from datetime import datetime
from typing import Optional, List, Tuple

import attr

from . import atom, rss
from .utils import FeedParseError


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
    link: str = attr.ib()
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
        atom_feed.title.value,
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
    return Feed(
        rss_channel.title,
        rss_channel.description,
        rss_channel.link,
        rss_channel.pub_date,
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
    """Parse an Atom or RSS feed from a local XML file."""
    try:
        return _adapt_rss_channel(rss.parse_rss_file(filename))
    except FeedParseError:
        try:
            return _adapt_atom_feed(atom.parse_atom_file(filename))
        except FeedParseError:
            raise FeedParseError('File is not a valid Atom nor RSS feed')


def simple_parse_bytes(data: bytes) -> Feed:
    """Parse an Atom or RSS feed from a byte-string containing XML data."""
    try:
        return _adapt_rss_channel(rss.parse_rss_bytes(data))
    except FeedParseError:
        try:
            return _adapt_atom_feed(atom.parse_atom_bytes(data))
        except FeedParseError:
            raise FeedParseError('File is not a valid Atom nor RSS feed')
