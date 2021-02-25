# 큐 2
import sys
from collections import deque

N=int(sys.stdin.readline())
q=deque([])

for _ in range(N):
    command=sys.stdin.readline().rstrip()
    if "push" in command:
        p,n=command.split()
        q.append(int(n))
    elif command=="pop":
        if len(q)==0:
            print(-1)
        else:
            print(q.popleft())
    elif command=="size":
        print(len(q))
    elif command=="empty":
        if len(q)==0:
            print(1)
        else:
            print(0)
    elif command=="front":
        if len(q)==0:
            print(-1)
        else:
            print(q[0])
    elif command=="back":
        if len(q)==0:
            print(-1)
        else:
            print(q[-1])

# 카드
import sys
from collections import deque

N=int(sys.stdin.readline())
q=deque([i for i in range(1,N+1)])

while len(q)!=1:
    q.popleft()
    q.append(q.popleft())

print(q[0])


# 프린터 큐
from collections import deque
N=int(input())

for _ in range(N):
    c,n=map(int,input().split())
    pri=deque(map(int,input().split()))
    cnt=0
    while pri:
        m=max(pri)
        n -= 1
        p=pri.popleft()
        if m != p:
            pri.append(p)
            if n < 0:
                n = len(pri) - 1
        else:
            cnt += 1
            if n == -1:
                print(cnt)
                break


# 덱
import sys
from collections import deque

N=int(input())
de=deque([])
for _ in range(N):
    command=sys.stdin.readline().rstrip()
    if ' ' in command:
        c,n=command.split()
        if c == 'push_front':
            de.appendleft(int(n))
        elif c == 'push_back':
            de.append(int(n))

    elif command == 'pop_front':
        if len(de) == 0:
            print(-1)
        else:
            print(de.popleft())

    elif command == 'pop_back':
        if len(de) == 0:
            print(-1)
        else:
            print(de.pop())

    elif command == 'size':
        print(len(de))

    elif command == 'empty':
        if len(de) == 0:
            print(1)
        else:
            print(0)

    elif command == 'front':
        if len(de) == 0:
            print(-1)
        else:
            print(de[0])

    elif command == 'back':
        if len(de) == 0:
            print(-1)
        else:
            print(de[-1])


# 회전하는 큐
import sys
from collections import deque

N, M= map(int,sys.stdin.readline().split())
de = deque([i for i in range(1,N)])
idx= list(map(int,sys.stdin.readline().split()))

cnt=0
for i in idx:
    id = de.index(i)
    s=min(id, len(de) - id)
    cnt += s
    if s == id:
        de.rotate(-id)
    else:
        de.rotate(len(de)-id)
    de.popleft()


print(cnt)


# 요세푸스 문제 0
from collections import deque
N, K = map(int,input().split())
de=deque([i for i in range(1,N+1)])
del_list=[]

while len(de)!=1:
    de.rotate(-K+1)
    del_list.append(de.popleft())

del_list.append(de[0])


print('<'+', '.join(map(str,del_list))+'>')


# # 프린터 큐
# T = int(input())
# for _ in range(T):


