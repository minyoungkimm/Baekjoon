# # 스택
# import sys
# N = int(sys.stdin.readline())
# stack=[]
# for _ in range(N):
#     command=sys.stdin.readline().rstrip()
#     if "push" in command:
#         p,n=command.split()
#         stack.append(int(n))
#     elif command=='pop':
#         if len(stack)>0:
#             print(stack.pop(-1))
#         else:
#             print(-1)
#     elif command=='size':
#         print(len(stack))
#     elif command=='empty':
#         if len(stack)==0:
#             print(1)
#         else:
#             print(0)
#     elif command=='top':
#         if len(stack)>0:
#             print(stack[-1])
#         else:
#             print(-1)


# # 제로
# import sys
# K=int(sys.stdin.readline())
# stack=[]
#
# for _ in range(K):
#     num=int(sys.stdin.readline())
#     if num == 0:
#         stack.pop(-1)
#     else:
#         stack.append(num)
#
# print(sum(stack))


# # 괄호
# import sys
# T = int(sys.stdin.readline())
#
# for _ in range(T):
#     ps=sys.stdin.readline()
#     stack=list(ps)
#     sum=0
#
#     for i in stack:
#         if i == '(':
#             sum += 1
#         elif i == ')':
#             sum -= 1
#         if sum < 0 :
#             print('NO')
#             break
#
#     if sum > 0:
#         print('NO')
#     elif sum == 0:
#         print('YES')
