def top_down(val, wt, s):
    n = len(val)
    t = [[-1 for _ in range(s + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        t[i][0] = 0

    for j in range(s + 1):
        t[0][j] = 0

    for i in range(1, n + 1):
        for j in range(1, s + 1):
            if wt[i - 1] <= j:
                t[i][j] = max(val[i - 1] + t[i - 1][j - wt[i - 1]], t[i - 1][j])
            else:
                t[i][j] = t[i - 1][j]
    print(t)
    return t[n][s]


if __name__ == "__main__":
    val = [3, 4, 2, 7, 5]
    wt = [2, 3, 1, 8, 3]
    s = 2
    print(top_down(val, wt, s))