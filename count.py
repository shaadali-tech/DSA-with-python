from math import *
n=int(input("Enter a numbers :"))

num=n
count=0
while(num>0):
  count+=1
  num=num//10

print(count)

def counting(num):
  return int(log10(num)+1)

print(counting(num))