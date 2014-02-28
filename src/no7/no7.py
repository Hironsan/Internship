def get_max_xline(points):
    maxval = 0
    maxidx = -1
    for i, line in enumerate(points):
        v = sum(line)
        if v > maxval:
            maxval = v
            maxidx = i
    return maxval, maxidx


def get_max_yline(points):
    maxval = 0
    maxidx = -1
    for i in range(len(points)):
        v = 0
        for j in range(len(points)):
            v += points[j][i]
        if v > maxval:
            maxval = v
            maxidx = i
    return maxval, maxidx


def del_xline(idx, points):
    for i in range(len(points)):
        points[idx][i] = 0


def del_yline(idx, points):
    for i in range(len(points)):
        points[i][idx] = 0

def solve(N, K, points):
    cnt = 0
    delete_num = 0
    while delete_num < K:
        x_star_num, x_idx = get_max_xline(points)
        y_star_num, y_idx = get_max_yline(points)
        if x_star_num > y_star_num:
            delete_num += x_star_num
            del_xline(x_idx, points)
        else:
            delete_num += y_star_num
            del_yline(y_idx, points)
        cnt += 1
    return cnt

if __name__ == "__main__":
    N = input("N = ")
    K = input("K = ")
    points = [[0] * N for i in range(N)]
    for i in range(K):
        R, C = map(int, raw_input().split(","))
        points[R][C] = 1
    print solve(N, K, points)
