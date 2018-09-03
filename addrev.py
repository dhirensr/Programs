n=int(input())

for i in range(n):
    x,y = input().split()
    rev_x = x[::-1]
    rev_y = y[::-1]
    add= int(rev_y) + int(rev_x)
    final_res = int(str(add)[::-1])
    print(final_res)
