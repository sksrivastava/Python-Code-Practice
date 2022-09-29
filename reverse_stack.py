def insert(s, last):
    if len(s) == 0:
        s.append(last)
        return
    top = s.pop()
    insert(s, last)
    s.append(top)
    return


def reverse(s):
    if len(s) <= 1:
        return
    temp = s.pop()
    reverse(s)
    insert(s, temp)
    return


if __name__=="__main__":
    s = [1, 2, 3]
    print(s)
    reverse(s)
    print("reversed :", s)