
T = int(input())

for _ in range(T):
    
    n = int(input())
    
    line = input()
    a = [int(q) for q in line.split()]
    
    seated = set()
    for passenger in a:
        if ((passenger - 1) not in seated and 
            (passenger + 1) not in seated and
            len(seated) >= 1):
            print("No")
            break
        
        seated.add(passenger)
    
    if len(seated) == n:
        print("Yes")
        
        
    
    