from collections import deque

reversed_queue = deque()
for element in queue:
	reversed_queue.appendleft(element)

