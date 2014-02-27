from no2_a import Stack

candidate = set()
candidate = []
gomi = set()

def dfs(num, ans):
    if num == 2*n:
        if is_match(ans):
            candidate.append(ans)
        return
    if ans in gomi:
        return
    else:
        gomi.add(ans)
    if not is_match1(ans):
        return
    for i in range(2*n):
        if not used[i]:
            used[i] = True
            dfs(num+1, ans+string[i])
            used[i] = False

def is_match(string):
    stack = Stack()
    for ch in string:
        if ch == "(":
            stack.push("(")
        elif ch == ")":
            if stack.empty():
                return False
            stack.pop()
    return stack.empty()


def is_match1(string):
    stack = Stack()
    for ch in string:
        if ch == "(":
            stack.push("(")
        elif ch == ")":
            if stack.empty():
                return False
            stack.pop()
    return True

n = input()
string = "(" * n + ")" * n
used = [False] * n * 2
dfs(0, "")
for cand in candidate:
    print cand+",",
print
