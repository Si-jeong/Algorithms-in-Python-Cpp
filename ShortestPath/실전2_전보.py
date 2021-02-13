{\rtf1\ansi\ansicpg949\cocoartf2578
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red255\green255\blue254;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;\cssrgb\c100000\c100000\c99608;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl420\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import heapq\cb1 \
\cb3 import sys\cb1 \
\
\cb3 input = sys.stdin.readline\cb1 \
\cb3 INF = int(1e9)\cb1 \
\
\cb3 n, m, start = map(int, input().split())\cb1 \
\
\cb3 graph = [[] for _ in range(n+1)]\cb1 \
\
\cb3 distance = [INF]*(n+1)\cb1 \
\
\cb3 for _ in range(m):\cb1 \
\cb3   x, y, z = map(int, input().split())\cb1 \
\cb3   graph[x].append((y, z))\cb1 \
\
\cb3 def dijkstra(start):\cb1 \
\cb3   q = []\cb1 \
\cb3   heapq.heappush(q, (0, start))\cb1 \
\cb3   distance[start] = 0\cb1 \
\cb3   while q:\cb1 \
\cb3     dist, now = heapq.heappop(q)\cb1 \
\cb3     if distance[now] < dist:\cb1 \
\cb3       continue\cb1 \
\cb3     for i in graph[now]:\cb1 \
\cb3       cost = dist + i[1]\cb1 \
\cb3       if cost < distance[i[0]]:\cb1 \
\cb3         distance[i[0]] = cost\cb1 \
\cb3         heapq.heappush(q, (cost, i[0]))\cb1 \
\
\cb3 dijkstra(start)\cb1 \
\
\cb3 count = 0\cb1 \
\cb3 max_distance=0\cb1 \
\cb3 for d in distance:\cb1 \
\cb3   if d != INF:\cb1 \
\cb3     count += 1\cb1 \
\cb3     max_distance = max(max_distance, d)\cb1 \
\
\cb3 print(count-1, max_distance)\cb1 \
}