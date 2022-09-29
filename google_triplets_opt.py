import time
k = 7
A = []
ans = []

def find_low_index(a, arr):
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

def find_high_index(a, arr):
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


def find_range(low, high, arr=A):
    index_low = find_low_index(low, arr)
    index_high = find_high_index(high, arr)
    if index_high == -1 or index_low == -1:
        return []
    else:
        return arr[index_low: index_high + 1]


def solve(p):
    n = len(A)
    if n < 2:
        return
    low = p-k
    high = p+k
    rng = find_range(low, high)
    print("large ", rng)
    while len(rng) > 1:
        ele = rng[-1]
        rng = rng[:-1]
        l1 = ele - k
        h1 = ele + k
        rng1 = find_range(l1, h1, rng)
        print("smaller ", rng1)
        for el in rng1:
            ans.append([p, ele, el])


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
end = time.time()
print(f"Total runtime of the program is {end - begin}")