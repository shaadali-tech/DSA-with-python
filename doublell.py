class Node:
  def __init__(self,data=None):
    self.data=data
    self.prev=None
    self.next=None

class doubleyll:
   def __init__(self):
    self.head=None

   def insrtatend(self,data):
    temp=Node(data)
    if (self.head==None):
        self.head=temp
        return
    t=self.head
    while(t.next!=None):
      t=t.next
    t.next=temp
    temp.prev=t

   def printll(self):
      t1=self.head
      while(t1.next!=None):
        print(t1.data)
        t1=t1.next


obj=doubleyll()
obj.insrtatend(10)
obj.insrtatend(20)
obj.insrtatend(30)
obj.insrtatend(40)
obj.printll()