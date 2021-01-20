# # 수 정렬하기
# N = int(input())
#
# s_list=[int(input()) for _ in range(N)]
#
# result=sorted(s_list)
# print(*result,sep='\n')

# # 수 정렬하기 2
# N = int(input())
#
# s2=[int(input()) for _ in range(N)]
#
#
# def merge(left,right):
#     v=[]
#     i,j=0,0
#     while i<len(left) and j<len(right):
#         if left[i]<=right[j]:
#             v.append(left[i])
#             i+=1
#         else:
#             v.append(right[j])
#             j+=1
#         if i == len(left):
#             v+=right[j:len(right)]
#         if j == len(right):
#             v+=left[i:len(left)]
#         return v
#
# def sort_(l):
#     if len(l)<=1:
#         return l
#     mid=len(l)//2
#     left=sort_(l[:mid])
#     right=sort_(l[mid:])
#     return merge(left,right)
#
# result=sort_(s2)
# print(*s2,sep='\n')



# 통계학
from collections import Counter
import sys

N = int(input())
num = [int(sys.stdin.readline()) for _ in range(N)]

### 평균
print(round(sum(num)/len(num)))

### 중앙값
num=sorted(num)
idx=len(num)//2
print(num[idx])


### 최빈값
count=Counter(num)
count=count.most_common()
most=count[0][1]

mode_list=[]
for i in count:
    if i[1] == most:
        mode_list.append(i[0])

sort_most=sorted(mode_list)
if len(sort_most) != 1:
    print(sort_most[1])
else:
    print(sort_most[0])

### 범위
print(max(num)-min(num))



