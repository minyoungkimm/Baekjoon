# 아스키 코드
alphabet=input()
print(ord(alphabet))

# 숫자의 합
N = int(input())
num = list(map(int,input()))
n_sum = sum(num)
print(n_sum)

# 알파벳 찾기
S = input()
for x in range(26):
    idx=S.find(chr(x+97)) # a : 97
    print(idx,end=' ')

# 문자열 반복
T = int(input())
for x in range(T):
    rep,text=input().split()
    for y in text:
        print(y*int(rep),end='')
    print()

# 문자열 반복 ver.2
for i in range(int(input())):
    n, word = input().split()
    n = int(n)
    print(''.join(j*n for j in word))



# 단어 공부
word = input().upper()
word_dup=list(set(word))
max=0
result=' '
for x in word_dup:
    count = word.count(x)
    if max == count:
        result='?'
    elif max < count:
        max = count
        result=x

print(result)

# 단어 공부 ver.2
S=input().upper()
alpha=[0 for _ in range(26)]

for s in S:
    alpha[ord(s)-ord('A')] += 1

max_cnt=max(alpha)
M=0
for i,cnt in enumerate(alpha):
    if max_cnt == cnt:
        M += 1
        max_alpha=chr(i+65)

if M >= 2:
    print('?')
else:
    print(max_alpha)

# 단어 공부 ver.3
S=input().upper()
alpha=[]
for i in range(65,91):
    alpha.append(S.count(chr(i)))
print('?' if alpha.count(max(alpha)) > 1 else chr(alpha.index(max(alpha))+65))


# 단어의 개수
# text = input().strip()
# word_cnt= text.split()
# print(len(word_cnt))

text = list(input().split())
print(len(text))

# 상수
A, B = input().split()
A = int(A[::-1])
B = int(B[::-1])
if A > B:
    print(A)
else:
    print(B)

# 다이얼
word=input()
alphabet_list=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
time=0
for x in alphabet_list:
    for y in x:
        for z in word:
            if z == y:
                time += alphabet_list.index(x) + 3

print(time)

# 크로아티아 알파벳
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

# 크로아티아 알파벳 ver.2
croatia_lst=['c=','c-','dz=','d-','lj','nj','s=','z=']
word=input()
for x in croatia_lst:
    word=word.replace(x,'#')
print(len(word))


# 그룹 단어 체커
N = int(input())
result=N
for _ in range(N):
    word = input()
    s=word[0]
    al_lst=[s]
    for j in range(1,len(word)):
        if word[j] == s:
            pass
        else:
            s = word[j]
            al_lst.append(s)
    if len(al_lst) != len(list(set(al_lst))):
        result -= 1

print(result)


# 그룹 단어 체커 ver.2
N=int(input())
for i in range(N):
    word=input()
    for j in range(1,len(word)):
        if word.find(word[j-1]) > word.find(word[j]):
            N -= 1
            break
print(N)

# 그룹 단어 체커 ver.3
N = int(input())
result=N
for _ in range(N):
    word = input()
    al_set=set()
    al_set.add(word[0])
    s=word[0]
    for w in word:
        if s == w:
            continue
        else:
            if w in al_set:
                N -= 1
                break
            else:
                al_set.add(w)
                s=w

print(N)