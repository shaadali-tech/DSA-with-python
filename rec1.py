
# count=0
# def greet(count):
#   print("Shaad")
#   if(count==4):
#     return
#   count+=1
#   return greet(count)

# greet(count)

# Recusrsion using parameter

# def func(x,n):
#   if(n==0):
#     return
#   print(x)
#   return func(x,n-1)

# func(7,4)

# def fun(sum,n):
#   if(n<0):
#     return sum
#   sum=sum+n
#   return fun(sum,n-1)
  
# print(fun(0,10))

# def func(n):
#   if(n==1):
#     return 1
#   return n+func(n-1)

# print(func(4))

# def factorial(n):
#   if(n==0 or n==1):
#     return 1
#   return n*factorial(n-1)

# print(factorial(9))

nums=[1,2,3,4,5,6,7,8]


i=len(nums)-1
while(i>=0):
  print(nums[i],end="")
  i-=1


