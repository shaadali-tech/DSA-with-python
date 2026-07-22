# TODAY WE ARE STARTING LINKED LIST 21/JULY/2026

class Node:
  def __init__(self,value,next=None):
    self.value=value
    self.next=next

class Linkedlist:
  def __init__(self,head=None):
    self.head=head
  
  def insert_at_end(self,value):
    temp=Node(value)
    if self.head!=None:
      t=self.head
      while(t.next!=None):
        t=t.next
      t.next=temp
    else:
      self.head=temp

  def traversal(self):
    if not self.head:
      print("LL IS EMPTY")
    curr=self.head
    while(curr is not None):
        print(curr.value,end=" ")
        curr=curr.next
    print()

  def insert_at(self,value,position):
    New_Node=Node(value)
    if position==0:
      New_Node.next=self.head
      self.head=New_Node
    else:
      current=self.head
      count=0
      prev_node=None
      while(current is not None and count<position):
        prev_node=current
        current=current.next
        count+=1
      prev_node.next=New_Node
      New_Node.next=current
  def delete(self,value):
    temp=self.head
    if temp.next is not None:
      if temp.value==value:
        self.head=temp.next
        return
      else:
        prev=None
        found=False
        while(temp is not None):
          if temp.value==value:
            found=True
            break
          prev=temp
          temp=temp.next

        if found:
          prev.next=temp.next
          return
        else:
          print("Node not Found")


Sll=Linkedlist()

Sll.traversal()
Sll.insert_at_end(5)
Sll.insert_at_end(10)
Sll.insert_at_end(15)
Sll.insert_at(6,2)
Sll.delete(6)
Sll.traversal()


      