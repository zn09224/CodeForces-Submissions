T = int(input())
for _ in range(T):
    s = input()
    s.split()
    
    a = ''.join(sorted(s))
    
    if a != s:
        print("YES")
        print(a)
        continue
    
    a = a[::-1]
    if a != s:
        print("YES")
        print(a)
        continue
    
    print("NO")
    
    
        