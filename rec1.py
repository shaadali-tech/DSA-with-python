
# count=0
# def greet(count):
#   print("Shaad")
#   if(count==4):
#     return
#   count+=1
#   return greet(count)

# greet(count)

# Recusrsion using parameter

def func(x,n):
  if(n==0):
    return
  print(x)
  return func(x,n-1)

func(7,4)