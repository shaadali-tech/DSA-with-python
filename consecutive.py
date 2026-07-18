# nums=[1,99,101,98,2,5,3,100,1,1,4,6,7]
# n=len(nums)
# longest=0
# for i in range(0,n):
#   current=nums[i]
#   count=1
#   while current+1 in nums:
#     current+=1
#     count+=1
#   longest=max(longest,count) 

# print(longest)


nums=[1,99,101,98,2,5,3,100,1,1,4,6,7]
n=len(nums)
longest=0

nums.sort()

count=1
for i in range(1,n):
  if(nums[i]==nums[i-1]):
    continue
  elif(nums[i]==nums[i-1]+1):
    count+=1
  else:
    longest=max(longest,count)
    count=1

longest=max(longest,count)
print(longest)