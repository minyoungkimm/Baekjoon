# 1번
N = int(input())
L = list(map(int,input().split()))
L.sort()

print(L[0],L[-1])

# 2번
num_list=[]
for x in range(9):
    num=int(input())
    num_list.append(num)

sort_list=sorted(num_list)
max=sort_list[-1]
print(max,num_list.index(max)+1,sep='\n')

# 3번
A = int(input())
B = int(input())
C = int(input())
result=str(A*B*C)

for x in range(10):
    x=str(x)
    print(result.count(x))

# 4번
remain_list=[]
for x in range(10):
    num=int(input())
    remain_list.append(num%42)

print(len(set(remain_list)))

# 5번
N = int(input())
score = list(map(int,input().split()))
score.sort()
max = score[-1]
sum=0

for x in score:
    sum += x/max*100

print(sum/len(score))

# 6번
T = int(input())

for x in range(T):
    ox = input()
    score = 0
    cnt = 0
    for y in range(len(ox)):
        if ox[y] == 'O':
            cnt += 1
            score += cnt
        elif ox[y] == 'X':
            cnt = 0
    print(score)

# 7번
C = int(input())
for x in range(C):
    score=list(map(int,input().split()))
    mean=sum(score[1:])/score[0]
    cnt=0
    for y in score[1:]:
        if y > mean:
            cnt += 1
    print(format(cnt/(len(score)-1)*100,'.3f'),'%',sep='')


