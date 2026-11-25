import sys

sys.setrecursionlimit(10000)


def solve(n, tracks):
    m = len(tracks)
    suffix = [0] * (m + 1)
    for i in range(m - 1, -1, -1):
        suffix[i] = suffix[i + 1] + tracks[i]
    visited = [[False] * (n + 1) for _ in range(m + 1)]
    best = [-1, []]
    chosen = []

    def search(i, total):
        if total > best[0]:
            best[0] = total
            best[1] = chosen[:]
        if i == m or best[0] == n or visited[i][total]:
            return
        visited[i][total] = True
        if total + suffix[i] <= best[0]:
            return
        if total + tracks[i] <= n:
            chosen.append(tracks[i])
            search(i + 1, total + tracks[i])
            chosen.pop()
        search(i + 1, total)

    search(0, 0)
    return best


def main():
    out = []
    for line in sys.stdin:
        nums = list(map(int, line.split()))
        if not nums:
            continue
        n, s = nums[0], nums[1]
        tracks = nums[2:2 + s]
        total, chosen = solve(n, tracks)
        out.append("sum:%d" % total)
    sys.stdout.write("\n".join(out) + "\n")


main()
