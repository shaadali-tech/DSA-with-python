# arr=[2,4,1,5,6,3,6,9,1,8]

# largest=arr[0]
# second=largest
# n=len(arr)
# for i in range(1,n):
#   if(arr[i]>largest):
#     second=largest
#     largest=arr[i]
#   elif arr[i] > second and arr[i] != largest:
#         second = arr[i]


# print(largest)
# print(second)

# arr=[1,2,3,4,5,6]

# for i in range(0,len(arr)-1):
#   if(arr[i]>arr[i+1]):
#     print("False")

    
# unique array elements

# freq_map={}

# for i in range(0,n):
#   freq_map[arr[i]]=0

# print(freq_map)

# j=0

# for k in freq_map:
#   arr[j]=k
#   j+=1

# print(arr)



# arr=[1,1,1,2,2,2,3,3,4,4,5,5,6,6]



# def unique(arr):
#   n=len(arr)
#   i=0
#   j=i+1
#   while(j<n):
#     if(arr[i]==arr[j]):
#       j+=1
#     elif(arr[i]!=arr[j]):
#       i+=1
#       arr[i],arr[j]=arr[j],arr[i]
#       j+=1
#   return i+1


# print(unique(arr))

# RIGHT ROTATE AN ARRAY
# arr=[1,2,3,4,5,6,7,8]

# n=len(arr)
# last=arr[n-1]


# for i in range(n-1,0,-1):
#   arr[i]=arr[i-1]

# arr[0]=last
# print(arr)

# LEFT ROTATE AN ARRAY

# arr=[1,2,3,4,5,6,7,8]

# n=len(arr)
# first=arr[0]

# for i in range(0,n-1):
#   arr[i]=arr[i+1]

# arr[n-1]=first
# print(arr)

# RIGHT ROTATE AN ARRAY BY K PLACES


# n=len(arr)
# last=arr[n-1]

# arr=[1,2,3,4,5,6,7,8]
# k=3
# n=len(arr)


# while(k>0):
#   last=arr[n-1]
#   for i in range(n-1,0,-1):
#     arr[i]=arr[i-1]
 
#   arr[0]=last
#   k-=1

# print(arr)

# for i in range(0,n-1):
#   if(arr[i]==0):
#     arr[i+1],arr[i]=arr[i],arr[i+1]

# print(arr)



# n = len(arr)

# temp = []
# count = 0

# for i in range(n):
#     if arr[i] != 0:
#         temp.append(arr[i])
#     else:
#         count += 1

# nz = len(temp)

# for i in range(nz):
#     arr[i] = temp[i]

# for i in range(nz, n):
#     arr[i] = 0

# print(arr)



# Linear Search
arr = [1,0,2,3,0,0,4,5,6,7]

target=3
n=len(arr)
for i in range(0,n):
  if arr[i]==target:
    print(i)





















