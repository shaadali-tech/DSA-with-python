arr=[1,3,2,4,6,7]
target=5
n=len(arr)


def twosum(arr):
  for i in range(n):
    for j in range(i+1,n):
      if arr[i]+arr[j]==target:
        return i,j
       
print(twosum(arr))