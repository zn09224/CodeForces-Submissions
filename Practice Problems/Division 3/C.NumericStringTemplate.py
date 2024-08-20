T = int(input())

for _ in range(T):
    
    n = int(input())
    line = input()
    a = [int(q) for q in line.split()]
    
    m = int(input())
    for k in range(m):
        s = input()
        
        if len(s) != n:
            print('No')
            continue
        
        res = "Yes"
        
        hashmapNums = {}
        hashmapString = {}
        for i in range(n):
            if a[i] in hashmapNums and hashmapNums[a[i]] != s[i]:
                res = "No"
                break
            
            hashmapNums[a[i]] = s[i]
            
            if s[i] in hashmapString and hashmapString[s[i]] != a[i]:
                res = 'NO'
                break
            
            hashmapString[s[i]] = a[i]
                    

        print(res)
        
            
    
    