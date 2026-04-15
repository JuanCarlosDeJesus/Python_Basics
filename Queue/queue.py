import queue  # Importing the built-in queue module for demonstration purposes
"""
Queue
Time Complexity: O(1) for enqueue and dequeue operations.

Linear data structure that follows the First In First Out (FIFO) principle.
The first element added to the queue will be the first one to be removed.
Insertion happens at the rear end and deletion happens at the front end.
Operations:

- enqueue(element): Add an element to the rear of the queue.
- dequeue(): Remove and return the front element of the queue.
- peek(): Return the front element of the queue without removing it.
- is_empty(): Check if the queue is empty.
- size: Return the number of elements in the queue.

Disadvantages:
- Limited access: Only the front and rear elements can be accessed directly.
- Memory usage: If implemented using an array, it may require resizing when the queue is full.
"""
# import queue

q = queue.Queue()  # Create a queue object
numbers = [1, 2, 3, 4, 5]
print("Enqueueing element with put():", numbers)
for num in numbers:
    q.put(num)  # Enqueue elements
print("Print q with list():", list(q.queue))
print("Queue size with qsize():", q.qsize())  # Output: Queue size: 5
print("Front element with queue[0]:", q.queue[0])  # Output: Front element: 1

print("Dequeue element with get():", q.get())  # Output: Dequeue element: 1
print("Queue size after dequeue:", q.qsize())  # Output: Queue size after dequeue: 4

print("Is the queue empty with empty()?", q.empty())  # Output: Is the queue empty?

"""
LifoQueue
Time Complexity: O(1) for push and pop operations.
Linear data structure that follows the Last In First Out (LIFO) principle.
The last element added to the stack will be the first one to be removed.
"""
# import queue
lifo_q = queue.LifoQueue()  # Create a LifoQueue object
print("Enqueueing element with put():", numbers)
for num in numbers:
    lifo_q.put(num)  # Enqueue elements
print("Print lifo_q with list():", list(lifo_q.queue))
print("Stack size with qsize():", lifo_q.qsize())  # Output: Stack size: 5
print("Top element with queue[-1]:", lifo_q.queue[-1])  # Output: Top element: 5

print("Pop element with get():", lifo_q.get())  # Output: Pop element: 5
print("Stack size after pop:", lifo_q.qsize())  # Output: Stack size after pop: 4

print("Is the stack empty with empty()?", lifo_q.empty())  # Output: Is the stack empty?

"""
PriorityQueue
Time Complexity: O(log n) for enqueue and dequeue operations.
Linear data structure that follows the priority principle.
Elements are added to the queue with a priority, and the element with the highest priority is removed
"""
# import queue
priority_q = queue.PriorityQueue()  # Create a PriorityQueue object
print("Enqueueing elements with put((priority, element)) - 3, Task 3")
priority_q.put((3, "Task 3"))
print("Enqueueing elements with put((priority, element)) - 2, Task 2")
priority_q.put((2, "Task 2"))
print("Enqueueing elements with put((priority, element)): - 1, Task 1")
priority_q.put((1, "Task 1"))

print("Print priority_q with list():", list(priority_q.queue))  # Output: Print priority_q with list(): [(1, 'Task 1'), (2, 'Task 2'), (3, 'Task 3')]

while not priority_q.empty():
   print

print("Print priority_q with list():", list(priority_q.queue))
print("Queue size with qsize():", priority_q.qsize())  # Output: Queue size: 5
print("Highest priority element with queue[0]:", priority_q.queue[0])  # Output: Highest priority element: 1