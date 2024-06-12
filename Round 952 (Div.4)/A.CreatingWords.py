T = int(input())
for _ in range(T):
    line = input()
    a, b = line.split()
    print(b[0] + a[1:], a[0] + b[1:])
