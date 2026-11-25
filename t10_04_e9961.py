import sys


def generate(n, k, perm, used, out):
    if len(perm) == k:
        out.append(" ".join(map(str, perm)))
        return
    for x in range(1, n + 1):
        if not used[x]:
            used[x] = True
            perm.append(x)
            generate(n, k, perm, used, out)
            perm.pop()
            used[x] = False


n, k = map(int, input().split())
out = []
generate(n, k, [], [False] * (n + 1), out)
sys.stdout.write("\n".join(out) + "\n")
