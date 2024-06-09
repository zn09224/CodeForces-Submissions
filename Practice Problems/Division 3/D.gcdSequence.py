def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_increasing(a, n):
    for i in range(1, n - 1):
        # print((gcd(a[i - 1], a[i]), gcd(a[i], a[i + 1])))
        if gcd(a[i - 1], a[i]) > gcd(a[i], a[i + 1]):
            return (0, i)
    return 1

T = int(input())
for _ in range(T):
    n = int(input())
    line = input()
    a = [int(q) for q in line.split()]
    
    if is_increasing(a, n) == 1:
        print("YES")
        # print(1)
        continue
    
    res, ind = is_increasing(a, n)
    if ind == n - 2:
        print("YES")
        # print(2)
        continue
    
    if (is_increasing(a[0:ind - 1] + a[ind:n], n - 1) == 1 or
        is_increasing(a[0:ind] + a[ind + 1:n], n - 1) == 1 or
        is_increasing(a[0:ind + 1] + a[ind + 2:n], n - 1) == 1):
        print("YES")
        # print(3)
        continue
    
    print("NO")
    
    
    