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

arr=[23,55,33,78,44,99,84]
largest=arr[0]
second=arr[1]
for i in arr:
 
  if i>largest:
    second=largest
    largest=i
  elif i > second and i != largest:
        second = i

print(largest)
print(second)