
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

def func(n):
  if(n==1):
    return 1
  return n+func(n-1)

print(func(4))