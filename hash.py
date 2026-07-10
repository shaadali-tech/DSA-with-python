num=[1,2,3,1,2,4,5,6,7]
m=[1,2,3,4,5,6,7]

# for i in m:
#   count=0
#   for x in num:
#     if i==x:
#       count+=1
#   print(f"count of element {i} in {x} is {count}")

hashlist=[0]*11
print(hashlist)

for i in num:
  hashlist[i]+=1

print(hashlist)

for x in m:
  print(hashlist[x])