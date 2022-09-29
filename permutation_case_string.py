def solve(ip, op):
    if len(ip) == 0:
        A.append(op)
        print(op)
        return
    t = ip[0]
    ip = ip[1:]
    if t.isdigit():
        op1 = op + t
        solve(ip, op1)
    else:
        t = t.lower()
        T = t.upper()
        op1 = op + t
        op2 = op + T
        solve(ip, op1)
        solve(ip, op2)

A = []
ip = "3a"
op = ""
solve(ip, op)
print(A)