from Queue import Queue

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
        if (0, i) not in used:
            Q.put((cnt+1, del_point(points, 0, i), used | set((0, i))))
        if (1, i) not in used:
            Q.put((cnt+1, del_point(points, 1, i), used | set((1, i))))