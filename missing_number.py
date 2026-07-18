# Missing number in an array

arr=[0,1,3,4]
n=4

sum=n*(n+1)/2

original_sum=0
for i in range(0,len(arr)):
    original_sum+=arr[i]

missing=sum-original_sum
print(missing)