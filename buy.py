# NOW WE ARE GOING TO WRITE A PROGRAM ON BUY AND SELL STOCK

nums=[7,2,1,5,6,4,8]
n=len(nums)
maxi=0
for i in range(0,n-1):
  total=0
  for j in range(i+1,n):
    total=nums[j]-nums[i]
    maxi=max(maxi,total)
print(maxi)