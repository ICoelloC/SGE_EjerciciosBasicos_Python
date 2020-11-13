#! /usr/bin/env python
from itertools import islice


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    print(list(islice(fibonacci(), 10)))
