# 1번
def solve(A):
    return sum(A)




# 2번
lst=list(range(1,10001))
remove=[]
for x in lst:
    for y in str(x):
        x += int(y)
    if x <= 10000:
        remove.append(x)

remove_list=list(set(remove))
for i in lst:
    if i not in remove_list:
        print(i)

# 2번 ver.2
def d(n):
    next_num=n
    for s in str(n):
        next_num +=int(s)

    if next_num <= 10000 and num[next_num]==0:
        num[next_num]=1
        return d(next_num)
    else:
        return

num=[0 for _ in range(10001)]
result=[]
for i in range(1,10001):
    if num[i] == 0:
        result.append(i)
        d(i)

print(result)



# 한수
number=int(input())

def count_hansu(num):
    hansu=0
    for x in range(1,num+1):
        if x < 100:
            hansu += 1
        else:
            y = str(x)
            if int(y[2]) - int(y[1]) == int(y[1]) - int(y[0]):
                hansu += 1
    return hansu

print(count_hansu(number))



### 한수 n자리
def count_hansu(num):
    hansu=0
    n_list=[int(i) for i in str(num)]
    if len(n_list) < 3:
        hansu = 1
    else:
        diff=n_list[1]-n_list[0]
        for i in range(1,len(n_list)-1):
            cdiff=n_list[i+1]-n_list[i]
            if diff != cdiff:
                hansu = 0
                break
            else:
                hansu = 1
    return hansu


number = int(input())
s = 0
for i in range(1,number + 1):
    s += count_hansu(i)
print(s)


#### zip이용
A = int(input())
cnt=0
for i in range(1,A+1):
    tmp=list(str(i))
    seq=[int(b)-int(a) for a,b in zip(tmp,tmp[1:])]
    if len(seq)<=1:
        cnt+=1
    else:
        if len(seq)==seq.count(seq[0]):
            cnt+=1

print(cnt)
