def lower_Bound(nums,target):
  n=len(nums)
  low=0
  high=n-1
  lb=-1
  while(low<=high):
    mid=(low+high)//2
    if(nums[mid]>=target):
      lb=mid
      high=mid-1
    else:
      low=mid+1 

  return lb
  
  
def Upper_bound(nums,target):
  n=len(nums)
  low=0
  high=n-1
  Ub=-1
  while(low<=high):
    mid=(low+high)//2
    if(nums[mid]>target):
      Ub=mid
      high=mid-1
    else:
      low=mid+1 

  return Ub-1


nums=[1,2,3,3,3,3,3,5,6,8,9,9,10]
print(lower_Bound(nums,target=3))
print(Upper_bound(nums,target=3))
