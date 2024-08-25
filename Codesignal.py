#Q1. Given a year return its century
#1905=20 1700=15
import math
def centuryFromYear(year):
  return math.ceil(year/100)

print(math.ceil(1.4))  -->2
print(math.ceil(5.1))  -->6
print(math.ceil(-5.1))  -->-5
print(math.ceil(22.6))  -->23
print(math.ceil(10.2))  -->11

########################################
#Q2. Is palindrome or not?
def checkpalindrom(inputs):
  i=0
  j=len(inputs)-1
  while i<j:
    if inputs(i)!=inputs(j) return False
    i+=1
    j-=1
  return True
  #or
   return inputs[::-1]==inputs
##########################################
#Q3. Return the max product of the adjusent element from array
#will return the pairs and product
N=[1,2,3,4,-12,13,-5,6,-7]
i=0 
j=1
p=0
while j<len(N):
        pnew= N[i]*N[j]
        if pnew>p:
            pairs=[N[i],N[j]]
            p=pnew
        i+=1
        j+=1
print(p,pairs)
# will return pair
N=[1,2,3,4,-12,13,-5,6,-7]
i=0 
j=1
p=0
while j<len(N):
        pnew= N[i]*N[j]
        p=max(p,pnew)
        i+=1
        j+=1
print(p)
#or 
return max ([N[i]*N[i+1] for i in range(0,len(N)-1)])
