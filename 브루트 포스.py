# 블랙잭
N,M=map(int,input().split())
card=list(map(int,input().split()))

sum_list=[]
for idx,x in enumerate(card):
    for idy,y in enumerate(card):
        if idy != idx:
            for idz,z in enumerate(card):
                if idz != idx and idz != idy:
                    sum = x + y + z
                    if sum <= M:
                        sum_list.append(sum)

print(max(sum_list))

# 블랙잭 ver.2
N, M = map(int, input().split())
card = list(map(int, input().split()))

sum = 0
for i in range(N - 2):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            card_sum=card[i] + card[j] + card[k]
            if card_sum <= M and card_sum > sum:
                sum = card[i] + card[j] + card[k]

print(sum)


# 블랙잭 ver.3
from itertools import combinations

n, m = map(int, input().split())
n_list = list(map(int, input().split()))
combinations_n_list = list(combinations(n_list,3))
answer = 0

for i in combinations_n_list:
    if answer < sum(i) and sum(i) <= m:
        answer = sum(i)

print(answer)




# 분해합
n = int(input())

m=1
while True:
    m_list=[int(i) for i in str(m)]
    m_sum = m + sum(m_list)
    if m_sum == n:
        break
    m += 1
    if m > n:
        m = 0
        break

print(m)


# 덩치
N = int(input())
n_list=[]
for _ in range(N):
    n_list.append(input().split())

for i in range(N):
    rank = 1
    for j in range(N):
        if n_list[i][0] < n_list[j][0] and n_list[i][1] < n_list[j][1]:
            rank += 1
    print(rank,end=' ')


# 체스판 다시 칠하기
M,N = map(int,input().split())

c_list=[]
for _ in range(M):
    c_list.append(input())

rep_list=[]
for i in range(M-7):
    for j in range(N-7):
        w=0
        b=0
        for k in range(i,i+8):
            for p in range(j,j+8):
                if (k+p) % 2 == 0:
                    if c_list[k][p] != 'W':
                        w += 1
                    if c_list[k][p] != 'B':
                        b += 1
                else:
                    if c_list[k][p] != 'B':
                        w += 1
                    if c_list[k][p] != 'W':
                        b += 1
        rep_list.append(w)
        rep_list.append(b)

print(min(rep_list))



# 영화감독 숌
N=int(input())

cnt=0
x=666
while True:
    if '666' in str(x):
        cnt+=1
    if cnt == N:
        print(x)
        break

    x += 1

