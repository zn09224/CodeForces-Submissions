T = int(input())
for _ in range(T):
    line_1 = input()
    n, f, k = [int(q) for q in line_1.split()]
    line_2 = input()
    a = [int(q) for q in line_2.split()]
    fav_cube = a[f - 1]
    a.sort()
    a = a[::-1]
    if k == n or a[k] < fav_cube:
        print("YES")
    elif a[k] == fav_cube and a[k] == a[k - 1]:
        print("MAYBE")
    else:
        print("NO")
    
