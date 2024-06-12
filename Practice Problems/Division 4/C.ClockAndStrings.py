T = int(input())
for _ in range(T):
    line = input()
    a, b, c, d = [int(q) for q in line.split()]
    
    a, b = min(a, b), max(a, b)
    c, d = min(c, d), max(c, d)
    
    l = [a, b, c, d]
    l.sort()
    
    if (l[1] == a and l[2] == b) or (l[1] == c and l[2] == d):
        print("NO")
    elif (l[0] == a and l[1] == b) or (l[0] == c and l[1] == d):
        print("NO") 
    else:
        print("YES")
