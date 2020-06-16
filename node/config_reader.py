"""
                @file           :   config_reader.py

                @authors:       :   mulh8377

                @version:       :   1.0 - 11/11/19

                @description    :   Reads the config.ini and outputs a config.out file.
                                    will be read by our coordinator.

                @modules        :   configparser, numpy, networkx

"""

import configparser
import numpy as np
import networkx as nx

config = configparser.ConfigParser()
config.read('./config.ini')
sections = config.sections()

def generate_gallagher():
    """
    @function_name      :
    @parameters         :
    @return             :
    @description        :
    """
    total_nodes = config[sections[0]]['nodes']
    port_number = config[sections[0]]['port']
    return total_nodes, port_number
#print("Total Nodes: " + total_nodes)
#print("Port-Number: " + port_number)

def generate_links(total_nodes):
    """
    @function_name      :
    @parameters         :
    @return             :
    @description        :
    """
    results = []
    nodes = []
    for i in range(0, total_nodes, 1):
        res = 'node{i}'.format(i=i)
        nodes.append(res)
    for node in config[sections[1]]:
        weight = config[sections[1]][node]
        weights = weight.split('|')
        #weights = np.array(weight.split('|'), int)
        #weights = np.array(weight.split(','), int)
        res = "{},{},{}".format(node, nodes, weights)
        results.append(res)
    return results

def generate_adjacency_matrix(links):
    """
    @function_name      :
    @parameters         :
    @return             :
    @description        :
    """
    return np.array(links)

def generate_graph_from_adj_matrix(matrix):
    """
    @function_name      :
    @parameters         :
    @return             :
    @description        :
    """
    G = nx.from_numpy_matrix(matrix)
    return G

if __name__ == "__main__":
    nodes, port = generate_gallagher()
    print("Nodes: " + nodes)
    print("Port: " + port)
    links = generate_links(total_nodes=int(nodes))
    #print("Links:")
    print(links)
    #print(generate_adjacency_matrix(links))
    #print(adj_matrix)
    #print(adj_matrix)
    #edge_list = generate_graph_from_adj_matrix(adj_matrix)
    #nx.write_adjlist(adj_matrix, 'config.out')              ## store graph edges in config.out :)