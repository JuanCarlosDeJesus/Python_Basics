
"""
LinkList 
Collection of nodes, where each node contains data and a reference to the next node in the list.
linear data structure, where each element points to the next, forming a chain of nodes.
Elements are not stored in contiguous memory locations, allowing for dynamic memory allocation and efficient insertion and deletion operations.

Why use LinkList?
Linklist more efficient than list
Elements stored in non-contiguous memory locations, allowing for dynamic memory allocation and efficient insertion and deletion operations.
Accessing elements in a linked list slower
Utilization of memory is higher than list, as it does not require contiguous memory allocation.
List is accessed via index, while linked list is accessed via nodes.

types of linked list:
Singly Linked List: Each node contains a reference to the next node in the list. traversal is done in one direction, from the head to the end of the list.

 head(contains data and reference to next node) -> node1(data and reference to next node) -> node2(data and reference to next node) -> None

Doubly Linked List: Each node contains a reference to both the next and previous nodes in the list.
Circular Linked List: The last node in the list points back to the first node, creating a circular structure.
"""
# Creating a Node class to represent each node in the linked list
class Node:
    def __init__(self, data=None):
        self.data = data  # Store the data
        self.next = None  # Initialize the next reference to None

# n1 = Node(10)
# print(n1.data)  # Output: 10

# Creating a LinkedList class to manage the linked list
class LinkedList:
    def __init__(self):
        self.head = Node()  # Initialize the head of the list to None

    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data
        cur = self.head  # Start from the head
        while cur.next!=None:  # Traverse to the end of the list
            cur = cur.next
        cur.next = new_node  # Set the next reference of the last node to the new node

    def length(self):
        count = 0
        cur = self.head  # Start from the head
        while cur.next!=None:  # Traverse through the list
            count += 1  # Increment the count for each node
            cur = cur.next  # Move to the next node
        return count  # Return the total count of nodes in the list

    def display(self):
        elems = []
        cur_node = self.head  # Start from the head
        while cur_node.next!=None:  # Traverse through the list
            cur_node = cur_node.next  # Move to the next node
            elems.append(cur_node.data)  # Append the data of the current node to the list
        print(elems) # Return the list of elements

# Example usage
sll = LinkedList()

sll.display()

sll.append(1)
sll.append(2)
sll.display()  # Output: []