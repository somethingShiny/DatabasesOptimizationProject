# -*- coding: utf-8 -*-
import create_graph
import re

INTERSECT = ' ∩ '
UNION = ' ∪ '
JOIN = ' ⨝'
PROJECT = 'π '
SELECT = 'σ '
AND = '∧'.decode('utf-8')


def optimize(relational_query):
    #Draw initial graph
    create_graph.draw_graph(relational_query)

    #This block optimizes cartesian products followed by select on equality conditions
    #It searches for the character 'X' and equality conditions and replaces them
    #With the keyword JOIN
    for i in range(len(relational_query) - 1):
        if relational_query[i + 1].find('X') != -1:
            parts = relational_query[i].split(AND)
            print parts
            relational_query[i] = ''
            for j in range(len(parts)):
                parts[j] = parts[j].replace("’".decode('utf-8'), '\'')
                if re.search(r'=[0-9]+', parts[j]):
                    relational_query[i] += parts[j]
                elif parts[j].find("'") != -1:
                    relational_query[i] += parts[j]
                else:
                    relational_query[i + 1] = relational_query[i + 1].replace('X', 'JOIN')


    #Draw graph mid-optimization
    create_graph.draw_graph(relational_query)


    #This block optimizes a query by moving selections to happen earlier
    #It looks for selections for matching a constant and switches their position
    #with other statements to reduce the size of the results sooner
    for i in range(len(relational_query) - 1):
        parts = relational_query[i].split(AND)
        for part in parts:
            relational_query[i] = ''
            if part.find("'") != -1:
                table = part.lstrip(' ')[0]
                tmp_str = relational_query[i+1][0:relational_query[i+1].find(table)] + part + relational_query[i+1][relational_query[i+1].find(table):]
                relational_query[i+1] = tmp_str
            elif re.search(r'=[0-9]+', part):
                table = part[0]
                tmp_str = relational_query[i+1][0:relational_query[i+1].find(table)] + part + relational_query[i+1][relational_query[i+1].find(table):]
                relational_query[i+1] = tmp_str
            else:
                relational_query[i] += part
    tmp_query = list()
    for r in relational_query:
        if len(r.strip(' ')):
            tmp_query.append(r)
    relational_query = tmp_query

    #Draw final graph
    create_graph.draw_graph(relational_query)
