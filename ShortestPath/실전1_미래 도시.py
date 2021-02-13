{\rtf1\ansi\ansicpg949\cocoartf2578
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;\f1\fnil\fcharset129 AppleSDGothicNeo-Regular;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red255\green255\blue254;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;\cssrgb\c100000\c100000\c99608;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl420\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 INF = int(1e9)  # 
\f1 \'b9\'ab\'c7\'d1\'c0\'bb
\f0  
\f1 \'c0\'c7\'b9\'cc\'c7\'cf\'b4\'c2
\f0  
\f1 \'b0\'aa\'c0\'b8\'b7\'ce
\f0  10
\f1 \'be\'ef\'c0\'bb
\f0  
\f1 \'bc\'b3\'c1\'a4
\f0 \cb1 \
\
\cb3 n, m = map(int, input().split())  # 
\f1 \'b3\'eb\'b5\'e5
\f0  
\f1 \'b0\'b3\'bc\'f6
\f0  n, 
\f1 \'b0\'a3\'bc\'b1
\f0  
\f1 \'b0\'b3\'bc\'f6
\f0  m\cb1 \
\
\cb3 # 2
\f1 \'c2\'f7\'bf\'f8
\f0  
\f1 \'b8\'ae\'bd\'ba\'c6\'ae
\f0 (
\f1 \'b1\'d7\'b7\'a1\'c7\'c1
\f0  
\f1 \'c7\'a5\'c7\'f6
\f0 ) 
\f1 \'b8\'b8\'b5\'e9\'b0\'ed
\f0 , 
\f1 \'b8\'f0\'b5\'e7
\f0  
\f1 \'b0\'aa\'c0\'bb
\f0  
\f1 \'b9\'ab\'c7\'d1\'c0\'b8\'b7\'ce
\f0  
\f1 \'c3\'ca\'b1\'e2\'c8\'ad
\f0 \cb1 \
\cb3 graph = [[INF]*(n+1) for _ in range(n + 1)]\cb1 \
\
\cb3 # 
\f1 \'c0\'da\'b1\'e2
\f0  
\f1 \'c0\'da\'bd\'c5\'c0\'b8\'b7\'ce
\f0  
\f1 \'b0\'a1\'b4\'c2
\f0  
\f1 \'ba\'f1\'bf\'eb\'c0\'ba
\f0  0
\f1 \'c0\'b8\'b7\'ce
\f0  
\f1 \'c3\'ca\'b1\'e2\'c8\'ad
\f0 \cb1 \
\cb3 for a in range(1, n + 1):\cb1 \
\cb3     for b in range(1, n + 1):\cb1 \
\cb3         if a == b:\cb1 \
\cb3             graph[a][b] = 0\cb1 \
\
\cb3 for _ in range(m):\cb1 \
\cb3     a, b = map(int, input().split())\cb1 \
\cb3     graph[a][b] = 1\cb1 \
\cb3     graph[b][a] = 1\cb1 \
\
\cb3 x, k = map(int, input().split())  # 
\f1 \'b0\'c5\'c3\'c4\'b0\'a5
\f0  
\f1 \'b3\'eb\'b5\'e5
\f0  x, 
\f1 \'c3\'d6\'c1\'be
\f0  
\f1 \'b8\'f1\'c0\'fb\'c1\'f6
\f0  
\f1 \'b3\'eb\'b5\'e5
\f0  k\cb1 \
\
\cb3 # 
\f1 \'c1\'a1\'c8\'ad\'bd\'c4\'bf\'a1
\f0  
\f1 \'b5\'fb\'b6\'f3
\f0  
\f1 \'c7\'c3\'b7\'ce\'c0\'cc\'b5\'e5
\f0  
\f1 \'bf\'f6\'bc\'c8
\f0  
\f1 \'be\'cb\'b0\'ed\'b8\'ae\'c1\'f2
\f0  
\f1 \'bc\'f6\'c7\'e0
\f0 \cb1 \
\cb3 for k in range(1, n + 1):\cb1 \
\cb3     for a in range(1, n + 1):\cb1 \
\cb3         for b in range(1, n + 1):\cb1 \
\cb3             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])\cb1 \
\
\cb3 # 
\f1 \'bc\'f6\'c7\'e0\'b5\'c8
\f0  
\f1 \'b0\'e1\'b0\'fa
\f0  
\f1 \'c3\'e2\'b7\'c2
\f0 \cb1 \
\cb3 distance = graph[1][k] + graph[k][x]\cb1 \
\
\cb3 # 
\f1 \'b5\'b5\'b4\'de\'c7\'d2
\f0  
\f1 \'bc\'f6
\f0  
\f1 \'be\'f8\'b4\'c2
\f0  
\f1 \'b0\'e6\'bf\'ec
\f0 \cb1 \
\cb3 if distance >= INF:\cb1 \
\cb3     print("-1")\cb1 \
\cb3 else:\cb1 \
\cb3     print(distance)\cb1 \
\
}