# 모든 경우를 탐색하는 백트랙킹 알고리즘

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
# N, M = map(int,input().split())
#
# tmp = []
# answer = []
# def recur():
#     if len(tmp) == M:
#         print(' '.join(map(str,tmp)))
#         return
#     for i in range(1, N+1):
#         if i not in tmp and (len(tmp) == 0 or i > tmp[-1]):
#             tmp.append(i)
#             recur()
#             tmp.pop()
#
# recur()


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
# from itertools import product
#
# N, M = map(int, input().split())
# p1 = list(map(str,range(1,N+1)))
#
# for pro in list(product(p1, repeat=M)):
#     print(' '.join(pro))


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



# N-Queen (9663번)
# 크기가 N x N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램 작성
#
# 스도쿠 (2580번)
import sys
sudoku = [list(map(int,sys.stdin.readline().split())) for _ in range(9)]
emptyspace = [(i,j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

def candidating(y,x):
    numbers = [i + 1 for i in range(9)]
    # 행/열 검사
    for k in range(9):
        if sudoku[y][k] in numbers:
            numbers.remove(sudoku[y][k])
        if sudoku[k][x] in numbers:
            numbers.remove(sudoku[k][x])
    # 3 x 3 검사
    y = y//3
    x = x//3
    for i in range(y*3, (y+1)*3):
        for j in range(x*3, (x+1)*3):
            if sudoku[i][j] in numbers:
                numbers.remove(sudoku[i][j])
    return numbers

def dfs(count):
    if count == len(emptyspace):
        for row in sudoku:
            print(*row)
        return
    (i,j) = emptyspace[count]
    candi = candidating(i,j)
    for num in candi:
        sudoku[i][j] = num
        dfs(count+1)
        sudoku[i][j] = 0

dfs(0)


# 스도쿠_ver.2 (2580번)
import sys

sdk = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if sdk[i][j] == 0]


def sudoku(index):
    # 한 바퀴에서 모든 경우를 다 보았으면 출력
    if index == len(zeros):  # 더이상 넣을곳이 없어지면
        for row in sdk:
            print(*row)
        sys.exit(0)  # 하나이상 있을시 하나만 출력

    x = zeros[index][0]  # 넣을곳의 x좌표
    y = zeros[index][1]  # 넣을곳의 y좌표
    dx = (x // 3) * 3
    dy = (y // 3) * 3

    # 사용할 수 있는 숫자 9개 0은 못쓰기때문에 처음부터 false로 둔다.
    num_list = [0] + [1 for _ in range(9)]
    ## 가로세로 박스를 검사해 넣을수 있는숫자만 true로 남긴다.
    for j in range(9):
        # 가로 검사
        if (sdk[x][j]):  # 가로의 숫자 체크 불가능한 숫자 모두 num list에서 false로 만들어줌
            num_list[sdk[x][j]] = 0
            # 세로 검사
        if (sdk[j][y]):  # 세로의 숫자 체크
            num_list[sdk[j][y]] = 0

        # 3*3 box 검사
    for i in range(dx, dx + 3):
        for j in range(dy, dy + 3):
            check_num = sdk[i][j]
            if (check_num):
                num_list[check_num] = 0

        # 현재 가능한 수(후보숫자)만 가져옴
        # 가능한 수를 가져왔으면, 이전에 다뤄왔던 백트래킹을 사용하면 됨
    candidate_list = []
    for i in range(len(num_list)):
        if num_list[i] == 1:
            candidate_list.append(i)

    # 후보숫자 하나씩 넣어봄
    for num in candidate_list:
        sdk[x][y] = num
        sudoku(index + 1)  # 다음 칸
        sdk[x][y] = 0


sudoku(0)


# 연산자 끼워넣기 (14888번)
import sys
input = sys.stdin.readline

N = int(input())

num = list(map(int,input().split()))
operation = list(map(int,input().split())) # [덧셈, 뺄셈, 곱셉, 나눗셈]

max_result = -100000001
min_result = 100000001


def make_cal(cnt, result, p, m, mul, div):
    global max_result
    global min_result
    if cnt == N:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    if p:
        make_cal(cnt+1, result+num[cnt], p-1, m, mul, div)
    if m:
        make_cal(cnt+1, result-num[cnt], p, m-1, mul, div)
    if mul:
        make_cal(cnt + 1, result * num[cnt], p, m, mul - 1, div)
    if div:
        make_cal(cnt + 1, -(-result // num[cnt]) if result < 0 else result // num[cnt], p, m, mul, div - 1)


make_cal(1, num[0], operation[0], operation[1], operation[2], operation[3])

print(max_result)
print(min_result)



# 연산자 끼워넣기_ver.2 (14888번)
# permutation함수 사용
from itertools import permutations
from collections import deque
import copy
import sys

def solve(n, num_list, operation_count_list):
    op = ['+','-','*','//']
    operation_list =[]
    max = -sys.maxsize -1
    min = sys.maxsize
    for i in range(4):
        operation = op[i]
        count = operation_count_list[i]
        temp = [operation]*count
        operation_list.extend(temp)
    # 중복 제거
    case_list = set(permutations(operation_list, n-1))

    for case in case_list:
        temp_list = deque(copy.deepcopy(num_list)) # deepcopy : 내부 객체들까지 모두 새롭게 copy
        idx = -1
        result = temp_list.popleft()
        while temp_list:
            idx += 1
            next_num = temp_list.popleft()
            current_op = case[idx]

            if current_op == '+':
                result += next_num
            elif current_op == '-':
                result -= next_num
            elif current_op == '*':
                result *= next_num
            else:
                if result < 0:
                    result = -result
                    result //= next_num
                    result = -result
                else:
                    result //= next_num

        if result < min:
            min = result
        if max < result:
            max = result

    return max, min

if __name__ == '__main__':
    N = int(input().strip())
    num_list = deque(list(map(int, input().strip().split())))
    operation_count_list = deque(list(map(int, input().split())))

    max, min = solve(N, num_list, operation_count_list)
    print(max)
    print(min)


# 스타트와 링크 (14889번)
from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
S = [list(map(int,input().split())) for _ in range(N)]

members = [i for i in range(N)]
possible_team = []


for team in list(combinations(members, N//2)):
    possible_team.append(team)

print(possible_team)

min_stat_gap = 10000
for i in range(len(possible_team)//2):
    team = possible_team[i]
    stat_A = 0
    for j in range(N//2):
        member = team[j]
        for k in team:
            stat_A += S[member][k]

    team = possible_team[-i-1]
    stat_B = 0
    for j in range(N//2):
        member = team[j]
        for k in team:
            stat_B += S[member][k]

    min_stat_gap = min(min_stat_gap, abs(stat_A- stat_B))

print(min_stat_gap)






