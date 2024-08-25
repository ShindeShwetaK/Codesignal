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
########################################################
#Q4.Find missing consuctive numbers
Statue=[6,2,3,8]# [2,3,4,5,6,7,8] 4 5 7 is missing
Statue.sort()
m=0
for i in range(0,len(Statue)-1):
    if Statue[i+1]-Statue[i]>1:
        m+=Statue[i+1]-Statue[i]-1
print(m)
##########################################################
#Q8. Matrix elemet Sum (only sum which does not have 0 above it
#https://www.youtube.com/watch?v=BB1RNQA78cg
Matrix=[[0,1,1,2],
        [0,5,0,0],
        [2,0,3,3]] #1+5+1+2=9
sum=0
for col in range(len(Matrix[0])):
    for row in range(len(Matrix)):
        if Matrix[row][col]==0:
            break
        elif row>0 and Matrix[row-1][col]==0:
            break
        else:
            sum+=Matrix[row][col]
print(sum)
################################################################
