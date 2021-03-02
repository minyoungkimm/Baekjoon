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



# 정수 삼각형
n = int(input())
num=[]
for _ in range(n):
    num.append(list(map(int,input().split())))

print(num)




















