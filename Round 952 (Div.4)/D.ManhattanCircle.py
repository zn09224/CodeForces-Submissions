T = int(input())
for _ in range(T):
    line = input()
    n, m = [int(q) for q in line.split()]
    
    matrix = []
    for i in range(n):
        line = input()
        matrix.append(list(line))
    
    flag = True
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '#':
                col = j
                r = i
                first_row = i
                flag = False
                break
        if flag == False:
            break
    
    row = None   
    rows = 0
    for i in range(r, n):
        if matrix[i][col] != '#':
            row = i - 1
            break
    if row == None:
        row = n - 1

    
    row = (row +  first_row) // 2
    
    print(row + 1, col + 1)
    
    
    
            
                    
                
    
    
        
        