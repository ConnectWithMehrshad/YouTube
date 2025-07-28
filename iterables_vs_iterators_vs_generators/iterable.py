from collections.abc import Iterator, Iterable
from typing import Any

class IterableExample:
    def __iter__(self) -> Iterator[Any]:
        pass

isinstance(IterableExample(), Iterable) # --> True
