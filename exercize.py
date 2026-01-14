def reversestring(s):
    return s[::-1]
print(reversestring("hello"))#reverse string

def pali(s):
    return s==s[::-1]
print(pali("madam"))
print(pali("sir"))# reverse palindrome

n = 5
fact = 1
for i in range(1,n+1):
    fact *= i
    print(fact)

import math
print(math.factorial(6))

n= int(input("enter hoe many terms you want: "))
a, b=0,1
for i in range(n):
    print(a,end=" ")
    a,b = b,a+b

    word = input("enter a word")
    count = {}
    for ch in word:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1
    print(count)       


    
