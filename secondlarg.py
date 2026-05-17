array=[1,3,2,5,4,6,7,832,23,45,67,89,90
       ]

largest=array[0]
for i in array:
    if i>largest:
        largest=i
print(largest)

second=array[-1]

for i in array:
    if i>second and i!=largest:
        second=i


  
print(second)