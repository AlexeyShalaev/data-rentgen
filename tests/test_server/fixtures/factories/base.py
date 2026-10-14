from __future__ import annotations

from datetime import UTC, datetime
from random import randrange
from string import ascii_letters, digits, punctuation

letters = ascii_letters + digits + punctuation + " "


def random_string(length: int = 16) -> str:
    return "".join(letters[randrange(0, len(letters))] for _ in range(length))


def random_datetime(
    start: datetime | None = None,
    end: datetime | None = None,
) -> datetime:
    if not start:
        start = datetime.fromtimestamp(0, tz=UTC)
    if not end:
        end = datetime.now(tz=UTC)
    return datetime.fromtimestamp(randrange(int(start.timestamp()), int(end.timestamp())), tz=start.tzinfo)
