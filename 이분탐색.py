# 수 찾기 (1920번)
import sys
n = sys.stdin.readline()
A = sorted(map(int, sys.stdin.readline().split()))

m = sys.stdin.readline()
B = map(int, sys.stdin.readline().split())


def binary_num(l, A, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if l == A[m]:
        return 1
    elif l < A[m]:
        return binary_num(l, A, start, m-1)
    else:
        return binary_num(l, A, m+1, end)

for l in B:
    start=0
    end = len(A)-1
    print(binary_num(l,A,start,end))



# 숫자 카드 2 (10816번)
import sys
N = sys.stdin.readline()
Nlist = sorted(map(int,sys.stdin.readline().split()))

M = sys.stdin.readline()
Mlist = map(int,sys.stdin.readline().split())


def binary_card(n, Nlist, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if n == Nlist[m]:
        return Nlist[start:end+1].count(n)
    elif n < Nlist[m]:
        return binary_card(n, Nlist, start, m-1)
    else:
        return binary_card(n, Nlist, m+1, end)

# for x in Mlist:
#     start=0
#     end=len(Nlist)-1
#     print(binary_card(x,Nlist,start,end),end=' ')

n_dic={}
for i in Nlist:
    start = 0
    end = len(Nlist) - 1
    if i not in n_dic:
        n_dic[i] = binary_card(i,Nlist,start,end)

print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in Mlist))



# 랜선 자르기(1654번)
import sys
K, N = map(int,sys.stdin.readline().split())

k_list = [int(sys.stdin.readline()) for _ in range(K)]
start = 1
end = max(k_list)


while start <= end:
    mid = (start + end)//2
    lines = 0
    for i in k_list:
        lines += i//mid

    if lines >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)



# 나무 자르기 (2805번)
N, M = map(int, input().split())
tree_list = list(map(int, input().split()))

start = 1
end = max(tree_list)

while start <= end:
    mid = (start + end) // 2
    tree = 0
    for i in tree_list:
        if i >= mid:
            tree += i - mid

    if tree >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)



# 공유기 설치 (2110번)
N, C = map(int,input().split())

house = sorted(list(int(input()) for _ in range(N)))

start = 1
end = house[-1] - house[0]
distance = 0

while start <= end:
    mid = (start + end) // 2
    old = house[0]
    cnt = 1

    for i in range(1, len(house)):
        if house[i] >= old + mid:
            cnt += 1
            old = house[i]

    if cnt >= C:
        start = mid + 1
        distance = mid
    else:
        end = mid - 1

print(distance)


# K번째 수 (1300번)
N = int(input())
K = int(input())

start = 1
end = K
answer = 0

while start <= end:
    mid = (start+end)//2
    count = 0
    for i in range(1,N+1):
        count += min(mid//i,N)

    if count < K:
        start = mid + 1
    else:
        answer = mid
        end = mid - 1

print(answer)



#가장 긴 증가하는 부분수열 (12015번)
import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
dp = [0]

for i in range(n):
    low = 0                # 시작 위치
    high = len(dp) - 1     # 끝 위치
    while low <= high:
        mid = (low+high)//2
        if dp[mid] < A[i]:
            low = mid + 1
        else:
            high = mid - 1
    if low >= len(dp):
        dp.append(A[i])
    else:
        dp[low] = A[i]

print(len(dp)-1)

### bisect 이용 ###
import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().rsplit()))
dp = []

for i in A:
    k = bisect_left(dp, i)
    if len(dp) <= k:
        dp.append(i)
    else:
        dp[k] = i

print(len(dp))




