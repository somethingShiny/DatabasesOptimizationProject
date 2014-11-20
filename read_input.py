# required imports (probably codecs for utf-8 encoding and either stdin or file)
# -*- coding: utf-8 -*-
from sys import stdin
import re


def get_query():
    new_query = re.compile(r'[a-z]\. ')
    nested_query = re.compile(r'(.*)')
    query = stdin.readlines()

    return parse_query(query)
    lines = []
    queries = []
    for line in query:
        line = line.strip('\n')
        if (re.match(new_query, line)):
            add = True
        line = re.sub(new_query, '', line)

        if add:
            queries.append(lines)
            lines = []
            add = False
        lines.append(line)

    grouped_queries = []
    for i in range(1, len(queries)):
        grouped_queries.append(queries[i])

    return grouped_queries


def parse_query(query):
    add = False
    new_query = re.compile(r'[a-z]\. ')
    lines = []
    queries = []

    for line in query:
        line = line.replace(')', '')  #Strip off closing parenthesis from nested queries
        line = line.strip('\n')  #Strip newlines
        if re.match(new_query, line):
            add = True
        line = re.sub(new_query, '', line)
        if add:
            queries.append(lines)
            lines = []
            add = False
        split_lines = line.split('(')
        if (len(split_lines) > 1):
            for line in split_lines:
                if len(line.strip(' ')):
                    lines.append(line)
        else:
            lines.append(line)
    queries.append(lines)
    grouped_queries = []
    for i in range(1, len(queries)):
        grouped_queries.append(queries[i])

    return grouped_queries