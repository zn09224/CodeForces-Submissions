T = int(input())
for _ in range(T):
    line = input()
    x, y = [int(q) for q in line.split()]
    print(min(x, y), max(x, y))
