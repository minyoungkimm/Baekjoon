# 1번
A,B = map(int,input().split())
if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')

# 2번
score=int(input())
if score >= 90:
    print('A')
elif score >=80:
    print('B')
elif score >=70:
    print('C')
elif score >=60:
    print('D')
else:
    print('F')

# 3번
year=int(input())
if (year%4==0 and year%100!=0) or year%400==0:
    print(1)
else:
    print(0)

# 4번
x=int(input())
y=int(input())
if x > 0 and y > 0:
    print(1)
elif x > 0 and y < 0:
    print(4)
elif x < 0 and y > 0 :
    print(2)
else:
    print(3)

# 5번
H,M=map(int,input().split())
if M >= 45:
    print(H,M-45)
else:
    if H == 0:
        print(23,M+15)
    else:
        print(H-1,M+15)