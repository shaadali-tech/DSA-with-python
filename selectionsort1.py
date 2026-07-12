# arr=[1,4,2,7,8,3,6,7]

# n=len(arr)
# for i in range(0,n):
#   min_index=i
#   for j in range(i+1,n):
#     if arr[j]<arr[min_index]:
#       min_index=j
#   arr[i], arr[min_index] = arr[min_index], arr[i]

# print(arr)


list=[3,2,5,6,1,7,8]

n=len(list)

for i in range(0,n):
  min_index=i
  for j in range(i+1,n):
    if list[j]<list[min_index]:
      min_index=j
  list[i],list[min_index]=list[min_index],list[i]

print(list)

