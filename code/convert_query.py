#module to convert sql query to relational algebra
# -*- coding: utf-8 -*-

import sys
import re

INTERSECT = ' ∩ '
UNION = ' ∪ '
JOIN = ' ⨝'
PROJECT = 'π '
SELECT = 'σ '
AND = '∧'

def reorder_query(query):
    for i in range(0, len(query) - 1):
        t1 = query[i].lstrip(' ')
        t2 = query[i+1].lstrip(' ')
        if t1.startswith('FROM') and t2.startswith('WHERE'):
            tmp = query[i]
            query[i] = query[i+1]
            query[i+1] = tmp
    return query

def convert(sqlQuery):
    #declare regular expressions to be used later
    pre_join = r'\((.*)' + JOIN
    nested_query = r'\)\)(.*)'
    pre_set_op = r'\)\)(.*)(?=[∩∪-])'
    pre_regex = re.compile(pre_join)
    nested_regex = re.compile(nested_query)
    pre_set_regex = re.compile(pre_set_op)

    reorder_query(sqlQuery)
    relational_query = list()
    for line in sqlQuery:
        line = line.lstrip(' ')
        if line.startswith('SELECT'):
            #if select statement, parse it as such
            relational_query.append(parse_select(line))
        elif line.startswith('FROM'):
            #if from statement, parse it as such
            relational_query.append(parse_from(line))
        elif line.startswith('WHERE'):
            #if where statement, parse it as such
            relational_query.append(parse_where(line))
        else:
            #Default parser for other keywords
            relational_query.append(parse_other(line))


        rel_string = ''.join(relational_query)

    #if a join is found, this takes care of placing the two relations to be joined in the right order
    if rel_string.find(JOIN) != -1:

        pre_matches = pre_regex.findall(rel_string)

        nested_matches = nested_regex.findall(rel_string)

        rel_string = rel_string.replace(pre_matches[0], nested_matches[0])
        rel_string = rel_string.rstrip(nested_matches[0])

        rel_string += '))'



        relational_query = rel_string.split('(')

    #Process SQL line by line, adding relational algebra representation to relational query
    return relational_query


def parse_select(select_statement):
    rel_select = PROJECT + ' '
    rel_select = rel_select + select_statement.strip('SELECT')
    return rel_select


def parse_from(from_statement):
    from_statement = from_statement.replace(',', '')
    rel_from = ' ('
    tokens = from_statement.split()
    #loop through every word
    for i in range(1, len(tokens)):
        token = tokens[i]
        if not from_statement.find('AS') == -1:
            #If the token is AS, omit it
            if token == 'AS':
                pass
            else:
                rel_from = rel_from + token + ' '
            if tokens[i - 1] == 'AS':
                rel_from += ' X '
            else:
                pass
        else:
            rel_from = rel_from + token + ' X '

    rel_from = rel_from.rstrip(' X ')
    rel_from += '))'

    return rel_from


def parse_where(where_statement):
    rel_where = ' (' + SELECT
    tokens = where_statement.split(' ')
    prev_token = ''
    in_found = False
    for i in range(1, len(tokens)):
        token = tokens[i]
        #if IN keyword, remove the previous token
        if token == 'IN':
            in_found = True
            rel_where.replace(prev_token, '')
        elif token == 'AND':
            rel_where += AND + ' '
        else:
            rel_where += token + ' '
            prev_token = token
    #remove extra whitespace
    rel_where = rel_where.rstrip(' ')

    if in_found:
        rel_where += JOIN

    return rel_where


def parse_other(line):
    if line == 'INTERSECT':
        return INTERSECT
    elif line == 'UNION':
        return UNION
    elif line == 'EXCEPT':
        return '-'
    else:
        raise Exception('INVALID CHARACTER FOUND. CONVERSION OF THIS QUERY ABORTED ' + line)