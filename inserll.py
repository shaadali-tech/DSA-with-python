class Node:
  def __init__(self,data=None,next=None):
    self.next=next
    self.data=data

n1=Node(data=10,next=n2)
n2=Node(data=20,next=n3)
n3=Node(data=20)



Temp=n1

while (Temp):
    print(Temp.data)
    Temp=Temp.next