from queue import Queue

q = Queue()
q.put(4)
rt = [0,0,0,0]
print(not q.empty())
t = q.get()
v = q.get()
print(t,v)