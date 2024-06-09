T = int(input())
for _ in range(T):
    n = int(input())
    line = input()
    a = [int(q) for q in line.split()]
    ans = float('inf')
    for i in range(n - 1):
        ans = min(ans, max(a[i], a[i + 1]))
    print(ans - 1)
        
    