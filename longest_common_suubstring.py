def longest_common_substring(x, y):
    m = len(x)
    n = len(y)
    max_len = 0
    row_ptr, col_ptr = 0, 0# pointing to end index of common substring
    t = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if i==0 or j==0:
                t[i][j] = 0
            elif x[i-1] == y[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
                if t[i][j]>max_len:
                    max_len = t[i][j]
                    row_ptr = i
                    col_ptr = j
            else:
                t[i][j] = 0
    if max_len == 0:
        print("No common substring")
        return 0
    else:
        s1 = [' ']*max_len
        max_len1= max_len
        while t[row_ptr][col_ptr] != 0:
            max_len1 -= 1
            s1[max_len1] = x[row_ptr-1]
            row_ptr -= 1
            col_ptr -= 1
        print("".join(s1))
        return max_len
if __name__ == "__main__":
    x = "dabecdg"
    y = "abcdg"

    print(longest_common_substring(x, y))