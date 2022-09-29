lim = int(input())
sms = input()
# lim = 14
# sms = "my na,m is. sac.? in..dra, wat ,was urs?"
s_list = sms.split()
line_len = 0
ans = []
p = ""
word = 0
br = False

for s in s_list:
    if len(s) > (lim - 5):
        br = True
        break

    l1 = len(s) + word
    if (line_len + l1) > (lim - 5):
        ans.append(p)
        p = ""
        line_len = 0
        word = 0
        l1 = len(s)

    if (line_len + l1) <= (lim-5):
        p = p + " " + s if word else s
        line_len += l1
        word += 1
if br:
    print([])
else:
    ans.append(p)
    tot = len(ans)
    cur = 1
    for a in ans:
        ans[cur-1] = a + f"<{cur}/{tot}>"
        cur += 1
    print(ans)