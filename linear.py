nums=[1,2,3,4,5,6,7,8,245,100]

user=int(input("Enter the element you want to search :"))

for i in range(len(nums)):
  if (nums[i]==user):
    print(f"Number is presnt at index {i}")
    break
