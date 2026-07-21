# nums=[11,15,20,1,4,5,6,8,9,10]

# target=8
# n=len(nums)
# low=0
# high=n-1

# while(low<=high):
#   mid=(low+high)//2
#   if nums[mid]==target:
#     print(mid)
  
#   if nums[mid]<=nums[high]:

#     if nums[mid]<=target<=nums[high]:
#       low=mid+1
#     else:
#       high=mid-1
    
#   else:
#     if nums[mid]>=target>=nums[low]:
#       high=mid-1
#     else:
#       low=mid+1



# SEARCH IN ROTATED ARRAY WITH DUPLICATES


# nums=[7,7,7,7,7,7,7,1,2,3,4,5,7,7]
# n=len(nums)
# low=0
# high=n-1
# target=1
# while(low<=high):
#   mid=(low+high)//2
#   if(nums[mid]==target):
#     print(mid)
#   if(nums[mid]==nums[low]==nums[high]):
#     low+=1
#     high-=1
#     continue
#   if(nums[mid]<=nums[high]):
#     if(nums[mid]<=target<=nums[high]):
#       low=mid+1
#     else:
#       high=mid-1
#   else:
#     if(nums[mid]>=target>=nums[low]):
#       high=mid-1
#     else:
#       low=mid+1



# MINIMUM IN ROTATED SORTED ARRAY

nums=[7,8,0,1,2,3,4]
n=len(nums)
low=0
high=n-1
mini=float("inf")
while(low<=high):
  mid=(low+high)//2
  if(nums[mid]<=nums[high]):
    mini=min(mini,nums[mid])
    high=mid-1
  else:
    mini=min(mini,nums[low])
    low=mid+1


print(mini)

















  