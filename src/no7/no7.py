def get_max_line(line):
    maxval = 0
    maxidx = -1
    for i, v in enumerate(line):
        if v > maxval:
            maxval = v
            maxidx = i
    return maxval, maxidx


def solve(N, K, x_line, y_line):
    cnt = 0
    delete_num = 0
    while delete_num < K:
        x_star_num, x_idx = get_max_line(x_line)
        y_star_num, y_idx = get_max_line(y_line)
        if x_star_num > y_star_num:
            delete_num += x_star_num
            x_line[x_idx] = 0
        else:
            delete_num += y_star_num
            y_line[y_idx] = 0
        cnt += 1
    return cnt

if __name__ == "__main__":
    N = input("N = ")
    K = input("K = ")
    x_line = [0] * N
    y_line = [0] * N
    points = [map(int, raw_input().split(",")) for i in range(K)]
    for x, y in points:
        x_line[x] += 1
        y_line[y] += 1
    print solve(N, K, x_line, y_line)
