#required imports
# -*- coding: utf-8 -*-
from read_input import get_query
from read_input import parse_query
from convert_query import convert
from optimization import optimize
from sys import stdout

PROJECT = 'π'.decode('utf-8')
SELECT = 'σ'.decode('utf-8')

def main():
    query = get_query()
#     query = ["""SELECT sname
# FROM Sailors, Boats, Reserves
# WHERE Sailors.sid=Reserves.sid AND Reserves.bid=Boats.bid AND  Boats.color='red'
# UNION
# SELECT sname
# FROM Sailors, Boats, Reserves
# WHERE Sailors.sid=Reserves.sid AND Reserves.bid=Boats.bid AND Boats.color='green'
# """.splitlines()]
    for q in query:
        for l in q:
            stdout.write(l + '\n')
        print '\n'
    print '\n\n'

    rel_al_query = []

    for q in query:
        rel_al_query.append(convert(q))

    for q in rel_al_query:
        print q

        optimize(q)

    exit()


if __name__ == '__main__':
    main()