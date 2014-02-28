# k: depth, l, r: left(right) kakko num
def dfs(k, l, r, kakko):
    if l < r:
        return
    if k == x:
        print kakko
        return
    if l < n:
        dfs(k+1, l+1, r, kakko+"(")
    if r < n:
        dfs(k+1, l, r+1, kakko+")")

n = input()
x = 2 * n
dfs(0, 0, 0, "")