#Python core types

# number 
sum = 123 + 122
print(sum)
print(3.115*2)

import math
print(math.pi)
print(math.sqrt(4))

import random
print(random.random())

# string
str = 'Spam'
print(str)

print(str[0])
print(str[1:4])

str = "SpamAgain"
print(str)

print(str + "xyz")
print(str * 8)
print(str)

L = list(str)
print(L)
print(L[1])
print(L[1:5])
print(''.join(L))

# list
L = list("abcde")
print(L)
print(L[1])
print(L[1:5])
L.append('NI')
print(L)
L.pop(0)
print(L)
L.extend(['uiyr','658'])
print(L)
L.sort()
print(L)

M=[[1,2,3],
   [4,5,6],
   [7,8,9]]
print(M)
print(M[2])
print(M[2][2])

## list comprehension expression
col0 = [row[0] for row in M]
print(col0)
diag = [M[2-i][i] for i in [0, 1, 2]]
print(diag)
print(list(range(10)))
print(list(range(-10, 11, 2)))
cprl = [[i**2,i**3] for i in range(5)]
print(cprl)

print(M)
rsm = [sum(row) for row in M]
print(rsm)

G = (sum(row) for row in M)
for isum in G:
    print("isum", isum)
    
print("list(map(sum, M)): ", list(map(sum, M)))
for x in map(sum, M):
    print(x)
    
sumset = {sum(row) for row in M}
print(sumset)

sumdic = {i: sum(M[i]) for i in range(3)}
print(sumdic)
