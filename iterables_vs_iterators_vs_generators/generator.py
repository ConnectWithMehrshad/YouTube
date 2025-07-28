from collections.abc import Generator, Iterator

def generator_example() -> Generator[str, None, None]:
    value = "ConnectWith"
    yield value
    value = "Mehrshad"
    yield value
    return

g = generator_example()
isinstance(g, Generator) # -> True
isinstance(g, Iterator) # -> True

next(g) # -> "ConnectWith"
next(g) # -> "Mehrshad"
next(g) # -> raises StopIteration
