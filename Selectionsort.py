def selectionsort(arr):

  n=len(arr)

  for i in range (n):
    min=i
    for j in range(i,n):
      if arr[min]>arr[j]:
        min=j
    arr[i],arr[min]=arr[min],arr[i]

arr=[5,6,3,1,6,6,10]
selectionsort(arr)
print(arr)