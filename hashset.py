nums=[1,99,101,98,2,5,3,100,1,1]
n=len(nums)
longest=0
hash_set=set()
for i in range(0,n):
  hash_set.add(nums[i])

print(hash_set)

for num in hash_set:
  if num-1 not in hash_set:
    current=num
    count=1
    while current+1 in hash_set:
      count+=1
      current+=1
    longest=max(longest,count)

print(longest)