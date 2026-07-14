# now we are going to start solving array based dsa problems

# two pointer problem
# arr=[1,2,3,4,5,6,7,8]

# length=len(arr)
# left=0
# right=length-1

# while(left<right):
#   arr[left],arr[right]=arr[right],arr[left]
#   left+=1
#   right-=1

# print(arr)

# largest element in an array

# arr=[23,55,33,78,44,99,84]
# largest=arr[0]
# second=arr[1]
# for i in arr:
 
#   if i>largest:
#     second=largest
#     largest=i
#   elif i > second and i != largest:
#         second = i

# print(largest)
# print(second)

# array is sort or not

# arr=[1,2,3,4,5,6]
# flag=True
# print(len(arr))
# for i in range(0,len(arr)-1):
#   if arr[i]>arr[i+1]:
#     flag=False

# if flag:
#   print("array is sorted")

# remove duplicate elements from array

# arr = [1, 1, 1, 1, 2, 2, 3, 3, 3, 4]

# sorted=[arr[0]]
# for i in range(1,len(arr)):
#   if arr[i]!=arr[i-1]:
#     sorted.append(arr[i])
# print(sorted)

# move all zeroes to end

# arr=[1, 0, 2, 0, 4, 0, 5]

# nozeroes=[]
# count=0
# for i in range(0,len(arr)):
#   if(arr[i]!=0):
#     nozeroes.append(arr[i])
#   else:
#     count+=1

# for i in range(count):
#   nozeroes.append(0)

# print(nozeroes)
# print(count)

# left rotate an array

# arr=[1,2,3,4,5]

# first=arr[0]

# for i in range(len(arr)-1):
#   arr[i]=arr[i+1]

# arr[len(arr)-1]=first

# Right Shift n array

arr=[1,2,3,4,5,6]

length=len(arr)

last=arr[length-1]

for i in range(length-1,0,-1):
  arr[i]=arr[i-1]

arr[0]=last

print(arr)

















