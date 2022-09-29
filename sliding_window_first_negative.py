A = [12, 3, -4, 0, 5, 7, -2, 1,1]
n = len(A)
k = 3
ans = []
temp = []
i = j =0

while j < n:
    if A[j] < 0:
        temp.append(A[j])
    if j-i+1 < k:
        j += 1
    else:
        if len(temp) == 0:
            ans.append(0)
        else:
            ans.append(temp[0])
            if temp[0] == A[i]:
                temp = temp[1:]
        i += 1
        j += 1
print(ans)