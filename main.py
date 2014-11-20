#required imports
# -*- coding: utf-8 -*-
from read_input import get_query
from read_input import parse_query
from convert_query import convert
from sys import stdout

PROJECT = 'π'.decode('utf-8')
SELECT = 'σ'.decode('utf-8')


def main():
    print '\n\n'
    query = get_query()
    for q in query:
        for l in q:
            stdout.write(l + '\n')
        print '\n'
    print '\n\n'
    convert(query)
    exit()


if __name__ == '__main__':
    main()