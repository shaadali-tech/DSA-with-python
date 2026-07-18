# arr=[1,2,31,1,1,1,5,4,6,3,1,1,1,1,1]
# n=len(arr)
# count=0
# maxi=0

# for i in range(0,n):
#   if arr[i]==1:
#     count+=1
#     maxi=max(maxi,count)
#   else:
#     count=0

# print(maxi)

# n=len(nums)
# maxi=float("-inf")

# for i in range(0,n):
#   total=0
#   for j in range(i,n):
#     total=total+nums[j]
#     maxi=max(maxi,total)

# print(maxi)

nums=[-2,1,-3,4,-1,2,1,-5,4]
n=len(nums)
total=0
maxi=float("-inf")
for i in range(0,n):
  total=total+nums[i]
  maxi=max(maxi,total)
  if(total<0):
    total=0

print(maxi)