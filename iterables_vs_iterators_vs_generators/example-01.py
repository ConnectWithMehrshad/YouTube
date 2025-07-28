from collections.abc import Iterable, Iterator

my_list = ["Connect", "With", "Mehrshad"]
isinstance(my_list, Iterable) # --> True
isinstance(my_list, Iterator) # --> False

my_iterator = iter(my_list)
isinstance(my_iterator, Iterable) # --> True
isinstance(my_iterator, Iterator) # --> True

next(my_iterator) # --> "Connect"
next(my_iterator) # --> "With"
next(my_iterator) # --> "Mehrshad"
next(my_iterator) # --> raises StopIteration
