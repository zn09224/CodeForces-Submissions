T = int(input())

for _ in range(T):
    
    n = int(input())
    line = input()
    a = [int(q) for q in line.split()]
    s = input()
    
    total = sum(a)
    res = 0
    l, r = 0, n - 1
    
    while l < r:
        
        if s[l] == 'L' and s[r] == 'R':
            res += total
            total -= a[l]
            l += 1
            total -= a[r]
            r -= 1
        
        if s[l] != 'L':
            total -= a[l]
            l += 1
        
        if s[r] != 'R':
            total -= a[r]
            r -= 1
        
    print(res)     
    