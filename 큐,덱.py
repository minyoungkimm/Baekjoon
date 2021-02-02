# # 큐 2
# import sys
# from collections import deque
#
# N=int(sys.stdin.readline())
# q=deque([])
#
# for _ in range(N):
#     command=sys.stdin.readline().rstrip()
#     if "push" in command:
#         p,n=command.split()
#         q.append(int(n))
#     elif command=="pop":
#         if len(q)==0:
#             print(-1)
#         else:
#             print(q.popleft())
#     elif command=="size":
#         print(len(q))
#     elif command=="empty":
#         if len(q)==0:
#             print(1)
#         else:
#             print(0)
#     elif command=="front":
#         if len(q)==0:
#             print(-1)
#         else:
#             print(q[0])
#     elif command=="back":
#         if len(q)==0:
#             print(-1)
#         else:
#             print(q[-1])

# # 카드
# import sys
# from collections import deque
#
# N=int(sys.stdin.readline())
# q=deque([i for i in range(1,N+1)])
#
# while len(q)!=1:
#     q.popleft()
#     q.append(q.popleft())
#
# print(q[0])


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




