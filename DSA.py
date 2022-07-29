#from collections import deque

#q=deque()
q=[]

q.append(20)
q.append(70)
q.sort()
q.append(50)
q.sort()
q.append(10)
q.sort()

print("initial queue")
print(q)

print("\n Element dequed from the queue")
print(q.pop())
print(q.pop())
print(q.pop())

print("\n Queue after removing elements")
print(q)