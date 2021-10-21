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

