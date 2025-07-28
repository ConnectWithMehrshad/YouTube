iterable = ["Connect", "With", "Mehrshad"]

iterator = iter(iterable)
while True:
    try:
        item = next(iterator)
    except StopIteration:
        break

    pass