class BTree:
  def __init__(self, value=None, left=None, right=None):
    self.add_left(left)
    self.add_right(right)
    self.value = value
  
  def add_left(self, child):
    if (child is not None) & (not isinstance(child, BTree)):
      self.left = BTree(child)
    else:
      self.left = child
    
  def add_right(self, child):
    if (child is not None) & (not isinstance(child, BTree)):
      self.right = BTree(child)
    else:
      self.right = child

  # list protocol
  def __len__(self):
    count = 0
    for ch in self.nodes_ltor():
      count += 1
    return count
  
  @property
  def height(self):
    mxChHt = 0
    if self.left is not None:
      mxChHt = self.left.height
    if self.right is not None:
      mxChHt = max(mxChHt, self.right.height)
    return 1 + mxChHt
    
  # node generator left->right
  def nodes_ltor(self):
    if self.left is not None:
      for ch in self.left.nodes_ltor():
        yield ch
    yield self
    if self.right is not None:
      for ch in self.right.nodes_ltor():
        yield ch
    
  # node generator right->left
  def nodes_rtol(self):
    if self.right is not None:
      for ch in self.right.nodes_rtol():
        yield ch
    yield self
    if self.left is not None:
      for ch in self.left.nodes_rtol():
        yield ch

# Red Black Binary Tree
class RB_BTree(BTree):
  def __init__(self):
    super().__init__()
    