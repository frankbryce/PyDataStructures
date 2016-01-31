class BinaryTree:
  def __init__(self, value=None, left=None, right=None):
    self.parent = None
    self.add_left(left)
    self.add_right(right)
    self.value = value
    
  @property
  def root(self):
    if self.parent is None:
      return self
    return self.parent.root
  
  @property
  def grandparent(self):
    if self.parent is None:
      return None
    return self.parent.parent
    
  @property
  def uncle(self):
    gp = self.grandparent
    if gp is None:
      return None
    if self.parent == gp.left:
      return gp.right
    return gp.left
    
  @property
  def sibling(self):
    if self.parent is None:
      return None
    if self.parent.left == self:
      return self.parent.right
    return self.parent.left
    
  def is_leaf(self):
    return (self.left is None) and (self.right is None)
  
  # add sub-trees
  def add_left(self, child):
    if (child is not None) & (not isinstance(child, type(self))):
      self.left = type(self)(value=child)
    else:
      self.left = child
    if self.left is not None:
      self.left.parent = self
  
  def add_right(self, child):
    if (child is not None) & (not isinstance(child, type(self))):
      self.right = type(self)(value=child)
    else:
      self.right = child
    if self.right is not None:
      self.right.parent = self
  
  # node is BinaryTree, prop is "left" or "right"
  def _swap_prop(self, node, prop):
    if getattr(self, prop) == node:
      setattr(self, prop, getattr(node, prop))
      setattr(node, prop, self)
    elif getattr(node, prop) == self:
      setattr(node, prop, getattr(self, prop))
      setattr(self, prop, node)
    else:
      np = getattr(node, prop)
      setattr(node, prop, getattr(self, prop))
      setattr(self, prop, np)
    if getattr(self,prop) is not None:
      getattr(self,prop).parent = self
    if getattr(node,prop) is not None:
      getattr(node,prop).parent = node
  
  def swap_node(self, node):
    if node is None:
      raise ValueError("node to swap with cannot be None")
    
    #swap parent pointers
    np,sp = True,True
    lf,rt = True,True
    if self.parent == node:
      node.parent, self.parent = self, node.parent
      if node.left == self:
        node.left, self.left, lf = self.left, node, False
        if node.left is not None: node.left.parent = self
      else:
        node.right, self.right, rt = self.right, node, False
        if node.right is not None: node.right.parent = self
      np=False # don't have to set node.parent child pointer
    elif node.parent == self:
      self.parent, node.parent = node, self.parent
      if self.left == node:
        self.left, node.left, lf = node.left, self, False
        if self.left is not None: self.left.parent = self
      else:
        self.right, node.right, rt = node.right, self, False
        if self.right is not None: self.right.parent = self
      sp=False # don't have to set self.parent child pointer
    elif node.parent == self.parent:
      if node.parent.left == node:
        node.parent.left = self
        node.parent.right = node
      else:
        node.parent.left = node
        node.parent.right = self
      np,sp=False,False # don't have to set either parent child pointer
    else:
      node.parent, self.parent = self.parent, node.parent
      
    if sp:
      if self.parent is not None:
        if self.parent.left == node:
          self.parent.left = self
        else:
          self.parent.right = self
    if np:
      if node.parent is not None:
        if node.parent.left == self:
          node.parent.left = node
        else:
          node.parent.right = node
    
    #swap left & right pointers
    if lf:
      self._swap_prop(node, "left")
    if rt:
      self._swap_prop(node, "right")
      
  def swap_val(self, node):
    v = self.value
    self.value = node.value
    node.value = v
    
  def swap(self,node):
    self.swap_val(node)
  
  # right means moving myself to the right of my left child
  def rotate_right(self):
    s = self
    sl = self.left
    sr = self.right
    sp = self.parent
    if self.left is not None:
      slr = self.left.right
    else:
      slr = None
      
    if slr is not None:
      slr.parent = s
    if sl is not None:
      sl.right = s
      sl.parent = sp
    if sp is not None:
      if sp.left == s:
        sp.left = sl
      else:
        sp.right = sl
    s.parent = sl
    s.left = slr
    return sl
  
  # left means moving myself to the left of my right child
  def rotate_left(self):
    s = self
    sl = self.left
    sr = self.right
    sp = self.parent
    if self.right is not None:
      srl = self.right.left
    else:
      srl = None
      
    if srl is not None:
      srl.parent = s
    if sr is not None:
      sr.left = s
      sr.parent = sp
    if sp is not None:
      if sp.left == s:
        sp.left = sr
      else:
        sp.right = sr
    s.parent = sr
    s.right = srl
    return sr
  
  # the height of the tree
  @property
  def height(self):
    mxChHt = 0
    if self.left is not None:
      mxChHt = self.left.height
    if self.right is not None:
      mxChHt = max(mxChHt, self.right.height)
    return 1 + mxChHt
    
  # node generator left->right
  def ltor(self):
    if self.left is not None:
      for ch in self.left.ltor():
        yield ch
    yield self
    if self.right is not None:
      for ch in self.right.ltor():
        yield ch
    
  # node generator right->left
  def rtol(self):
    if self.right is not None:
      for ch in self.right.rtol():
        yield ch
    yield self
    if self.left is not None:
      for ch in self.left.rtol():
        yield ch
        
  # list protocol
  def __len__(self):
    count = 0
    for ch in self.ltor():
      count += 1
    return count
    
  def __cmp__(self, node):
    return self.value.__cmp__(node.value)
        
  def __str__(self, depth=0):
    ret = ""

    # Print right branch
    if self.right != None:
      ret += self.right.__str__(depth + 1)

    # Print own value
    ret += "\n" + ("    "*depth) + str(self.value)

    # Print left branch
    if self.left != None:
      ret += self.left.__str__(depth + 1)

    return ret
  
# experiment that may or may not be useful  
class RevBTree(BinaryTree):
  def __init__(self, btree):
    self._tree = btree
    if (not isinstance(btree, BinaryTree)) and (btree is not None):
      raise ValueError("btree must be a derived type of BinaryTree")
    super().__init__()
  
  @property
  def left(self):
    if self.Tree.right is None:
      return None
    return RevBTree(self.Tree.right)
    
  @left.setter
  def left(self, value):
    self.Tree.right = value
  
  @property
  def right(self):
    if self.Tree.left is None:
      return None
    return RevBTree(self.Tree.left)
    
  @right.setter
  def right(self, value):
    self.Tree.left = value
  
  @property
  def parent(self):
    if self.Tree.parent is None:
      return None
    return RevBTree(self.Tree.parent)
    
  @right.setter
  def parent(self, value):
    self.Tree.parent = value
  
  @property
  def value(self):
    return self.Tree.value
    
  @value.setter
  def value(self, value):
    self.Tree.value = value
  
  @property
  def Tree(self):
    return self._tree
