"""
A linked list is a linear collection of nodes 
where each node contains a data value and a reference 
to the next node in the list.

This structure allows for efficient insert and removal of a node at O(1) constant time.
However, accessing and searching for a particular node is linear O(n).

Below implements a singly linked list where each node points to the next node in the list.
"""

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
         self.head = None
    
    # insert node at the end
    def insert(self, data):
        newNode = Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
    
    # print each node in the list
    def printList(self):
        current = self.head
        while(current):
            print(current.data, end=" ")
            current = current.next
    
    # make a loop in the linked list
    def makeLoop(self, k):
        current = self.head
        count = 1
        while (count < k):
            current = current.next
            count += 1
        
        join_pt = current
        
        while (current.next != None) :
            current = current.next
        
        current.next = join_pt
      
    # Floyd's cycle finding algorithm
    # 2 pointers one iterate every 2nd
    # O(n) time complexity
    # O(1) space complexity
    def detectLoop(self):
        tortoise = self.head
        hare = self.head
        loop = False
        while (tortoise and hare and hare.next):
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                loop = True
                break
        if loop:
            print("loop found")
        else:
            print("no loop")
