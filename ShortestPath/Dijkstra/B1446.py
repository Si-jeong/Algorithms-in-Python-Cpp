import sys
input = sys.stdin.readline

n, d = map(int, input().split())

shortcut = [[] for _ in range(10001)]

for i in range(n):
    s, e, w = map(int, input().split())
    shortcut[s].append([w, e])

distance = [i for i in range(d+1)]

for i in range(d+1):
    if i != 0:
        distance[i] = min(distance[i], distance[i-1]+1)
    for w, e in shortcut[i]:
        if e <= d and distance[e] > w + distance[i]:
            distance[e] = w + distance[i]

print(distance[d])
    