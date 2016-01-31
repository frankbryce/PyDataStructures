class ListPQueue:
  class Node:
    def __init__(self, value, priority):
      self.item = {"value": value, "priority": priority}
      next = None
    @property
    def priority(self):
      return self.item["priority"]
    @property
    def value(self):
      return self.item["value"]

  def __init__(self):
    self.head = None
  
  def enqueue(self, value, priority=0):
    node = self.Node(value, priority)
    node.next = self.head
    self.head = node
    last = None
    while node.next is not None and \
          node.next.priority >= node.priority:
      nxt = node.next
      node.next = nxt.next
      nxt.next = node
      if last is not None:
        last.next = nxt
      if node==self.head:
        self.head = nxt
      last = nxt
  
  def peek(self):
    return self.head.value
  
  def dequeue(self):
    if self.head is None:
      return None
    val = self.head.value
    self.head = self.head.next
    return val
    
  def __str__(self):
    node = self.head
    s = ""
    while node is not None:
      s += "("+str(node.value)+","+str(node.priority)+")"
      node = node.next
    return s
    
class Heap:
  def __init__(self):
    self.items = []
  
  def pidx(self, idx):
    if idx%2==0:
      return int((idx-2)/2)
    return int((idx-1)/2)
  def lidx(self, idx):
    return int(2*idx+1)
  def ridx(self, idx):
    return int(2*idx+2)
  
  def enqueue(self, item, priority=0):
    if not isinstance(priority, int):
      raise ValueError("enter an integer for the priority")
    if priority < 0:
      raise ValueError("priority must be >= 0")
      
    self.items.append((item, priority))
    idx = len(self.items)-1
    while idx>0 and self.items[self.pidx(idx)][1]<self.items[idx][1]:
      t = self.items[self.pidx(idx)]
      self.items[self.pidx(idx)] = self.items[idx]
      self.items[idx] = t
      idx = self.pidx(idx)
  
  def peek(self):
    return self.items[0][0]
  
  def dequeue(self):
    item = self.items[0][0]
    self.items = [self.items[-1]] + self.items[1:-1]
    idx = 0
    while self.lidx(idx)<len(self.items):
      nIdx = self.lidx(idx)
      if self.ridx(idx)<len(self.items):
        ri = self.ridx(idx)
        rp = self.items[ri][1]
        if rp>=self.items[nIdx][1]: nIdx = ri
      if self.items[idx][1] < self.items[nIdx][1]:
        t = self.items[idx]
        self.items[idx] = self.items[nIdx]
        self.items[nIdx] = t
      else:
        break
      idx = nIdx
    return item
    