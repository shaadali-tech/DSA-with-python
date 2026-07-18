nums=[5,10,-3,-1,-10,6]
n=len(nums)
pos=0
neg=1
new_list=[0]*n
for i in range(0,n):
  if nums[i]>0:
    new_list[pos]=nums[i]
    pos+=2
  else:
    new_list[neg]=nums[i]
    neg+=2

print(new_list)