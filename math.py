# # 손익분기점
# A, B, C = map(int,input().split())
#
# if B >= C:
#     print(-1)
# else:
#     print(int(A/(C-B)) + 1)

# 달팽이는 올라가고 싶다
A, B, V = map(int,input().split())
d=1
while True:
    if (A-B)*d + A >= V:
        print(d+1)
        break
    else:
        d += 1




