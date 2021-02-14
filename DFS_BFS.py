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
            de.append([i,j])

while de:
    x, y = de.popleft()
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if 0<=nx<N and 0<=ny<M:
            if box[nx][ny]==0:
                de.append([nx,ny])
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



# 토마토 (3차원)
import sys
from collections import deque

M, N, H = map(int,sys.stdin.readline().split())
box=[[list(map(int,sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
c=[[[0]*M for _ in range(N)]for _ in range(H)]
de=deque()


dx=[0,1,0,-1,0,0]
dy=[1,0,-1,0,0,0]
dz=[0,0,0,0,1,-1]

for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1 and c[i][j][k] == 0:
                de.append([i,j,k])
                c[i][j][k] = 1


def bfs():
    while de:
        z, y, x = de.popleft()
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
                if box[nz][ny][nx] == 0 and c[nz][ny][nx] == 0:
                    de.append([nz, ny, nx])
                    box[nz][ny][nx] = 1
                    c[nz][ny][nx] = c[z][y][x] + 1


bfs()

for i in box:
    for j in i:
        if 0 in j:
            print(-1)
            sys.exit()

day = 0
for i in c:
    for j in i:
        max_day = max(j)
        day = max(day,max_day)

print(day-1)


# 숨바꼭질
N, K = map(int,input().split())

d=[0 for _ in range(100001)]
max_d = 100000

from collections import deque

def bfs(n):
    de=deque()
    de.append(n)
    d[n] = 1
    while de:
        l=de.popleft()
        if l + 1 <= max_d and d[l+1] == 0:
            de.append(l+1)
            d[l+1] = d[l] + 1
        if l - 1 >= 0 and d[l-1] == 0:
            de.append(l-1)
            d[l-1] = d[l] + 1
        if l * 2 <= max_d and d[l * 2] == 0:
            de.append(l*2)
            d[l*2] = d[l] + 1

bfs(N)
print(d[K]-1)


# 벽 부수고 이동하기
from collections import deque

N, M = map(int,input().split())
m = [list(map(int,input())) for _ in range(N)]
c = [[[0]*2 for _ in range(M)] for _ in range(N)]
de=deque()

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def bfs():
    de.append([0,0,1])
    c[0][0][1] = 1
    while de:
        x, y, z = de.popleft()
        if x == N -1 and y == M -1:
            return c[x][y][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if m[nx][ny] == 1 and z == 1:
                    c[nx][ny][0] = c[nx][ny][1] + 1
                    de.append([nx,ny,0])
                elif m[nx][ny] == 0 and c[nx][ny][z] == 0:
                    c[nx][ny][z] = c[x][y][z] + 1
                    de.append([nx,nx,z])
    return -1

print(bfs())



