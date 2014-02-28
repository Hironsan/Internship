from Queue import Queue

def del_point(points, ch, idx):
    return [points[i] for i in range(len(points)) if points[i][ch] != idx]

if __name__ == "__main__":
    N = input("N = ")
    K = input("K = ")
    points = [map(int, raw_input().split(",")) for i in range(K)]
    Q = Queue()
    Q.put((0, points))
    while not Q.empty():
        cnt, points = Q.get()
        if points == []:
            print cnt
            break
        for i in range(N):
            Q.put((cnt+1, del_point(points, 0, i)))
            Q.put((cnt+1, del_point(points, 1, i)))