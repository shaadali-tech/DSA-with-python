nums=[1,0,-1,0,-2,2,5,9]
n=len(nums)
target=0
my_set=set()
for i in range(0,n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      for l in range(k+1,n):
        total=nums[i]+nums[j]+nums[k]+nums[l]
        if(total==target):
            temp=[nums[i],nums[j],nums[k],nums[l]]
            temp.sort()
            my_set.add(tuple(temp))

result=[]
for ans in my_set:
  result.append(list(ans))

print(result)