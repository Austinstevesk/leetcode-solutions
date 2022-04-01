
# Online Python - IDE, Editor, Compiler, Interpreter


# operations: pop, push, shift, reverse
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def push(self, value):
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
        self.length += 1
        self.tail.next = Node(value)
        self.tail = Node(value)
        
        return self
    
    
    # remove the last element    
    def pop(self):
        if not self.head:
            return None
            
        current_node = self.head
        new_tail = current_node
        
        while(current_node.next):
            new_tail = current_node
            current_node = current_node.next
        self.tail = new_tail
        self.tail.next = None
        self.length -= 1
        
        if (self.length == 0):
            self.head = None
            self.tail = None
        
        return self
        
    # removing the node at the beginning
    def shift(self):
        if not self.head:
            return None
            
        #
        self.head = self.head.next
        self.length -= 1
        return self
        
        
    # adding elements to the beginning of the list/head
    def unshift(self, value):
        # check whether the LinkedList is empty
        if not self.head:
            self.head = Node(value)
            self.head = Node(value)
            
        # we need a temp to make sure we store self.head, so that we can point the new node's tail to the current head we have
        temp = self.head
        self.head.next = temp
        self.head = Node(value)
        self.length += 1
        
        return self
        
        
    def reverse(self):
        """1 -> 2 -> 3 -> 4
        4 -> 3 -> 2 -> 1
        
        head should now be tail, tail should now be head
        tail -> 1
        head -> 4
        prev = None
        next = None
        current_node = None
        """
        
        prev = next = None
        current_node = self.head
        self.head = self.tail
        
        while current_node:
            next = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next
            
        return self
        
    
    # def print_nodes(self):
    #   while(self.head):
    #       print(self.value)
    #       self.head = self.head.next
           
        
llist = LinkedList()
llist.push(1)
print(llist.push(3))

#llist.print_nodes()
        
