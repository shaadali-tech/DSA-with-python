# pie=3.14
# redius=float(input("|Enter the Radius Of Circle : "))

# area=(pie*redius*redius)
# hello="hi shaad"
# print(f'{hello} area of circle is : {area}')


# for i in range(1,100,20):
#   print("Hello Shaad")

name='ShaadAli'
print(name[::-1])


my_dict={
  'name':"shaad",
  'rollno':"215/ICS/043",
}

print(my_dict['name'])

for i in my_dict:
  print(i)


x=[1,2,3,4,5]

listcom=[i**2 for i in x if i%2==0]
print(listcom)

numbers = [1, 2, 3, 4, 5]
squared = [n**2 for n in numbers]
# Output: [1, 4, 9, 16, 25]   