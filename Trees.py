class BTree:
  def __init__(self, value=None, left=None, right=None):
    self.AddLeft(left)
    self.AddRight(right)
    self.value = value
  
  def AddLeft(self, child):
    if (child is not None) & (not isinstance(child, BTree)):
      self.left = BTree(child)
    else:
      self.left = child
    
  def AddRight(self, child):
    if (child is not None) & (not isinstance(child, BTree)):
      self.right = BTree(child)
    else:
      self.right = child

  # list protocol
  def __len__(self):
    nodes = []
    myLen = 1
    for ch in [self.left, self.right]:
      if ch is None:
        chLen = 0
      else:
        chLen = len(ch)
      myLen += chLen
    return myLen
    
    
  # iterator protocol
  # def __iter__(self):
    # return self
    
  # def next(self):
    