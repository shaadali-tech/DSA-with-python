n=int(input("enter ean integer :"))

armstrong=0
num=n
nod=len(str(n))
while(n>0):
  digit=n%10
  armstrong=armstrong+digit**nod
  n=n//10
print(armstrong)
if(num==armstrong):
  print("armstrong")