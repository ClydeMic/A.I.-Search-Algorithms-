# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 15:43:06 2020

@author: Clyde007
"""
import Heap as h

PRIORITY = 0
PATH = 2
NODE= 1  
class UCSTraverser:
    def createVisitedNodes(self):
        self.visitedNodes = dict.fromkeys(self.vertices, False)  # intializes all to false to begin

    def visitNode(self, node):
        self.visitedNodes[node] = True


    def UCS(self, root, goal):
        frontier = h.PriorityQueue()
        frontier.enqueue((0, root, root))  # (priority, currnode, path)
        while (not (frontier.empty())):  # iterates till queue is empty otherwise until all nodes are exhausted
            print(frontier.queue)
            node = frontier.dequeue()
            if (node[NODE] in goal):  # if the current node in queue is equal to goal then we have print path
                print(node[PATH] + " Cost: " + str(node[PRIORITY]))  # prints path
                break
            elif(self.visitedNodes[node[NODE]]):
                continue #next iteration node has already been expanded
            else:
                self.visitNode(node[NODE])
                children = self.edges[node[NODE]]

                for childnode in children:
                    if (self.visitedNodes[childnode[NODE]] is not True):
                        frontier.enqueue((childnode[PRIORITY] + node[PRIORITY], childnode[NODE], node[PATH] + "->" + str(childnode[NODE])))  # enques all of the node children
                    else:
                        continue


  
