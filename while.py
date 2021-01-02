# 1번
while True:
    A,B = map(int,input().split())
    if A == 0 and B == 0:
        break
    print(A+B)

# 2번
while True:
    try:
        A,B = map(int, input().split())
        print(A+B)
    except:
        break

# 3번
N = int(input())
N_fix=N
cnt=0
while True:
    ten=N//10
    one=N%10
    N=(one*10)+((ten+one)%10)
    cnt+=1
    if N == N_fix:
        break

print(cnt)