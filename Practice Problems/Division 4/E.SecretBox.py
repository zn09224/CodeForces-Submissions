T = int(input())

for _ in range(T):
    line = input()
    x, y, z, k = [int(q) for q in line.split()]

    res = 0

    for a in range(1, x + 1):
        for b in range(1, y + 1):
            if (k % (a*b)) != 0:
                continue
            c = int(k / (a*b))
            if c > z:
                continue
            res = max(res, (x - a + 1)*(y - b + 1)*(z - c + 1))
    print(res)
                
               
            
    
    
    
    