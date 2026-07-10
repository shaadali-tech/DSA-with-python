nums=[1,2,3,4,5,6,7,2,5,3,2,2]
nums2=[1,1,2,3,4,5,2,2,3]
freq={}
freq2={}
for i in range(len(nums)):
  if nums[i] in freq:
    freq[nums[i]]+=1
  else:
    freq[nums[i]]=1

print(freq)

for i in range(len(nums2)):
  freq2[nums2[i]]=freq2.get(nums2[i],0)+1

print(freq2)