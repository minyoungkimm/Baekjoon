# 피보나치 함수
T = int(input())

for _ in range(T):
    n = int(input())
    zero = [1,0,1]
    one=[0,1,1]
    if n >= 3:
        for i in range(3, n+1):
            zero.append(zero[i-2] + zero[i-1])
            one.append(one[i-2] + one[i-1])
    print(zero[n],one[n])



# 신나는 함수실행
memo = [[[0]*21 for _ in range(21)] for _ in range(21)]

def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20,20,20)

    # 값이 이미 존재한다면 그 값을 리턴
    if memo[a][b][c]:
        return memo[a][b][c]

    if a < b < c:
        memo[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
        return memo[a][b][c]

    memo[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
    return memo[a][b][c]

while True:
    a,b,c = map(int,input().split())

    if a == -1 and b == -1 and c == -1:
        break

    print("w(%d, %d, %d) = %d"%(a,b,c,w(a,b,c)))





# 01타일
import sys
N = int(sys.stdin.readline())

first = 1
second = 2
tmp = 0
for _ in range(N-1):
    tmp=first
    first=second
    second=(tmp+first)%15746
print(first)




# 파도반 수열
T = int(input())

for _ in range(T):
    n = int(input())
    seq=[1,1,1,2,2]

    if n > 5:
        for i in range(5,n):
            seq.append(seq[i-1] + seq[i-5])

    print(seq[n-1])





# RGB거리
N = int(input())  # 집의 수
cost=[]
for _ in range(N):
    cost.append(list(map(int,input().split())))

for i in range(1,len(cost)):
    cost[i][0] = min(cost[i-1][1], cost[i-1][2]) + cost[i][0]
    cost[i][1] = min(cost[i-1][0], cost[i-1][2]) + cost[i][1]
    cost[i][2] = min(cost[i-1][0], cost[i-1][1]) + cost[i][2]

print(min(cost[N-1]))



# 정수 삼각형 (1932번)
n = int(input())
num=[]

for _ in range(n):
    num.append(list(map(int,input().split())))

for i in range(n-1):
    for j in range(len(num[i+1])):
        if j==0:
            num[i+1][j] = num[i][j] + num[i+1][j]
        elif j==len(num[i+1])-1:
            num[i+1][-1] = num[i][-1] + num[i+1][-1]
        else:
            num[i+1][j] = max(num[i][j-1] + num[i+1][j], num[i][j] + num[i+1][j])

print(max(num[-1]))


# 계단 오르기 (2579번)
n=int(input())
stair=[0]

for _ in range(n):
    stair.append(int(input()))

if n==1:
    print(stair[1])
else:
    dp=[0]*(n+1)
    dp[1]=stair[1]
    dp[2]=stair[1]+stair[2]

    for i in range(3,n+1):
        dp[i]=max(dp[i-3]+stair[i-1]+stair[i],dp[i-2]+stair[i])

    print(dp[n])



# 계단 오르기 ver.2 (2579번)
n=int(input())
max_score=[0 for _ in range(n)]

steps=[]
for i in range(n):
    steps.append(int(input()))

def score(n):
    max_score[0] = steps[0]
    if n==1:
        return

    max_score[1]=steps[1] + steps[0]
    if n==2:
        return

    max_score[2] = max(steps[0]+steps[2], steps[1]+steps[2])
    if n==3:
        return

    for i in range(3,n):
        max_score[i] = steps[i] + max(steps[i-1] + max_score[i-3], max_score[i-2])

score(n)
print(max_score[n-1])


# 1로 만들기 (1463번)
n = int(input())

dp = [0 for _ in range(n+2)]
dp[2] = 1


for i in range(2, len(dp)):

    dp[i] = dp[i - 1] + 1

    if i % 3 == 0:
        if dp[i] > dp[int(i / 3)] + 1:
            dp[i] = dp[int(i / 3)] + 1
    if i % 2 == 0:
        if dp[i] > dp[int(i / 2)] + 1:
            dp[i] = dp[int(i / 2)] + 1

print(dp[n])



# 쉬운 계단 수 (10844번)
N = int(input())
dp=[1 for _ in range(10)]
dp[0]=0

for _ in range(1,N):
    dp_n=[0 for _ in range(10)]
    for j in range(len(dp)):
        if j==0:
            dp_n[j]=dp[1]
        elif j==9:
            dp_n[j]=dp[8]
        elif j>0 and j<9:
            dp_n[j]=dp[j-1]+dp[j+1]
    dp=dp_n

print(sum(dp)%1000000000)


# 쉬운 계단 수 ver.2
n = int(input())
dp = [[0 for i in range(10)] for j in range(101)]
for i in range(1, 10):
    dp[1][i] = 1
for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
print(sum(dp[n]) % 1000000000)



# 포도주 시식 (2156번)
n=int(input())
quan=[0]
for i in range(n):
    quan.append(int(input()))

dp=[0 for _ in range(n+1)]
dp[1]=quan[1]

for i in range(2,n+1):
    if i==2:
        dp[i]=quan[1]+quan[2]
    else:
        dp[i]=max(dp[i-1],dp[i-3]+quan[i-1]+quan[i],dp[i-2]+quan[i])

print(dp[-1])


# 가장 긴 증가하는 부분 수열 (11053번)
n= int(input())
A=list(map(int,input().split()))

dp=[0] * n

for i in range(n):
    for j in range(i):
        if A[i] > A[j] and dp[i] < dp[j]:
            dp[i]=dp[j]
    dp[i]+=1

print(max(dp))




# 가장 긴 바이토닉 부분 수열 (11054번)
n = int(input())
num=list(map(int,input().split()))
incre=[1] * n
decre=[1] * n
result=[]

for i in range(n):
    for j in range(i):
        if num[i] > num[j] and incre[i] < incre[j] + 1:
            incre[i] = incre[j] + 1

for i in range(n-1,-1,-1):
    for j in range(i+1,n):
        if num[i] > num[j] and decre[i] < decre[j] + 1:
            decre[i] = decre[j] + 1

for i in range(n):
    result.append(incre[i] + decre[i]-1)

print(max(result))



