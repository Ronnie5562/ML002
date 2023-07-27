#!/usr/bin/python3
"""This module define classes for singly-linked list impementation"""


class Node:
    """Objs of this clsass represents a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.__data = data
        self.__next_node = next_node
        
    @property
    """property(get&set) for the data of the Node."""
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        if (not isinstance(value, int)):
            raise TypeError("data must be an integer")
        self.__data = value
    
    @property
    """property(get&set) for the next_node."""
    def next_node(self):
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        if (not isinstance(value, Node) and value is not None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value
    
class SinglyLinkedList:
    """This class represents a singly-linked list."""

    def __init__(self):
        """Initialize a new SinglyLinkedList."""
        self.__head = None
    
    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.

        The node is inserted into the list at the sorted
        position in the list (increasing order)

        Args:
            value (Node): The new Node to insert.
        """
        new_node = Node(value)
        if self.__head == None:
            self.__head = new_node
        elif self.__head.data > new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current_node = self.__head
            while (current_node.next_node is not None and
            current_node.next_node.data < value):
                current_node = current_node.next_node
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node
    
    def __str__(self):
        """Defines the print() representation of a SinglyLinkedList obj"""
        node_list = []
        current_node = self.__head
        while (current_node is not None):
            node_list.append(str(current_node.data))
            current_node = current_node.next_node
        return '\n'.join(node_list)