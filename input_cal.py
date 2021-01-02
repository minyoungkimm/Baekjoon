# 1번
print('Hello World!')

# 2번
print('강한친구 대한육군\n강한친구 대한육군')

# 3번
print("\    /\\\n )  ( ')\n(  /  )\n \(__)|")

# 4번
print("|\_/|")
print("|q p|   /}")
print("( 0 )\"\"\"\\")
print("|\"^\"`    |")
print("||_/=\\\__|")

# 5번
A,B = input().split()
print(int(A) + int(B))

# 6번
A,B = input().split()
print(int(A) - int(B))

# 7번
A,B = input().split()
print(int(A)*int(B))

# 8번
A,B = input().split()
print(int(A)/int(B))

# 9번
A,B = map(int,input().split())
print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)

# 10번
A,B,C = map(int,input().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)

# 11번
A=int(input())
B=int(input())
s1=A*(B%10)
s2=A*((B%100)//10)
s3=A*(B//100)
s4=A*B
print(s1,s2,s3,s4,sep='\n')
