# # 팩토리얼
# N = int(input())
#
# def factorial(num):
#     if num == 0:
#         return 1
#     result = 1
#     while True:
#         result *= num
#         num -= 1
#         if num == 0:
#             break
#     return result
#
# print(factorial(N))

# 팩토리얼
n=int(input())
def fac(n):
    if n <=1:
        return 1
    else:
        return n*fac(n-1)

print(fac(n))

# 피보나치 수
n=int(input())

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

print(fibo(n))


# 별 찍기
def star(n):
    lst=[]
    for i in range(3*len(n)):
        if i // len(n) == 1:
            lst.append(n[i%len(n)]+' '*len(n)+n[i%len(n)])
        else:
            lst.append(n[i % len(n)] * 3)
    return lst

n=int(input())
l=['***','* *','***']
e=0
while n!=3:
    n=n//3
    e+=1

for _ in range(e):
    l = star(l)

for i in l:
    print(i)


# 하노이 탑 이동 순서
def hanoi(n,a,b,c):
    if n == 1:
        move.append([a,c])
    else:
        hanoi(n-1,a,c,b)
        move.append([a,c])
        hanoi(n-1,b,a,c)

move=[]
n=int(input())
hanoi(n,1,2,3)

print(len(move))
for i in move:
    for j in i:
        print(j,end=' ')
    print()



