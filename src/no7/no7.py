from Queue import Queue

def get_max_star_num(idx, points, N):
    line = [0] * N
    for i in range(len(points)):
        line[points[i][idx]] += 1
    return line

def gen_new_points(points, del_item):
    new_list = []
    ch, point = delete_item
    for x, y in points:
        if ch == "x":
            if x != point:
                new_list.append((x, y))
        else:
            if y != point:
                new_list.append((x,y))
    return new_list


if __name__ == "__main__":
    N = input("N = ")
    K = input("K = ")
    points = []
    for i in range(K):
        R, C = map(int, raw_input().split(","))
        points.append((R, C))
    Q = Queue()
    # delete_star_num, bi-mukaisuu,points, next_delete_line
    Q.put((0, 0, points))
    while not Q.empty():
        k, cnt, points = Q.get()
        if k == K:
            print cnt
            break
        x_line = get_max_star_num(0, points, N)
        y_line = get_max_star_num(1, points, N)
        max_star_num = max(max(x_line), max(y_line))
        delete_items = []
        for i, v in enumerate(x_line):
            if v == max_star_num:
                delete_items.append(("x", i))
        for i, v in enumerate(y_line):
            if v == max_star_num:
                delete_items.append(("y", i))
        for delete_item in delete_items:
            Q.put((k+max_star_num, cnt+1, gen_new_points(points, delete_item)))
