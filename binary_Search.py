def Binary_Search(nums,target):
  n=len(nums)
 
  left=0
  right=n-1

  while(left<=right):
    mid=(left+right)//2
    if(nums[mid]==target):
      return mid
    elif(nums[mid]<target):
      left=mid+1
    else:
      right=mid-1
    

  return -1

nums=[2,4,6,7,9,11,18,19]
target=456

print(Binary_Search(nums,target))