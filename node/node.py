"""
                @file           :   node.py
                @authors:       :   @rbstiles   @shubham9482    @mulh8377
                @version:       :   1.0 - 11/11/19      2.0 - 11/26/19
                @description    :   Node.py file that is executed in our docker containers
                @modules        :   grpc, socket, time, logging, sys, configparser, futures
                                    messenger_pb2, messenger_pb2_grpc
"""

from concurrent import futures
import grpc
import socket
import time
import logging
import sys
import threading
import configparser
import csv
import messenger_pb2
import messenger_pb2_grpc

config = configparser.ConfigParser()
config.read('./config.ini')
sections = config.sections()


def generate_gallagher():
    """
    @function_name      :   generate_gallagher
    @parameters         :   empty
    @return             :   total_nodes -> str, port_number -> str
    @description        :   Returns total nodes and the port number
    """
    total_nodes = config[sections[0]]['nodes']
    port_number = config[sections[0]]['port']
    return total_nodes, port_number


# print("Total Nodes: " + total_nodes)
# print("Port-Number: " + port_number)


def generate_links(total_nodes):
    """
    @function_name      :   generate_links
    @parameters         :   total_nodes -> int
    @return             :   results :=  list (node_id -> int, nodes -> str[], weights -> int[])
    @description        :   parses config file into an object that can be read into coordinator
    """
    results = []
    nodes = []
    for i in range(0, total_nodes, 1):
        res = 'node{i}'.format(i=i)
        nodes.append(res)
    for node in config[sections[1]]:
        weight = config[sections[1]][node]
        weights = weight.split('|')
        # weights = np.array(weight.split('|'), int)
        # weights = np.array(weight.split(','), int)
        res = [node, nodes, weights]
        results.append(res)
    return results


def extract_from_str(msg=str):
    msg = msg.strip('[')
    msg = msg.strip(']')
    msg = msg.strip('\'')
    msg = msg.split('\', \'')
    return msg


'''message object that stores info for each message'''


class Message:

    def __init__(self, instruction, content):
        self.instruction = instruction
        self.content = content

    def __str__(self):
        return "Recieved: \"" + str(self.instruction) + "\" Message: " + str(self.content)


'''class to define an edge'''


class Edge:

    def __init__(self, adjacent, weight):
        self.adjacent = adjacent
        self.weight = weight
        self.state = "Basic"

    def __str__(self):
        info = ""
        info += "Adjacent: " + str(self.adjacent) + ", "
        info += "Weight: " + str(self.weight) + ", "
        info += "State: " + str(self.state)

        return info


# coordinator
class coordinator(messenger_pb2_grpc.messengerServicer):
    def __init__(self):
        self.node_info = []
        # self.broadcast_service = None

    def add_info(self, node_id=str, nodes=str, weights=str):
        """
        @function_name      :   add_info
        @parameters         :   node_id -> str, nodes -> str, weights -> str
        @return             :   result := void
        @description        :   appends a nodes info to the coordinator.
        """
        self.node_info.append([node_id, nodes, weights])

    def disperse_neighbors(self):
        """
        @function_name      :   disperse_neighbors
        @parameters         :   none
        @return             :   result := void
        @description        :   creates a channel and sends a message containing the node_id, neighbors[] and weights[]
        """
        for info in self.node_info:
            print(info)
            '''set the channel and create the stub'''
            address = info[0] + ':50051'
            channel = grpc.insecure_channel(address)

            stub = messenger_pb2_grpc.messengerStub(channel)

            msg = messenger_pb2.Msg()
            msg.instruction = 'neighbors'

            msg.content[:] = [info[0], info[1], info[2]]

            response = stub.send(request=msg)

    def initial_wake(self):
        '''set the channel and create the stub'''
        address = 'node0:50051'
        channel = grpc.insecure_channel(address)

        stub = messenger_pb2_grpc.messengerStub(channel)

        msg = messenger_pb2.Msg()
        msg.instruction = 'wakeup'

        msg.content[:] = []

        response = stub.send(request=msg)

    '''starts the coordinator service'''

    def start_coordinator(self):
        """
        @function_name      :   start_coordinator
        @parameters         :   empty
        @return             :   result := void
        @description        :   starts the coordinator server
        """
        '''starts the coordinator'''
        logging.debug('coordinator start')

        '''server object'''
        self.broadcast_service = grpc.server(futures.ThreadPoolExecutor(max_workers=50))

        '''add the service to the server'''
        messenger_pb2_grpc.add_messengerServicer_to_server(self, self.broadcast_service)

        self.broadcast_service.add_insecure_port('[::]:50051')

        self.broadcast_service.start()

        time.sleep(2)

        self.disperse_neighbors()

        self.initial_wake()

        time.sleep(30)


