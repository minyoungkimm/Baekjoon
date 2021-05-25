# DFS와 BFS
from collections import defaultdict
from collections import deque

N,M,S = map(int,input().split())
V = defaultdict(list)

for _ in range(M):
    a,b = map(int,input().split())
    V[a].append(b)
    V[b].append(a)

for key in V:
    V[key].sort()


# DFS방법
visited=[0]*(N+1)
visited[S]=1

def dfs(node):
    print(node, end=' ')
    for i in V[node]:
        if visited[i]==0:
            visited[i]=1
            dfs(i)

dfs(S)
print()


# BFS방법
visited=[0]*(N+1)
visited[S]=1

def bfs(S):
    q=deque()
    q.append(S)

    while q:
        node=q.pop()
        print(node, end=' ')
        for i in V[node]:
            if visited[i]==0:
                visited[i]=1
                q.appendleft(i)

bfs(S)
print()


# 바이러스
from collections import deque
from collections import defaultdict

N = int(input())
p = int(input())
V = defaultdict(list)

for _ in range(p):
    a, b = map(int, input().split())
    V[a].append(b)
    V[b].append(a)

for key in V:
    V[key].sort()


# 방문 체크 리스트
visited = [0] * (N+1)

# dfs 방법
def virus(node):
    visited[node] = 1
    for i in V[node]:
        if visited[i] == 0:
            visited[i] = 1
            virus(i)

# bfs 방법
# def virus(node):
#     q = deque()
#     q.append(node)
#
#     while q:
#         node = q.pop()
#         for i in V[node]:
#             if visited[i] == 0:
#                 visited[i] = 1
#                 q.appendleft(i)

virus(1)
print(sum(visited)-1)


# 단지 번호 붙이기
N = int(input())
m = [list(map(int, input())) for _ in range(N)]


visited = [[0] * N for _ in range(N)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
result = []

def dfs(x,y):
    cnt = 0
    if m[x][y] == 1 and visited[x][y] == 0:
        visited[x][y] = 1
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                cnt += dfs(nx,ny)
    return cnt

for i in range(N):
    for j in range(N):
        c = dfs(i,j)
        if c > 0:
            result.append(c)

result.sort()
print(len(result))
print(*result,sep='\n')


# 유기농 배추
T = int(input())

dx = [0,1,0,-1]
dy = [1,0,-1,0]


def dfs(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if m[nx][ny] == 1:
                m[nx][ny] = -1
                dfs(nx,ny)


for _ in range(T):
    N, M, K = map(int,input().split())
    m = [[0] * M for _ in range(N)]


    for _ in range(K):
        a, b = map(int, input().split())
        m[a][b]=1


    cnt = 0
    for i in range(N):
        for j in range(M):
            if m[i][j] == 1:
                dfs(i,j)
                cnt += 1

    print(cnt)


# 미로 탐색 (2178번)
from collections import deque

N, M = map(int,input().split())
m=[list(map(int,input())) for _ in range(N)]

dx=[0,1,0,-1]
dy=[1,0,-1,0]

de = deque([[0,0]])

def bfs():
    while de:
        x, y = de.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if m[nx][ny] == 1:
                    de.appendleft([nx,ny])
                    m[nx][ny] = m[x][y] + 1

bfs()
print(m[N-1][M-1])


# 토마토 (7576번)
from collections import deque

N, M = map(int,input().split())
m = [list(map(int,input().split())) for _ in range(M)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
de = deque()

for i in range(M):
    for j in range(N):
        if m[i][j] == 1:
            de.appendleft([i,j])


def bfs():
    while de:
        x, y = de.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if m[nx][ny] == 0:
                    m[nx][ny] = m[x][y] + 1
                    de.appendleft([nx,ny])

bfs()

max = -1
flag=False
for i in range(M):
    for j in range(N):
        if m[i][j] == 0:
            flag=True
            break
        if m[i][j] > max:
            max = m[i][j]
    if flag == True:
        print(-1)
        break

if flag == False:
    print(max-1)


# 토마토 3차원 (7569번)
from collections import deque
import sys

r=sys.stdin.readline
M, N, H = map(int,r().split())
box = [list(list(map(int,r().split())) for _ in range(N)) for _ in range(H)]

dx = [0,1,0,-1,0,0]
dy = [1,0,-1,0,0,0]
dz = [0,0,0,0,1,-1]

de = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                de.appendleft([i,j,k])


def bfs():
    while de:
        z, y, x = de.pop()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
                if box[nz][ny][nx] == 0:
                    de.appendleft([nz,ny,nx])
                    box[nz][ny][nx] = box[z][y][x] + 1


bfs()

flag = False
day = -1
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 0:
                flag=True
                print(-1)
                sys.exit()
            else:
                if box[i][j][k] > day:
                    day = box[i][j][k]


if flag == False:
    print(day-1)


# 벽 부수고 이동하기 (2206번)
from collections import deque

N, M = map(int,input().split())
map = [list(map(int,input())) for _ in range(N)]
c = [list([0]*2 for _ in range(M)) for _ in range(N)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def collapse_wall():
    de = deque()
    de.append([0,0,1])
    c[0][0][1] = 1
    while de:
        x, y, z = de.popleft()
        if x == N - 1 and y == M - 1:
            return c[x][y][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if map[nx][ny] == 1 and z == 1:
                    c[nx][ny][0] = c[x][y][1] + 1
                    de.append([nx,ny,0])
                elif map[nx][ny] == 0 and c[nx][ny][z] == 0:
                    c[nx][ny][z] = c[x][y][z] + 1
                    de.append([nx,ny,z])
    return -1

print(collapse_wall())



# 나이트의 이동 (7562번)
from collections import deque

T = int(input())
dx = [1,2,2,1,-1,-2,-2,-1]
dy = [2,1,-1,-2,-2,-1,1,2]

def moving_n(sx,sy,tx,ty):
    de=deque()
    de.append([sx,sy])
    visited[sx][sy]=1
    while de:
        x, y = de.popleft()
        if x == tx and y == ty:
            print(visited[x][y] - 1)
            return
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    de.append([nx,ny])
    # print(visited[tx][ty] - 1)
    # return

for _ in range(T):
    l = int(input())
    sx, sy = map(int,input().split())
    tx, ty = map(int,input().split())
    visited = [[0] * l for _ in range(l)]
    moving_n(sx,sy,tx,ty)



# 1707
from collections import  deque
import sys

r = sys.stdin.readline
K = int(input())

def Bipartite_Graph(x):
    visited[x] = 1
    de = deque()
    de.append(x)
    while de:
        a = de.popleft()
        for i in dd[a]:
            if visited[i] == 0:
                visited[i] = -visited[a]
                de.append(i)
            else:
                if visited[i] == visited[a]:
                    return False
    return True


for _ in range(K):
    V , E = map(int,r().split())
    dd = [[] for _ in range(V+1)]
    visited = [0]*(V+1)
    flag=1
    for _ in range(E):
        a, b = map(int,r().split())
        dd[a].append(b)
        dd[b].append(a)
    for i in range(1, V + 1):
        if visited[i] == 0:
            if not Bipartite_Graph(i):
                flag = -1
                break
    print('YES' if flag == 1 else 'NO')

