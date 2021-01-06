# 1번
alphabet=input()
print(ord(alphabet))

# 2번
N = int(input())
num = list(map(int,input()))
n_sum = sum(num)
print(n_sum)

# 3번
S = input()
for x in range(26):
    idx=S.find(chr(x+97)) # a : 97
    print(idx,end=' ')

# 4번
T = int(input())
for x in range(T):
    rep,text=input().split()
    for y in text:
        print(y*int(rep),end='')
    print()

# 4번 ver.2
for i in range(int(input())):
    n, word = input().split()
    n = int(n)
    print(''.join(j*n for j in word))

# 5번
word = input().upper()
word_dup=list(set(word))
max=0
for x in word_dup:
    count = word.count(x)
    if max == count:
        result='?'
    elif max < count:
        max = count
        result=x

print(result)

# 6번
text = input().strip()
word_cnt= text.split()
print(len(word_cnt))

text = list(input().split())
print(len(text))

# 7번
A, B = input().split()
A = int(A[::-1])
B = int(B[::-1])
if A > B:
    print(A)
else:
    print(B)

# 8번
word=input()
alphabet_list=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
time=0
for x in alphabet_list:
    for y in x:
        for z in word:
            if z == y:
                time += alphabet_list.index(x) + 3

print(time)

# 9번
word=input()
croatia_lst=['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt = 0
idx=-1
for i in croatia_lst:
    while True:
        idx = word.find(i,idx+1)
        if idx == -1:
            break
        else:
            cnt += 1
            word=word.replace(i,' ',1)

split_lst=word.split()
for sp in split_lst:
    cnt += len(sp)

print(cnt)

# 9번 ver.2
croatia_lst=['c=','c-','dz=','d-','lj','nj','s=','z=']
word=input()
for x in croatia_lst:
    word=word.replace(x,'#')
print(len(word))


# 10번
N = int(input())
result=N
for i in range(N):
    word = input()
    s=word[0]
    al_lst=[s]
    for j in word[1:]:
        if j == s:
            pass
        else:
            s = j
            al_lst.append(s)
    if len(al_lst) != len(list(set(al_lst))):
        result -= 1

print(result)

# 10번 ver.2
N=int(input())
for i in range(N):
    word=input()
    for j in range(1,len(word)):
        if word.find(word[j-1]) > word.find(word[j]):
            N -= 1
            break
print(N)
