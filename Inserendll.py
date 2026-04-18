class Node:

  def __init__(self,data,next=None):
    self.data=data
    self.next=next


 
class Singleylinkedlist:

  def __init__(self,head=None):
    self.head=head

  def insert_at_end(self,value):
    temp=Node(value)
    if(self.head!=None):
      t1=self.head
      while(t1.next!=None):
        t1=t1.next
      t1.next=temp
    else:
      self.head=temp

  def insertatbeg(self,value):
    temp=Node(value)
    temp.next=self.head
    self.head=temp

  def printll(self):
      t1=self.head
      while(t1.next!=None):
        print(t1.data)
        t1=t1.next



obj=Singleylinkedlist()
obj.insert_at_end(10)
obj.insert_at_end(20)
obj.insert_at_end(30)
obj.insertatbeg(5)
obj.printll()