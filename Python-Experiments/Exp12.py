# Experiment 12: Stack and Queue Operations

from collections import deque

# Stack follows LIFO
stack = []

stack.append(10)
stack.append(20)
stack.append(30)
print("Stack:", stack)

print("Popped:", stack.pop())
print("Stack after pop:", stack)

# Queue follows FIFO
queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)
print("Queue:", list(queue))

print("Dequeued:", queue.popleft())
print("Queue after dequeue:", list(queue))

# Double-ended queue
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print("Deque:", dq)

dq.popleft()
dq.pop()
print("Updated deque:", dq)

# Checking whether stack is empty
print("Stack empty:", len(stack) == 0)
