from Queue import Queue
from copy import deepcopy

def del_point(points, ch, idx):
    return [points[i] for i in range(len(points)) if points[i][ch] != idx]

N = input("N = ")
K = input("K = ")
points = [map(int, raw_input().split(",")) for i in range(K)]
Q = Queue()
Q.put((0, points, set()))
while not Q.empty():
    cnt, points, used = Q.get()
    if points == []:
        print cnt
        break
    for i in range(N):
        if i not in used:
            new_used = deepcopy(used)
            new_used.add(i)
            Q.put((cnt+1, del_point(points, 0, i), new_used))
            Q.put((cnt+1, del_point(points, 1, i), new_used))