class Node:
    def __init__(self, data,key):
        self.item = data
        self.next = None
        self.prev = None
        self.key=key


class DoublyLinkedList:

    def __init__(self):
        self.head=None
        self.tail=None

    def insert_in_empty(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node

    def insert_in_full(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node

    def delete_end_element(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head=None
            return
        n=self.head
        while n.next is not None:
            n=n.next
        n.prev.next=None

    def delete(self,node):
        if node is self.head:
            self.head=node.next
        if node is self.tail:
            self.tail=node.prev
        if node.next:
            node.next.prev=node.prev
        if node.prev:
            node.prev.next=node.next

    def add_to_head(self,data,key):
        if self.head is None:
            self.head=self.tail=Node(data,key)
        else:
            node=Node(data,key)
            node.next=self.head
            self.head.prev=node
            self.head=node












