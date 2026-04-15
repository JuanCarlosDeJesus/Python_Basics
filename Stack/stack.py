from collections import deque
from queue import LifoQueue
"""
Stack
Time Complexity:
- push: O(1)
- pop: O(1)
- peek: O(1)
- is_empty: O(1)
- size: O(1)

stack is a linear data structure that follows the Last In First Out (LIFO) principle.
The last element added to the stack will be the first one to be removed.
Operations:
- push: (append()) Add an element to the top of the stack.
- pop: Remove and return the top element of the stack.
- peek: (top()) Return the top element of the stack without removing it.
- is_empty: Check if the stack is empty.
- size: Return the number of elements in the stack.

Example usage:    
"""
# Stack implementation using a list

# Create an empty stack
stack = []
# Push elements onto the stack using append()
stack.append("Welcome")
stack.append("to")
stack.append("Stack")
print(stack)  # Output: ['Welcome', 'to', 'Stack']

# Pop an element from the stack
top_element = stack.pop()
print(top_element)  # Output: Stack
print(stack)  # Output: ['Welcome', 'to']

# Implementation using collections.deque for better performance
# Additional functions like peek, is_empty, and size can be implemented as needed.
# from collections import deque

stack = deque()
stack.append("Welcome")
stack.append("to")
stack.append("Stack")
print(stack)  # Output: deque(['Welcome', 'to', 'Stack'])

# Pop an element from the stack
top_element = stack.pop()
print(top_element)  # Output: Stack
print(stack)  # Output: deque(['Welcome', 'to'])

# Queue module LIFO
# put() method is used to add an element to the stack, and get() method is used to remove an element from the stack.
# maxsize() method is used to set the maximum size of the stack. 
# full() returns True if the stack is full, it will block until space is available.
# qsize() method is used to return the number of elements in the stack.
# from queue import LifoQueue

stack = LifoQueue()
stack.put("Welcome")
stack.put("to")
stack.put("Stack")
print(stack.queue)  # Output: ['Welcome', 'to', 'Stack']

check_stack = LifoQueue(maxsize=3)
check_stack.put("I'm")
check_stack.put("I")
check_stack.put("Full?")
print(stack.qsize())
print(check_stack.full())  # Output: 3
check_stack.get()
print(check_stack.full())  # Output: False

# Pop an element from the stack
top_element = stack.get()
print(top_element)  # Output: Stack
print(stack.queue)  # Output: ['Welcome', 'to']
