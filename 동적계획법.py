# 피보나치 함수
# T = int(input())
#
# for _ in range(T):
#     n = int(input())
#     zero = [1,0,1]
#     one=[0,1,1]
#     if n >= 3:
#         for i in range(3, n+1):
#             zero.append(zero[i-2] + zero[i-1])
#             one.append(one[i-2] + one[i-1])
#     print(zero[n],one[n])

#

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

