# node
class node(messenger_pb2_grpc.messengerServicer):

    def __init__(self, id, sn="Sleeping", se=[], fn=None, ln=None):
        self.id = id
        self.SN = sn
        self.SE = se
        self.FN = fn
        self.LN = ln
        self.best_edge = Edge(None, None)
        self.best_wt = 99
        self.test_edge = Edge(None, None)
        self.in_branch = Edge(None, None)
        self.find_count = 0

        # fifo message queue
        self.messages = []
        self.message_service = None

        self.channels = {}

    def start_service(self):

        '''Preps the client for incoming connections'''
        # logging.debug('node service start')

        # nodes act like clients and servers since they talk to each other directly
        self.message_service = grpc.server(futures.ThreadPoolExecutor(max_workers=50))

        # Add the service to the node
        messenger_pb2_grpc.add_messengerServicer_to_server(self, self.message_service)

        # bind the service to the port
        self.message_service.add_insecure_port('[::]:50051')

        # start the node service
        self.message_service.start()

        print(self.id + ' is running')

        time.sleep(60)
        branches = [i for i in self.SE if i.state == "Branch"]
        for i in branches:
            print(i)

        time.sleep(2)
        print(self.id + ' has shut down')

    def send_message_to_node(self, instruction, content, nodeToSend):
        """
        @function_name      :   send_message_to_node
        @parameters         :   instruction -> str, content -> str, nodeToSend -> str
        @return             :   result := stub.send(msg)
        @description        :   sends a message to a node given a instruction, content, and node_id
        """

        print("\"" + instruction + "\" request from", content[0], "to", nodeToSend)
        '''set the channel and create the stub'''

        if nodeToSend in self.channels:
            channel = self.channels[nodeToSend]
        else:
            address = nodeToSend + ':50051'
            channel = grpc.insecure_channel(address)
            self.channels[nodeToSend] = channel
        stub = messenger_pb2_grpc.messengerStub(channel)

        msg = messenger_pb2.Msg()
        msg.instruction = instruction

        msg.content[:] = content

        # response = stub.send(request=msg)
        response_future = stub.send.future(request=msg)
        response = response_future.result()

    # deals with the incoming message
    def send(self, message, context):
        """
        @function_name      :   send
        @parameters         :   message -> Message, context
        @return             :   result := MsgAck
        @description        :   initializes a msg receieved and sends an MsgAck back
        """

        recieved = Message(message.instruction, message.content)
        # print(recieved)
        self.recieve(Message(message.instruction, message.content))

        return messenger_pb2.MsgAck()

    # adds incoming message to the queue
    def recieve(self, incoming):
        """
        @function_name      : recieve
        @parameters         : incoming -> Message
        @return             : result := process_message -> function
        @description        : receives a message and sends it to the process_message function
        """

        # logging.debug("send---" + str(incoming) + "--->recieve")

        self.messages.append(incoming)

        for m in self.messages:
            # print("messeges[]: " + str(m))
            time.sleep(.5)
        self.process_message(self.messages.pop(0))

    def add_edges(self, edge_info):
        """
        @function_name      :   add_edges
        @parameters         :   edge_info -> list(str)
        @return             :   result := none
        @description        :   adds edges to a given node.
        """
        # logging.debug("process_message---" + str(edge_info) + "--->add_edges")

        node_ids = extract_from_str(edge_info[1])

        weights = extract_from_str(edge_info[2])

        for i in range(0, len(node_ids)):
            e = Edge(node_ids[i], int(weights[i]))
            # print(e)
            self.SE.append(Edge(node_ids[i], int(weights[i])))

    def wakeup(self, content=None):
        """
        @function_name      :   wakeup
        @parameters         :   empty
        @return             :   result := send_message_to_node -> function
        @description        :   wakes up an initiate mode and sets it's state
                                sends a connect instruction to the smallest adjacent edge.
        """

        smallestEdge = self.SE[0]
        # smallestEdgeIndex = 0
        for i in range(0, len(self.SE)):
            if self.SE[i].weight < smallestEdge.weight:
                smallestEdge = self.SE[i]
                # smallestEdgeIndex = i

        smallestEdge.state = "Branch"
        # self.SE[smallestEdgeIndex].state = "Branch"
        self.LN = 0
        self.SN = "Found"
        self.find_count = 0

        content = [self.id, str(smallestEdge.weight), '0']

        print(self.id, "is now awake.")

        self.send_message_to_node("connect", content, smallestEdge.adjacent)

    def connect(self, content):
        """
        @function_name      :   connect
        @parameters         :   senderNode -> str, sender -> str, L -> int
        @return             :
        @description        :
        """
        senderNode = content[0]
        sender = (e for e in self.SE if str(e.weight) == content[1]).__next__()
        L = int(content[2])

        if self.SN == "Sleeping":
            self.wakeup()

        if L < self.LN:
            sender.state = "Branch"

            content = [self.id, str(sender.weight), str(self.LN), str(self.FN), self.SN]
            self.send_message_to_node("initiate", content, sender.adjacent)
            if self.SN == "Find":
                self.find_count += 1

        elif sender.state == "Basic":
            message = Message("connect", [self.id, str(sender.weight), str(L)])
            self.messages.append(message)
        else:
            content = [self.id, str(sender.weight), str(self.LN + 1), str(sender.weight), "Find"]
            self.send_message_to_node("initiate", content, sender.adjacent)

    def initiate(self, content):
        senderNode = content[0]
        # print("content:",content)
        sender = (e for e in self.SE if str(e.weight) == content[1]).__next__()
        L = int(content[2])
        F = int(content[3])
        S = content[4]
        self.LN = L
        self.FN = F
        self.SN = S
        self.in_branch = sender
        # print("Saving in branch: ", self.in_branch)
        self.best_edge = Edge(None, None)
        self.best_wt = 99

        branches = [e for e in self.SE if e.state == "Branches"]
        for i in range(0, len(branches)):
            if branches[i].weight != sender.weight:
                content = [self.id, str(branches[i].weight), str(L), str(F), S]
                self.send_message_to_node("initiate", content, branches[i].adjacent)
                if S == "Find":
                    self.find_count += 1
        if S == "Find":
            self.test()

    def test(self):
        """
        @function_name      :   test
        @parameters         :   empty
        @return             :
        @description        :
        """
        # print("self.test, location:",self.id)
        basics = [i for i in self.SE if i.state == "Basic"]
        if basics:
            minimumEdge = basics[0]
            for i in range(0, len(basics)):
                if basics[i].weight < minimumEdge.weight:
                    minimumEdge = basics[i]

                self.test_edge = minimumEdge

                content = [self.id, str(minimumEdge.weight), str(self.LN), str(self.FN)]
                self.send_message_to_node("test", content, self.test_edge.adjacent)
        else:
            self.test_edge = Edge(None, None)
            self.report()

    def Test(self, content):
        """
        @function_name      :   Test
        @parameters         :   senderNode, sender, L, F
        @return             :
        @description        :
        """
        senderNode = content[0]
        # print(self)
        # print(content)
        sender = (e for e in self.SE if str(e.weight) == content[1]).__next__()
        L = int(content[2])
        F = int(content[3])

        if self.SN == "Sleeping":
            self.wakeup()
        if L > self.LN:
            message = Message("test", [self.id, str(sender.weight), str(L), str(F)])
            self.messages.append(message)
        elif F != self.FN:
            content = [self.id, str(sender.weight)]
            self.send_message_to_node("accept", content, sender.adjacent)
        else:
            if sender.state == "Basic":
                sender.state = "Rejected"

            if self.test_edge != sender:
                content = [self.id, str(sender.weight)]
                self.send_message_to_node("reject", content, sender.adjacent)
            else:
                self.test()

    def accept(self, content):
        """
        @function_name      :   accept
        @parameters         :   senderNode, sender
        @return             :
        @description        :
        """
        senderNode = content[0]
        sender = (e for e in self.SE if str(e.weight) == content[1]).__next__()
        self.test_edge = Edge(None, None)
        if sender.weight < self.best_wt:
            self.best_edge = sender
            self.best_wt = sender.weight
        self.report()

    def reject(self, content):
        """
        @function_name      :   reject
        @parameters         :   senderNode, sender
        @return             :
        @description        :
        """
        senderNode = content[0]
        sender = (e for e in self.SE if str(e.weight) == content[1]).__next__()
        if sender.state == "Basic":
            sender.state = "Rejected"

        self.test()

    def report(self):
        """
        @function_name      :   report
        @parameters         :   empty
        @return             :
        @description        :
        """
        # print("self.report: \n",self)
        if self.find_count == 0 and self.test_edge == Edge(None, None):
            self.SN = "Found"
            content = [self.id, str(self.best_wt), str(self.in_branch.weight)]
            self.send_message_to_node("report", content, self.in_branch.adjacent)

    def Report(self, content):
        """
        @function_name      :   Report
        @parameters         :   senderNode, bestWeight, inBranch
        @return             :
        @description        :
        """
        # print("self.Report: \n", self)

        senderNode = content[0]
        bestWeight = int(content[1])
        inBranch = (e for e in self.SE if str(e.weight) == content[2]).__next__()
        # print("inBranch.weight:", inBranch.weight)
        if self.in_branch != inBranch:
            # if self.find_count > 0:
            self.find_count -= 1
            if bestWeight < self.best_wt:
                self.best_wt = bestWeight
                self.best_edge = inBranch
            self.report()
        elif self.SN == "Find":
            message = Message("report", [self.id, str(bestWeight), str(inBranch.weight)])
            self.messages.append(message)
        elif bestWeight > self.best_wt:
            self.change_root()
        elif bestWeight == self.best_wt == 99:
            print("Halt")
            return

    def change_root(self):
        """
        @function_name      :   change_root
        @parameters         :   empty
        @return             :
        @description        :
        """

        if self.best_edge.state == "Branch":
            content = [self.id, str(self.best_edge.weight)]
            self.send_message_to_node("change-root", content, self.best_edge.adjacent)

        else:
            content = [self.id, str(self.best_edge.weight), str(self.LN)]
            self.send_message_to_node("connect", content, self.best_edge.adjacent)
            self.best_edge.state = "Branch"


    def Change_root(self, content):
        """
        @function_name      :   Change_root
        @parameters         :   content
        @return             :
        @description        :
        """
        # senderNode = content[0]
        # sender = (e for e in self.SE if str(e.weight) == content[1]).__next__()
        self.change_root()

    # essentially a switch-case for our functions
    def process_message(self, msg=Message):
        print(msg,'\n',self)
        """
        @function_name      :   process_Message
        @parameters         :   msg -> Message
        @return             :
        @description        :
        """
        switcher = {
            "neighbors": self.add_edges,
            "wakeup": self.wakeup,
            "connect": self.connect,
            "initiate": self.initiate,
            "test": self.Test,
            "accept": self.accept,
            "reject": self.reject,
            "report": self.Report,
            "change-root": self.Change_root
        }

        # logging.debug("recieve---" + str(msg.content) + "--->process_message--->function")

        function = switcher.get(msg.instruction, lambda: "nothing")

        return function(msg.content)

        # print override function

    def __str__(self):

        info = "Node ID: " + str(self.id) + '\n'
        info += "SN: " + str(self.SN) + '\n'
        # add all the edges
        info += "SE: \n"
        for j in self.SE:
            info += '\t' + j.__str__() + '\n'

        info += "Fragment ID: " + str(self.FN) + '\n'
        info += "Level: " + str(self.LN) + '\n'
        info += "best-edge: " + str(self.best_edge) + '\n'
        info += "best-wt: " + str(self.best_wt) + '\n'
        info += "test-edge: " + str(self.test_edge) + '\n'
        info += "in-branch: " + str(self.in_branch) + '\n'
        info += "find-count: " + str(self.find_count) + '\n'

        return info


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(levelname)s:%(name)s %(message)s', level=logging.DEBUG)

    if socket.gethostname() == 'coordinator':
        coordinator = coordinator()

        nodes, port = generate_gallagher()
        print("Nodes: " + nodes)
        print("Port: " + port)
        links = generate_links(total_nodes=int(nodes))
        print(links)
        print(links[0])

        for i in range(0, int(nodes), 1):
            active_neighbors = []
            active_weights = []
            for j in range(0, len(links[i][2])):
                if links[i][2][j] != '0':
                    active_neighbors.append(links[i][1][j])
                    active_weights.append(links[i][2][j])
            coordinator.add_info(str(links[i][0]), str(active_neighbors), str(active_weights))

        coordinator.start_coordinator()

    else:
        node = node(socket.gethostname())

        node.start_service()
