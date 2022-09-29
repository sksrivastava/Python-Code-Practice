def lcs(x, y, n, m):
    if n==0 or m==0:
        return 0
    # global t

    if t[n][m] != -1:
        return t[n][m]
    if x[n-1] == y[m-1]:
        t[n][m] = 1 + lcs(x, y, n-1, m-1)
        return t[n][m]
    else:
        t[n][m] = max(lcs(x, y, n, m-1), lcs(x, y, n-1, m))
        return t[n][m]


if __name__ == "__main__":
    x = "abcdg"
    y = "abedfhr"
    n = len(x)
    m = len(y)
    t = [[-1 for _ in range(m+1)] for _ in range(n+1)]
    print(lcs(x, y, n, m))

