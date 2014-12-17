# -*- coding: utf-8 -*-
import codecs
import os

INTERSECT = '∩'.decode('utf-8')
UNION = '∪'.decode('utf-8')
JOIN = '⨝'.decode('utf-8')
PROJECT = 'π'.decode('utf-8')
SELECT = 'σ'.decode('utf-8')
AND = '∧'.decode('utf-8')



def draw_graph(relation_query):
    i = 0
    join_positions = list()


    edges = {}

    #find first number i for which a file queryi.gv does not exist
    while os.path.isfile('output/query' + str(i) + '.gv'):
        i += 1

    #open file
    file = codecs.open('output/query' + str(i) + '.gv', 'w', 'utf-8')
    i = 0
    file.write('digraph G {\n')
    file.write('node [ color="transparent" ]\n')
    file.write('edge [ dir=none ]\n')

    for line in relation_query:
        #replace special characters with words
        line = line.decode('utf-8').replace(UNION, 'UNION')
        line = line.replace(PROJECT, 'PROJECT')
        line = line.replace(INTERSECT, 'INTERSECT')
        line = line.replace(AND, 'AND')
        line = line.replace(SELECT, 'SELECT')
        line = line.replace(JOIN, 'JOIN')


        #if there's a cartesian product, split it and create the nodes and edges
        if line.find('X') > -1:
            parts = line.split('X')
            file.write('node' + str(i) + ' [ label="X" ]\n')
            join_position = i
            join_positions.append(join_position)
            i += 1
            join_positions.append(i)


            if len(parts) == 3:
                file.write('node' + str(i) + ' [ label="' + parts[0] + '" ]\n')
                edges['node'+str(join_position)] = list()
                edges['node'+str(join_position)].append('node'+str(i))
                i += 1
                join_positions.append(i)
                file.write('node' + str(i) + ' [ label="' + 'X' + '" ]\n')
                join_position_2 = i
                edges['node'+str(join_position_2)] = list()
                edges['node'+str(join_position)].append('node' + str(join_position_2))
                join_positions.append(i)
                i += 1

                file.write('node' + str(i) + ' [ label="' + parts[1] + '" ]\n')
                edges['node'+str(join_position_2)].append('node' + str(i))
                join_positions.append(i)
                i += 1

                file.write('node' + str(i) + ' [ label="' + parts[2] + '" ]\n')
                edges['node'+str(join_position_2)].append('node' + str(i))

                join_positions.append(i)
                i += 1
            else:
                file.write('node' + str(i) + ' [ label="' + parts[0] + '" ]\n')
                edges['node'+str(join_position)] = list()
                edges['node'+str(join_position)].append('node'+str(i))
                i += 1
                join_positions.append(i)
                file.write('node' + str(i) + ' [ label="' + parts[1] + '" ]\n')
                edges['node'+str(join_position)].append('node' + str(i))
                i += 1
                join_positions.append(i)
