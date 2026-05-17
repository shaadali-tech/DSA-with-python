class CircularQueue:
  def __init__(self,size):
    self.size = size
    self.queue = [None] * size
    self.front = -1
    self.rear = -1

  def insert(self,value):
    if((self.rear+1)%self.size == self.front):
      print("Queue is Full\n")
    elif(self.front == -1):
      self.front = 0
      self.rear = 0
      self.queue[self.rear] = value
    else:
      self.rear = (self.rear+1)%self.size
      self.queue[self.rear] = value

  def delete(self):
    if(self.front == -1):
      print("Queue is Empty\n")
    elif(self.front == self.rear):
      self.front = -1
      self.rear = -1
    else:
      self.front = (self.front+1)%self.size


cq=CircularQueue(5)
cq.insert(14)
cq.insert(22)
cq.insert(13)
cq.insert(-6)
cq.insert(9)
cq.insert(20)