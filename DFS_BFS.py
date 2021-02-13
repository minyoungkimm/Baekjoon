# DFS와 BFS
from collections import defaultdict
from collections import deque

N,M,S=map(int,input().split())
V=defaultdict(list)


def dfs(node):
    print(node,end=' ')
    for i in V[node]:
        if visited[i]==0:
            visited[i]=1
            dfs(i)

def bfs(S):
    q=deque()
    q.appendleft(S)
    # visited[S]=1

    while q:
        node=q.pop()
        print(node,end=' ')
        for i in V[node]:
            if visited[i] == 0:
                q.appendleft(i)
                visited[i]=1



for _ in range(M):
    a,b=map(int,input().split())
    V[a].append(b)
    V[b].append(a)

for key in V:
    V[key].sort()


visited=[0]*(N+1)
visited[S]=1
dfs(S)
print()

visited=[0]*(N+1)
visited[S]=1
bfs(S)


# 바이러스
from collections import defaultdict
from collections import deque

N=int(input())
c=int(input())
V=defaultdict(list)


for _ in range(c):
    a,b=map(int,input().split())
    V[a].append(b)
    V[b].append(a)

# dfs방법
def virus(node):
    visited[node]=1
    for i in V[node]:
        if visited[i]==0:
            visited[i]=1
            virus(i)

# bfs방법
# def virus(node):
#     q = deque()
#     q.appendleft(node)
#     visited[node]=1
#     while q:
#         node = q.pop()
#         for i in V[node]:
#             if visited[i] == 0:
#                 q.appendleft(i)
#                 visited[i]=1


visited=[0]*(N+1)
virus(1)
print(sum(visited)-1)


# 단지번호붙이기
N=int(input())
m=[list(map(int,input())) for _ in range(N)]

visited=[[0]*N for _ in range(N)]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
result=[]

def dfs(x,y):
    cnt=0
    if m[x][y]==1 and visited[x][y]==0:
        visited[x][y]=1
        cnt+=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0 <= nx < N and 0<= ny < N:
                cnt+=dfs(nx,ny)
    return cnt

for i in range(N):
    for j in range(N):
        c=dfs(i,j)
        if c > 0 :
            result.append(c)

result.sort()
print(len(result))
print(*result,sep='\n')



# 유기농 배추
import sys
sys.setrecursionlimit(10**5)

T = int(input())

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def dfs(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<N and 0<=ny<M:
            if m[nx][ny] == 1:
                m[nx][ny] = -1
                dfs(nx, ny)


for _ in range(T):
    M, N, K = map(int,sys.stdin.readline().split())
    m = [[0]*M for _ in range(N)]
    cnt=0

    for _ in range(K):
        x,y = map(int,sys.stdin.readline().split())
        m[y][x]=1

    for i in range(N):
        for j in range(M):
            if m[i][j]==1:
                dfs(i,j)
                cnt += 1

    print(cnt)



# 미로 탐색
from collections import deque

N, M = map(int,input().split())
m=[list(map(int,input())) for _ in range(N)]

dx=[0,1,0,-1]
dy=[1,0,-1,0]

de=deque([[0,0]])

# bfs방법
while de:
    x, y = de[-1][0], de[-1][1]
    de.pop()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if m[nx][ny] == 1:
                de.appendleft([nx,ny])
                m[nx][ny] = m[x][y] + 1

print(m[N-1][M-1])



# 토마토
import sys
from collections import deque

M, N = map(int,sys.stdin.readline().split())
box=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
de=deque()


dx=[0,1,0,-1]
dy=[1,0,-1,0]

for i in range(N):
    for j in range(M):
        if box[i][j]==1:
            de.append((i,j))

while de:
    x, y = de.popleft()
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if 0<=nx<N and 0<=ny<M:
            if box[nx][ny]==0:
                de.append((nx,ny))
                box[nx][ny]=box[x][y]+1

day=-1
breaker=0

for i in range(N):
    for j in range(M):
        if box[i][j]==0:
            print(-1)
            breaker=1
            break
        else:
            if day<box[i][j]:
                day=box[i][j]
    if breaker==1:
        break
# print(box)
if breaker == 0:
    print(day-1)


