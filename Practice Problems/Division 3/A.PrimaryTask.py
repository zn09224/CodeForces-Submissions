T = int(input())
for _ in range(T):
    n = input()
    if len(n) < 3: 
        print("No")
    elif len(n) == 3 and n[2] == '1':
        print('No')
    elif n[0] == '1' and n[1] == '0' and n[2] != '0':
        print('Yes')
    else:
        print('No')
    