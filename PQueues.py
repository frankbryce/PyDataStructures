

class LList:
  def __init__(self):
    self.items = []
  
  def enqueue(self, item, priority=0):
    pass
  
  def peek(self):
    pass
  
  def dequeue(self):
    pass
    
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
    while idx!=0 and self.items[self.pidx(idx)][1]<self.items[idx][1]:
      t = self.items[self.pidx(idx)]
      self.items[self.pidx(idx)] = self.items[idx]
      self.items[idx] = t
  
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
    return item
    