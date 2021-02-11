# # DFS와 BFS
# from collections import defaultdict
# from collections import deque
#
# N,M,S=map(int,input().split())
# V=defaultdict(list)
#
#
# def dfs(node):
#     print(node,end=' ')
#     for i in V[node]:
#         if visited[i]==0:
#             visited[i]=1
#             dfs(i)
#
# def bfs(S):
#     q=deque()
#     q.appendleft(S)
#     # visited[S]=1
#
#     while q:
#         node=q.pop()
#         print(node,end=' ')
#         for i in V[node]:
#             if visited[i] == 0:
#                 q.appendleft(i)
#                 visited[i]=1
#
#
#
# for _ in range(M):
#     a,b=map(int,input().split())
#     V[a].append(b)
#     V[b].append(a)
#
# for key in V:
#     V[key].sort()
#
#
# visited=[0]*(N+1)
# visited[S]=1
# dfs(S)
# print()
#
# visited=[0]*(N+1)
# visited[S]=1
# bfs(S)


# # 바이러스
# from collections import defaultdict
# from collections import deque
#
# N=int(input())
# c=int(input())
# V=defaultdict(list)
#
#
# for _ in range(c):
#     a,b=map(int,input().split())
#     V[a].append(b)
#     V[b].append(a)
#
# # dfs방법
# def virus(node):
#     visited[node]=1
#     for i in V[node]:
#         if visited[i]==0:
#             visited[i]=1
#             virus(i)
#
# # bfs방법
# # def virus(node):
# #     q = deque()
# #     q.appendleft(node)
# #     visited[node]=1
# #     while q:
# #         node = q.pop()
# #         for i in V[node]:
# #             if visited[i] == 0:
# #                 q.appendleft(i)
# #                 visited[i]=1
#
#
# visited=[0]*(N+1)
# virus(1)
# print(sum(visited)-1)


# # 단지번호붙이기
# N=int(input())
# m=[list(map(int,input())) for _ in range(N)]
#
# visited=[[0]*N for _ in range(N)]
# dx=[0,1,0,-1]
# dy=[1,0,-1,0]
# result=[]
#
# def dfs(x,y):
#     cnt=0
#     if m[x][y]==1 and visited[x][y]==0:
#         visited[x][y]=1
#         cnt+=1
#         for i in range(4):
#             nx=x+dx[i]
#             ny=y+dy[i]
#             if 0 <= nx < N and 0<= ny < N:
#                 cnt+=dfs(nx,ny)
#     return cnt
#
# for i in range(N):
#     for j in range(N):
#         c=dfs(i,j)
#         if c > 0 :
#             result.append(c)
#
# result.sort()
# print(len(result))
# print(*result,sep='\n')









