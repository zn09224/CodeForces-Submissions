from itertools import chain

def transpose(M):
    n = len(M[0])
    L = list(chain(*M))
    return [L[i::n] for i in range(n)]

def sort_check(a, b):
    sorted_a = sorted(sorted(i) for i in a)
    sorted_b = sorted(sorted(i) for i in b)
    if sorted_a != sorted_b:
        return False
    return True

T = int(input())
for _ in range(T):
    line = input()
    n, m = [int(q) for q in line.split()]
    
    a = []
    for i in range(n):
        line = input()
        col = [int(q) for q in line.split()]
        a.append(col)
    b = []
    for i in range(n):
        line = input()
        col = [int(q) for q in line.split()]
        b.append(col)
    
    if n == 1 or m == 1:
        print("YES")
        continue
    
    if not sort_check(a, b):
        print("NO")
        continue
    
    a = transpose(a)
    b = transpose(b)
    
    if not sort_check(a, b):
        print("NO")
        continue
    
    print("YES")
    
                
            
            
    
                        
                        

    
                        
    
    
    