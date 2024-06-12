T = int(input())
for _ in range(T):
    n = int(input())
    line = input()
    a = [int(q) for q in line.split()]
    
    maximum = a[0]
    total = 0
    res = 0
     
    for i in range(n):
        if a[i] >= maximum:
            maximum = a[i]
        
        total += a[i]
        if total - maximum == maximum:
            res += 1
        
    print(res)
            
        
         
