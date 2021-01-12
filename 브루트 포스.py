# # 블랙잭
# N,M=map(int,input().split())
# card=list(map(int,input().split()))
#
# sum_list=[]
# for idx,x in enumerate(card):
#     for idy,y in enumerate(card):
#         if idy != idx:
#             for idz,z in enumerate(card):
#                 if idz != idx and idz != idy:
#                     sum = x + y + z
#                     if sum <= M:
#                         sum_list.append(sum)
#
# print(max(sum_list))
#
# # 블랙잭 ver.2
# N, M = map(int, input().split())
# card = list(map(int, input().split()))
#
# sum = 0
# for i in range(N - 2):
#     for j in range(i + 1, N):
#         for k in range(j + 1, N):
#             card_sum=card[i] + card[j] + card[k]
#             if card_sum <= M and card_sum > sum:
#                 sum = card[i] + card[j] + card[k]
#
# print(sum)


# # 블랙잭 ver.3
# from itertools import combinations
#
# n, m = map(int, input().split())
# n_list = list(map(int, input().split()))
# combinations_n_list = list(combinations(n_list,3))
# answer = 0
#
# for i in combinations_n_list:
#     if answer < sum(i) and sum(i) <= m:
#         answer = sum(i)
#
# print(answer)

#


