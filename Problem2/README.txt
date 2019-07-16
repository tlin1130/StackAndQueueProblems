Problem: Implementing a Queue with Two Stacks

Problem Definition:
Given a stack implementation with O(1) push(item), pop(), peek() operations, implement a queue class with two stacks.

Solution:
In Queue.py, Queue class is implemented with Stack class from StackModule.py. In Queue class, enqueue(item) is O(1) time and dequeue() has an amortized cost of O(1) for m Queue class operations.
For m Queue class operations, the space complexity of the queue data structure is O(m).