#required imports
# -*- coding: utf-8 -*-
from read_input import get_query
from convert_query import convert



def main():
    print '\n\n'
    query = get_query()
    for q in query:
        try:
            convert(q)
        except IndexError, e:
            print e
            print '\n'

    exit()


if __name__ == '__main__':
    main()