# 1번
N = int(input())
for i in range(1,10):
    print(N,'*',i,'=',N*i,end='\n')

# 2번
T = int(input())
for i in range(T):
    A,B = map(int,input().split())
    print(A+B)

# 3번
n=int(input())
sum=0
for x in range(1,n+1):
    sum += x
print(sum)

# 4번
import sys
T = int(sys.stdin.readline())
for x in range(T):
    A,B = map(int,sys.stdin.readline().split())
    print(A+B)

# 5번
N = int(input())
for x in range(1,N+1):
    print(x)

# 6번
N = int(input())
for x in range(N,0,-1):
    print(x)

# 7번
T = int(input())
for x in range(T):
    A, B = map(int, input().split())
    print('Case #',x+1,': ',A+B,sep='')

# 8번
T = int(input())
for x in range(T):
    A, B = map(int, input().split())
    print('Case #',x+1,': ',A,' + ',B,' = ',A+B,sep='')

# 9번
N = int(input())
for x in range(N):
    print('*'*(x+1))

# 10번
N = int(input())
for x in range(N):
    print(' '*(N-x-1),'*'*(x+1),sep='')

# 11번
N,X = map(int,input().split())
A = list(map(int,input().split()))
for x in A:
    if x < X:
        print(x,end=' ')
