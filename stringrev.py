# str="nitin"

# list=str.split()
# list.reverse()
# print(list)

# n=int(input("Enter a  number upto you need fibonacci: "))

# a=0
# b=1
# for i in range(n):
#   print(a)
#   c=a+b
#   a=b
#   b=c

def fibonacci(num):
  if(num==0 or num==1):
    return num
  return fibonacci(num-1)+fibonacci(num-2)

print(fibonacci(5))