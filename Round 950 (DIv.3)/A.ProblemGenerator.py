T = int(input())
for _ in range(T):
    numbers = input()
    n, m = [int(q) for q in numbers.split()]
    problems = input()
    difficulties = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    my_dic = {}
    for p in difficulties:
        my_dic[p] = 0
    for p in problems:
        my_dic[p] += 1
    ans = 0
    for p in my_dic.keys():
        ans += (max(m - my_dic[p], 0))
    print(ans)
        
    