#moved join_positions.append(i) to after i+=1 to catch i =1
        elif line.find('JOIN') > -1:
            parts = line.split('JOIN')
            file.write('node' + str(i) + ' [ label="JOIN" ]\n')
            edges['node'+str(i)] = list()

            join_position = i
            join_positions.append(join_position)
            i += 1
            join_positions.append(i)


            if len(parts) == 3:
                if parts[0].find('|') > -1:
                    pieces = parts[0].split('|')
                    file.write('node' + str(i) + ' [ label="' + pieces[0] + '" ]\n')
                    # edges['node'+str(join_position)] = list()
                    edges['node'+str(join_position)].append('node'+str(i))
                    i += 1
                    join_positions.append(i)

                    file.write('node' + str(i) + ' [ label="' + pieces[1] + '" ]\n')
                    edges['node'+str(i-1)] = list()
                    edges['node'+str(i-1)].append('node'+str(i))
                    i += 1
                    join_positions.append(i)

                else:
                    file.write('node' + str(i) + ' [ label="' + parts[0] + '" ]\n')
                    # edges['node'+str(join_position)] = list()
                    edges['node'+str(join_position)].append('node'+str(i))
                    i += 1
                    join_positions.append(i)




                file.write('node' + str(i) + ' [ label="' + 'JOIN' + '" ]\n')
                join_position_2 = i
                edges['node'+str(join_position_2)] = list()
                edges['node'+str(join_position)].append('node' + str(join_position_2))
                join_positions.append(i)
                i += 1



                if parts[1].find('|') > -1:
                    pieces = parts[1].split('|')
                    file.write('node' + str(i) + ' [ label="' + pieces[0] + '" ]\n')

                    edges['node'+str(join_position_2)].append('node'+str(i))
                    i += 1
                    join_positions.append(i)

                    file.write('node' + str(i) + ' [ label="' + pieces[1] + '" ]\n')
                    edges['node'+str(i-1)] = list()
                    edges['node'+str(i-1)].append('node'+str(i))

                    join_positions.append(i-1)
                    i += 1
                else:
                    file.write('node' + str(i) + ' [ label="' + parts[1] + '" ]\n')
                    edges['node'+str(join_position_2)].append('node' + str(i))
                    join_positions.append(i)
                    i += 1

                if parts[2].find('|') > -1:
                    pieces = parts[2].split('|')
                    file.write('node' + str(i) + ' [ label="' + pieces[0] + '" ]\n')

                    edges['node'+str(join_position_2)].append('node'+str(i))
                    i += 1
                    join_positions.append(i)

                    file.write('node' + str(i) + ' [ label="' + pieces[1] + '" ]\n')
                    edges['node'+str(i-1)] = list()
                    edges['node'+str(i-1)].append('node'+str(i))

                    join_positions.append(i-1)
                    i += 1
                else:
                    file.write('node' + str(i) + ' [ label="' + parts[2] + '" ]\n')
                    edges['node'+str(join_position_2)].append('node' + str(i))

                join_positions.append(i)
                i += 1
            else:
                if parts[0].find('|') > -1:
                    pieces = parts[0].split('|')
                    file.write('node' + str(i) + ' [ label="' + pieces[0] + '" ]\n')
                    # edges['node'+str(join_position)] = list()
                    edges['node'+str(join_position)].append('node'+str(i))
                    i += 1
                    join_positions.append(i)

                    file.write('node' + str(i) + ' [ label="' + pieces[1] + '" ]\n')
                    edges['node'+str(i-1)] = list()
                    edges['node'+str(i-1)].append('node'+str(i))

                    join_positions.append(i)
                    i += 1
                else:
                    file.write('node' + str(i) + ' [ label="' + parts[0] + '" ]\n')
                    # edges['node'+str(join_position)] = list()
                    edges['node'+str(join_position)].append('node'+str(i))
                    i += 1
                    join_positions.append(i)

                if parts[1].find('|') > -1:
                    pieces = parts[1].split('|')
                    file.write('node' + str(i) + ' [ label="' + pieces[0] + '" ]\n')
                    # edges['node'+str(join_position)] = list()
                    edges['node'+str(join_position)].append('node'+str(i))
                    i += 1
                    join_positions.append(i)

                    file.write('node' + str(i) + ' [ label="' + pieces[1] + '" ]\n')
                    edges['node'+str(i-1)] = list()
                    edges['node'+str(i-1)].append('node'+str(i))

                    join_positions.append(i)
                    i += 1

                else:
                    file.write('node' + str(i) + ' [ label="' + parts[1] + '" ]\n')
                    # edges['node'+str(join_position)] = list()
                    edges['node'+str(join_position)].append('node'+str(i))
                    i += 1
                    join_positions.append(i)


#moved join_positions.append(i) to after i+=1 to catch i =1
        else:
            if line == 'UNION':
                edges['node'+str(i)] = list()
                edges['node'+str(i)].append('node'+str(0))
            elif line == 'INTERSECT':
                edges['node'+str(i)] = list()
                edges['node'+str(i)].append('node'+str(0))
            elif line == '-':
                edges['node'+str(i)] = list()
                edges['node'+str(i)].append('node'+str(0))
            file.write('node' + str(i) + ' [ label="' + line + '" ]\n')
            i += 1
#create edge that links node(i-1) to node (i-2)
#keep track of all nodes created
    total_nodes = i
    i = 0

    #add needed edges to edges dict
    try:
        join_positions[0] = join_positions[0]
    except IndexError:
        join_positions.append(total_nodes)
    for i in range(join_positions[0]):
        if i in join_positions and i + 1 in join_positions:
            pass
        elif i in join_positions:
            pass
        else:
            try:
                edges['node' + str(i)].append('node' + str(i+1))
            except KeyError:
                edges['node' + str(i)] = 'node' + str(i+1)
    for i in range(join_positions[0], total_nodes):
        if i == join_positions[0] + 1:
            pass
        else:
            if i in join_positions and i + 1 in join_positions:
                pass
            elif i in join_positions:
                pass
            else:
                try:
                    edges['node' + str(i)].append('node' + str(i+1))
                except KeyError:
                    edges['node' + str(i)] = 'node' + str(i+1)

    #write in all edges
    for key in edges:
        if isinstance(edges[key], list):
            for edge in edges[key]:
                file.write(key + '->' + edge + '\n')
        else:
            file.write(key + '->' + edges[key] + '\n')
    file.write('}\n')

    #close file
    file.close()


