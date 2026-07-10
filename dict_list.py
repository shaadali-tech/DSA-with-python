list1=[1,2,3,4,5,6,3,2,1,1,5]
list2=[1,2,3,4,5,6]

freq={}

for i in range(0,len(list1)):
  freq[list1[i]]=freq.get(list1[i],0)+1

print(freq) 