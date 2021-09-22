import time

import sys
input = sys.stdin.readline

t = int(input())

for u in range(t):
    
    print("Case #"+str(u)+": ", end ="")
    now = list(input())
    start = time.time()
    string = []
    for i in range(len(now)):
        string.append((now[i], now.count(now[i])))
    string.sort(key = lambda x: x[1], reverse=True)
    # 원소 개수 많은 것 순으로 정렬

    new = ['' for _ in range(len(now))]
    isFilled = True
    for i in range(len(now)):
        if not isFilled:
            new = "IMPOSSIBLE"
            break
        s = string[i][0]
        isFilled = False
        for j in range(len(now)):
            if now[j] == s:
                continue
            if new[j] != '':
                continue
            else:
                new[j] = s
                # print(s)
                isFilled = True
                break
    if new == "IMPOSSIBLE":
        print(new)
    else:
        for s in new:
            print(s, end = "")
        print("\0")
    end = time.time()
    print(f"{end-start}:.5f sec")


