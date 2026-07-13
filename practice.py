# i am going to practice 20+ programs

# n=int(input("Enter an integer :"))

# digit=len(str(n))
# sum=0
# for i in str(n):
#   sum=sum+int(i)**digit

# print(sum)

# n1=int(input("enter an integer 1:"))
# n2=int(input("Enter an integer 2 :"))

# n1,n2=n2,n1

# print(f"n1 is {n1} ")
# print(f"n2 is {n2} ")

# num=int(input("enter an integer :"))

# if(num%2==0):
#   print("even")
# else:
#   print("odd")

# n1=int(input("enter an integer 1 :"))
# n2=int(input("enter an integer 2 :"))
# print(max(n1,n2))

#fibonacci using factorial

# def fibonacci(num):
#   if(num==0):
#     return 0
#   if(num==1):
#     return 1
  
#   return fibonacci(num-1)+fibonacci(num-2)



# print(fibonacci(7))

# n=int(input("Enter a number upto which fibonacci you need :"))
# a=0
# b=1
# for i in range(n):
#   print(a)
#   c=a+b
#   a=b
#   b=c


# num=int(input("Enter a number to reverse :"))
# rev=0

# while(num>0):
#   digit=num%10
#   rev=rev*10+digit
#   num=num//10

# print(rev)

# num=int(input("enter a number upto which you want to check prime number : "))

# if(num<=2):
#   print("enter number greater than 2")
# else:
#   for i in range(2,num+1):
#     is_prime=True
#     for j in range(2,i):
#       if(i%j==0):
#         is_prime=False
#         break
#     if is_prime:
#       print(i)



# now a program for gcd

# n1=int(input("Enter an integer value n1 :"))
# n2=int(input("Enter an integer value n2 :"))

# mini=min(n1,n2)
# gcd=1
# for i in range(1,mini+1):
#   if(n1%i==0) and (n2%i==0):
#     gcd=i
# print(gcd)   

# num=int(input("enter a number to check whether its prime or not :"))

# if(num<2):
#   print("enter a greater number ")


# for i in range(2,num):
#   flag=True
#   for j in range(2,i):
#     if(i%j)==0:
#       flag=False
#       break
#   if flag:
#     print(f"yes prime number{i}")




# mini=min(n1,n2)
# gcd=1

# for i in range(1,mini+1):
#   if(n1%i==0) and (n2%i==0):
#     gcd=i
# print(gcd)

# now code for LCM

# code for LCM


# n1=int(input("Enter an integer value 1 :"))
# n2=int(input("Enter an integer value 2 :"))

# maximum=max(n1,n2)

# while True:
#   if(maximum%n1==0) and (maximum%n2==0):
#     print(maximum)
#     break
#   maximum+=1


# num=int(input("enter digits of numbers :"))
# string=str(num)

# sum=0
# for i in string:
#   sum+=int(i)

# print(sum)

# now a program for a perfect number

num=int(input("enter a number :"))
original=num
sum=0
for i in range(1,num):
  if(num%i==0):
    sum+=i

if sum==original:
  print("perfect")