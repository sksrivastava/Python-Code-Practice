def subset_sum(a, s):
    n = len(a)
    t = [[-1 for _ in range(s+1)] for _ in range(n+1)]
    for i in range(n+1):
        t[i][0] = True
    for j in range(1, s+1):
        t[0][j] = False
    for i in range(1,n+1):
        for j in range(1,s+1):
            if a[i-1] <= j:
                t[i][j] = t[i-1][j-a[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i - 1][j]
    return t[n][s]


if __name__ == "__main__":
    a = [2,3,7,8,10]
    s = 14
    print(subset_sum(a, s))