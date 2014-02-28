import sys


def is_sorted(lst1, lst2):
    return lst1 == lst2


def solve(lst):
    min_siz = sys.maxint
    length = len(lst)
    ansm, ansn = 0, length
    sorted_list = sorted(lst)
    for m in range(length-1):
        for n in range(m+1, length):
            part_sorted_lst = lst[:m] + sorted(lst[m:n]) + lst[n:]
            if is_sorted(sorted_list, part_sorted_lst):
                if min_siz > n - m - 1:
                    min_siz = n - m - 1
                    ansm, ansn = m, n - 1
    return ansm, ansn

if __name__ == "__main__":
    lst = [1,2,4,7,10,11,7,12,7,8,16,18,19]
    lst = map(int, raw_input().split(","))
    m, n = solve(lst)
    print "m = %d" % m
    print "n = %d" % n