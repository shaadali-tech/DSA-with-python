def lower_bound(nums,target):
 
  n=len(nums)
  lb=n
  low=0
  high=n-1

  while(low<=high):
    mid=(low+high)//2
    if nums[mid]>=target:
      lb=mid
      high=mid-1
    else:
      low=mid+1

  return lb




nums=[3,4,4,4,8,9,9,10,11,12,12,14,15]
n=len(nums)
print(lower_bound(nums,target=11))