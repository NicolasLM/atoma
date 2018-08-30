from datetime import datetime
from io import BytesIO
from typing import Optional, List
from xml.etree.ElementTree import Element

import attr
from defusedxml.ElementTree import parse

from .utils import get_child, get_text, get_int, get_datetime, FeedParseError


@attr.s
class RSSImage:
    url: str = attr.ib()
    title: str = attr.ib()
    link: str = attr.ib()
    width: int = attr.ib()
    height: int = attr.ib()
    description: Optional[str] = attr.ib()


@attr.s
class RSSEnclosure:
    url: str = attr.ib()
    length: int = attr.ib()
    type: str = attr.ib()


@attr.s
class RSSSource:
    title: str = attr.ib()
    url: str = attr.ib()


@attr.s
class RSSItem:
    title: Optional[str] = attr.ib()
    link: Optional[str] = attr.ib()
    description: Optional[str] = attr.ib()
    author: Optional[str] = attr.ib()
    categories: List[str] = attr.ib()
    comments: Optional[str] = attr.ib()
    enclosures: List[RSSEnclosure] = attr.ib()
    guid: Optional[str] = attr.ib()
    pub_date: Optional[datetime] = attr.ib()
    source: Optional[RSSSource] = attr.ib()

    # Extension
    content_encoded: Optional[str] = attr.ib()


@attr.s
class RSSChannel:
    title: str = attr.ib()
    link: str = attr.ib()

    description: Optional[str] = attr.ib()
    language: Optional[str] = attr.ib()
    copyright: Optional[str] = attr.ib()
    managing_editor: Optional[str] = attr.ib()
    web_master: Optional[str] = attr.ib()
    pub_date: Optional[datetime] = attr.ib()
    last_build_date: Optional[datetime] = attr.ib()
    categories: List[str] = attr.ib()
    generator: Optional[str] = attr.ib()
    docs: Optional[str] = attr.ib()
    ttl: Optional[int] = attr.ib()
    image: Optional[RSSImage] = attr.ib()

    items: List[RSSItem] = attr.ib()

    # Extension
    content_encoded: Optional[str] = attr.ib()


def _get_image(element: Element, name,
               optional: bool=True) -> Optional[RSSImage]:
    child = get_child(element, name, optional)
    if child is None:
        return None

    return RSSImage(
        get_text(child, 'url', optional=False),
        get_text(child, 'title', optional=False),
        get_text(child, 'link', optional=False),
        get_int(child, 'width') or 88,
        get_int(child, 'height') or 31,
        get_text(child, 'description')
    )


def _get_source(element: Element, name,
                optional: bool=True) -> Optional[RSSSource]:
    child = get_child(element, name, optional)
    if child is None:
        return None

    return RSSSource(
        child.text.strip(),
        child.attrib['url'],
    )


def _get_enclosure(element: Element) -> RSSEnclosure:
    return RSSEnclosure(
        element.attrib['url'],
        int(element.attrib['length']),
        element.attrib['type'],
    )


def _get_item(element: Element) -> RSSItem:
    root = element

    title = get_text(root, 'title')
    link = get_text(root, 'link')
    description = get_text(root, 'description')
    author = get_text(root, 'author')
    categories = [e.text for e in root.findall('category')]
    comments = get_text(root, 'comments')
    enclosure = [_get_enclosure(e) for e in root.findall('enclosure')]
    guid = get_text(root, 'guid')
    pub_date = get_datetime(root, 'pubDate')
    source = _get_source(root, 'source')

    content_encoded = get_text(root, 'content:encoded')

    return RSSItem(
        title,
        link,
        description,
        author,
        categories,
        comments,
        enclosure,
        guid,
        pub_date,
        source,
        content_encoded
    )


def _parse_rss(root: Element) -> RSSChannel:
    rss_version = root.get('version')
    if rss_version != '2.0':
        raise FeedParseError('Cannot process RSS feed version "{}"'
                             .format(rss_version))

    root = root.find('channel')

    # Mandatory
    title = get_text(root, 'title', optional=False)
    link = get_text(root, 'link', optional=False)

    # Optional
    description = get_text(root, 'description')
    language = get_text(root, 'language')
    copyright = get_text(root, 'copyright')
    managing_editor = get_text(root, 'managingEditor')
    web_master = get_text(root, 'webMaster')
    pub_date = get_datetime(root, 'pubDate')
    last_build_date = get_datetime(root, 'lastBuildDate')
    categories = [e.text for e in root.findall('category')]
    generator = get_text(root, 'generator')
    docs = get_text(root, 'docs')
    ttl = get_int(root, 'ttl')

    image = _get_image(root, 'image')
    items = [_get_item(e) for e in root.findall('item')]

    content_encoded = get_text(root, 'content:encoded')

    return RSSChannel(
        title,
        link,
        description,
        language,
        copyright,
        managing_editor,
        web_master,
        pub_date,
        last_build_date,
        categories,
        generator,
        docs,
        ttl,
        image,
        items,
        content_encoded
    )


def parse_rss_file(filename: str) -> RSSChannel:
    """Parse an RSS feed from a local XML file."""
    root = parse(filename).getroot()
    return _parse_rss(root)


def parse_rss_bytes(data: bytes) -> RSSChannel:
    """Parse an RSS feed from a byte-string containing XML data."""
    root = parse(BytesIO(data)).getroot()
    return _parse_rss(root)
