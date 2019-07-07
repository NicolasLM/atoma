from datetime import datetime, timedelta, timezone

from dateutil.tz import tzoffset

from atoma.utils import try_parse_date, try_parse_length


def test_try_parse_date():
    expected = datetime(
        2018, 11, 30, 17, 0, tzinfo=timezone(timedelta(seconds=32400))
    )
    assert try_parse_date('Fri, 30 Nov 2018 17:00:00 +0900') == expected

    assert try_parse_date('Fri, 30 Nov 2018 17:00:00:00 +0900') is None

    expected = datetime(2018, 11, 30, 17, 0, tzinfo=timezone.utc)
    assert try_parse_date('Fri, 30 Nov 2018 17:00:00 GMT') == expected
    assert try_parse_date('Fri, 30 Nov 2018 17:00:00 UT') == expected
    assert try_parse_date('Fri, 30 Nov 2018 17:00:00 Z') == expected
    assert try_parse_date('Fri, 30 Nov 2018 17:00:00') == expected

    expected = datetime(2018, 11, 30, 17, 0, tzinfo=tzoffset('PST', -28800))
    assert try_parse_date('Fri, 30 Nov 2018 17:00:00 PST') == expected

    expected = datetime(2018, 10, 10, 18, 0, tzinfo=timezone.utc)
    assert try_parse_date('Web, 10 Oct 2018 18:00:00 +0000') == expected


def test_try_parse_length():
    assert try_parse_length(10) == 10
    assert try_parse_length(545332) == 545332
    assert try_parse_length(10.5633) == 10
    assert try_parse_length('10') == 10

    assert try_parse_length('foo') is None
    assert try_parse_length(-1) is None
    assert try_parse_length(None) is None
