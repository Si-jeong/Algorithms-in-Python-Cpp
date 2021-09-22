import sys
input = sys.stdin.readline


n, x = map(int, input().split())

c = list(map(int, input().split()))
c.sort(reverse=True)

checked = [False]*n

count = 0

for i in range(n):
    if checked[i]:
        continue
    checked[i] = True
    if c[i] == x:
        count += 1
        continue
    if c[i] >= x/4:
        if i+1 > n-1:
            break
        if c[i] + c[i+1] >= x/2:
            checked[i] = True
            checked[i+1] = True
            count += 1
        else:
            break
    break

count += checked.count(False)//4
print(count)