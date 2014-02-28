from Queue import Queue

# k: depth, l, r: left(right) kakko num
def bfs(n):
    x = 2 * n
    q = Queue()
    q.put((0, 0, 0, ""))
    while not q.empty():
        k, l, r, kakko = q.get()
        if k == x:
            print kakko
            continue
        if l < r:
            continue
        if l < n:
            q.put((k+1, l+1, r, kakko+"("))
        if r < n:
            q.put((k+1, l, r+1, kakko+")"))

n = input()
bfs(n)