import time
k = 7
A = []
ans = []

def find_low_index(a, arr=A):
    l = len(arr) - 1
    s = 0
    res = 0
    if a > arr[l]:
        return -1
    if a < arr[0]:
        return 0
    while s<=l:
        mid = (s + l)//2
        if arr[mid] == a:
            return mid
        elif arr[mid] > a:
            res = mid
            l = mid - 1
        else:
            s = mid + 1
    return res

def find_high_index(a, arr=A):
    l = len(arr) - 1
    s = 0
    res = l
    if a > arr[l]:
        return l
    if a < arr[0]:
        return -1
    while s<=l:
        mid = (s + l)//2
        if arr[mid] == a:
            return mid
        elif arr[mid] > a:
            l = mid - 1
        else:
            s = mid + 1
            res = mid
    return res

def solve(p):
    n = len(A)
    while n < 2:
        return
    low = p-k
    high = p+k
    index_low = find_low_index(low)
    index_high = find_high_index(high)
    if index_high == -1 or index_low == -1:
        dist = 0
    else:
        dist = index_high - index_low + 1
    # print("low",index_low)
    # print("high", index_high)
    # print("distance", dist)
    if dist > 1:
        A1 = A[index_low : index_high+1]
        m = len(A1)
        for i in range(m-1):
            for j in range(i+1, m):
                if i != j and abs(A[i]-A[j]) <= k:
                    ans1 = [p, A1[i], A1[j]]
                    ans.append(ans1)


def incoming():
    p = input("Enter number : ")
    if p.isalpha():
        print("exist")
    else:
        p = int(p)
        print("Triplets with equi-diastance of ", k , " are : ")
        solve(p)
        print(ans)
        A.append(p)
        A.sort()
        print(A)
        incoming()

begin = time.time()
incoming()
time.sleep(1)
end = time.time()
print(f"Total runtime of the program is {end - begin}")
