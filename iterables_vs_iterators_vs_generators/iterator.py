from collections.abc import Iterator, Iterable
from typing import Any

class IteratorExample:
    def __next__(self) -> Any:
        # raise StopIteration to stop the iteration
        pass

    def __iter__(self) -> Iterator[Any]:
        return self

isinstance(IteratorExample(), Iterator) # --> True

isinstance(IteratorExample(), Iterable) # --> True
