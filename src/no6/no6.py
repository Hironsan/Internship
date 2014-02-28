import sys
import math
from itertools import combinations

def get_dist(plist1, plist2):
    x1, y1, r1 = plist1
    x2, y2, r2 = plist2
    return math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))


def get_rec(pset):
    length = 0
    plist = list(pset)
    n = len(plist)
    for i in range(n-1):
        for j in range(i+1, n):
            r1 = plist[i][-1]
            r2 = plist[j][-1]
            length = max(length, get_dist(plist[i], plist[j]) + r1 + r2)
    return length if length != 0 else sys.maxint


if __name__ == "__main__":
    N = input("N = ")
    points = [map(int, raw_input().split(",")) for i in range(N)]
    points = map(tuple, points)
    r = sys.maxint
    for i in range(1, N):
        set1 = set()
        set2 = set()
        for items in combinations(points, i):
            for item in items:
                set1.add(item)
            for point in points:
                if point not in set1:
                    set2.add(point)
            r = min(r, get_rec(set1), get_rec(set2))
    print r/2.0
