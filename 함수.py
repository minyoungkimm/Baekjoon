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

# 3번
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
