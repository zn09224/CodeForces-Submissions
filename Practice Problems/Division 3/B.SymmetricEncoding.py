T = int(input())
for _ in range(T):
    n = int(input())
    s = input().split()
    r = set()
    for c in s[0]:
        if c not in r:
            r.add(c)
    r = list(r)
    r.sort()
    my_dic = {}
    l = len(r)
    m = len(r) // 2
    remaining = l - 1 - m
    for i in range(l):
        my_dic[r[i]] = m + remaining - i
    ans = ""
    for e in s[0]:
        ans += r[my_dic[e]]
    print(ans)
        
    
        