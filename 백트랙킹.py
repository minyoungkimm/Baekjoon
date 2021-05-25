# 모든 경우를 탐색하는 백트랙킹 알고리즘
#
# N과 M(1) (15649번)
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 입력 : 첫째 줄에 자연수 N과 M이 주어짐
# 출력 : 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야함
N, M = map(int,input().split())
visited = [False] * N
out = []

def solve(depth, N, M):
    if depth == M: # 탈출 조건
        print(' '.join(map(str,out))) # list를 str으로 합쳐서 출력
        return
    for i in range(len(visited)): # 탐사 check 하면서
        if not visited[i]:  # 탐사 안했다면
            visited[i] = True  # 탐사 시작(중복 제거)
            out.append(i+1)  # 탐사 내용
            solve(depth + 1, N, M)  # 깊이 우선 탐색
            visited[i]=False  # 깊이 탐사 완료
            out.pop()  # 탐사 내용 제거

solve(0,N,M)


# N과 M(2) (15650번)
# 오름차순
N, M = map(int, input().split())
visited = [False] * N
out = []

out_list = []
def solve(depth, N, M):
    if depth == M:
        a = sorted(out)
        if a not in out_list:
            out_list.append(a)
            print(' '.join(map(str,a)))
        return
    for i in range(len(visited)):
        if not visited[i]:
            visited[i] = True
            out.append(i+1)
            solve(depth + 1, N, M)
            visited[i] = False
            out.pop()

solve(0,N,M)


# N과 M(2)_ver.2 (15650번)
N, M = map(int,input().split())

tmp = []
answer = []
def recur():
    if len(tmp) == M:
        print(' '.join(map(str,tmp)))
        return
    for i in range(1, N+1):
        if i not in tmp and (len(tmp) == 0 or i > tmp[-1]):
            tmp.append(i)
            recur()
            tmp.pop()

recur()


# N과 M(3) (15651번)
# 중복 허용
N, M = map(int, input().split())

tmp = []
answer = []
def recur():
    if len(tmp) == M:
        print(' '.join(map(str, tmp)))
        return
    for i in range(1, N+1):
        tmp.append(i)
        recur()
        tmp.pop()

recur()


# N과 M(3)_ver.2 (15651번)
from itertools import product

N, M = map(int, input().split())
p1 = list(map(str,range(1,N+1)))

for pro in list(product(p1, repeat=M)):
    print(' '.join(pro))


# N과 M(4) (15652번)
# 중복 가능
# 비내림차순이어야 함
N, M = map(int, input().split())
tmp = []

def recur():
    if len(tmp) == M:
        print(' '.join(map(str,tmp)))
        return
    for i in range(1, N+1):
        if len(tmp) == 0 or i >= tmp[-1]:
            tmp.append(i)
            recur()
            tmp.pop()

recur()


