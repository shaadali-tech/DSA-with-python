nums=[3,4,4,4,8,9,9,10,12,12,14,15]
n=len(nums)
low=0
high=n-1
target=11
ceil=0
floor=0
while(low<=high):
  mid=(low+high)//2
  if (nums[mid]<=target):
      floor=nums[mid]
      low=mid+1
  else:
     high=mid-1
     


print(floor)