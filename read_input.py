#required imports (probably codecs for utf-8 encoding and either stdin or file)
from sys import stdin


def get_query():
    query = stdin.readlines()
    return query