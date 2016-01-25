class BTree:
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

  # list protocol
  def __len__(self):
    count = 0
    for ch in self.ltor():
      count += 1
    return count
  
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

RED = False 
BLACK = True

# Red Black Binary Tree
class RB_BTree(BTree):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.color = BLACK

  # list protocol
  def __len__(self):
    if self.value is None:
      return 0
    return super().__len__()
  
  # the height of the tree
  @property
  def height(self):
    if self.value is None:
      return 0
    return super().height
  
  # add sub-trees... but all added nodes must be red
  def add_left(self, child):
    super().add_left(child)
    if self.left is not None:
      self.left.color = RED
  
  def add_right(self, child):
    super().add_right(child)
    if self.right is not None:
      self.right.color = RED
    
  def insert(self, key, value):
    if self.value is None:
      self.value = (key, value)
      self._insert_case1()
    elif self.value[0] == key:
      raise ValueError("key \"" + str(key) + "\" has already been inserted")
    elif key > self.value[0]:
      if self.right is None:
        self.add_right((key, value))
        self.right._insert_case1()
      else:
        self.right.insert(key,value)
    elif key < self.value[0]:
      if self.left is None:
        self.add_left((key, value))
        self.left._insert_case1()
      else:
        self.left.insert(key,value)
    else:
      raise ValueError("Invalid key: " + str(key))
    return self.root
    
  def _insert_case1(self):
    if self.parent is None:
      self.color = BLACK
    else:
      self._insert_case2()
      
  def _insert_case2(self):
    if self.parent.color == BLACK:
      return
    self._insert_case3()
  
  #parent is red
  def _insert_case3(self):
    if (self.uncle is None) or (self.uncle.color  == BLACK):
      self._insert_case4()
      return
      
    # uncle and parent are both red
    self.parent.color = BLACK
    self.uncle.color = BLACK
    self.grandparent.color = RED
    self.grandparent._insert_case1()
  
  def _insert_case4(self):
    # parent is red and uncle is black
    # put red child on the "outside" of the tree.. prepping
    # for step 5 where a rotation around the grandparent is performed
    if (self.parent.left == self) and (self.grandparent.right == self.parent):
      self.parent.rotate_right()
      self.right._insert_case5()
    elif (self.parent.right == self) and (self.grandparent.left == self.parent):
      self.parent.rotate_left()
      self.left._insert_case5()
    else:
      # already on the outside
      self._insert_case5()
    
  def _insert_case5(self):
    self.parent.color = BLACK
    self.grandparent.color = RED
    if self == self.parent.left:
      self.grandparent.rotate_right()
    else:
      self.grandparent.rotate_left()
    
  def _srch_node(self, key):
    if (self.value is None) or (self.value[0] == key):
      return self
    elif key > self.value[0]:
      if self.right is not None:
        return self.right._srch_node(key)
    elif key < self.value[0]:
      if self.left is not None:
        return self.left._srch_node(key)
    return None
    
  def search(self, key):
    node = self._srch_node(key)
    if (node is None) or (node.value is None):
      return None
    return node.value[1]
    
  def delete(self, key):
    node = self._srch_node(key)
    if (node is None) or (node.value is None):
      return self
    if (node.left is not None) and (node.right is not None):
      # node is internal node, so get smallest item from right
      # subtree and switch the two nodes.  Then, we delete the
      # node where this node went to, since it now has at most
      # one None child.
      smallestRight = next(node.right.ltor())
      node.value = smallestRight.value
      smallestRight._delete_one_child()
    else:
      node._delete_one_child()
    return self.root
    
  def _delete_one_child(self):
    child = (self.left, self.right)[self.left is None]
    selfcolor = self.color
    sibling = self.sibling
    parent = self.parent
    if parent is not None:
      wasLeft = self == parent.left
    
    ## replace self with child
    if parent is None:
      if child is not None:
        self.value = child.value
        self.left = child.left
        self.right = child.right
        self.color = child.color
      else:
        self.value = None # delete root's value
      return
    if wasLeft:
      parent.left = child
    else:
      parent.right = child
    if child is not None:
      child.parent = parent
    ## end replace self with child
    
    if (selfcolor == RED) or (parent is None):
      return
    if (child is not None) and (child.color==RED):
      child.color = BLACK
      return
    if (parent.color == BLACK) and (sibling.color == BLACK):
      if sibling.right is not None:
        sibling.right.color = BLACK
      if sibling.left is not None:
        sibling.left.color = BLACK
      if wasLeft:
        parent.rotate_left()
      else:
        parent.rotate_right()
      parent.color = RED
    elif (parent.color == BLACK) and (sibling.color == RED):
      sibling.color = BLACK
      if wasLeft:
        sibling.left.color = RED
        parent.rotate_left()
      else:
        sibling.right.color = RED
        parent.rotate_right()
    else: # (parent.color == RED) and (sibling.color == BLACK)
      parent.color = BLACK
      sibling.color = RED

from math import log
def _assert_black_height(t1, t2):
  if t1 is None:
    h1 = 1
  else:
    h1 = (0,1)[t1.color==BLACK] + _assert_black_height(t1.left, t1.right)
    
  if t2 is None:
    h2 = 1
  else:
    h2 = (0,1)[t2.color==BLACK] + _assert_black_height(t2.left, t2.right)
  assert h1 == h2
  return h1
    
def validate_RB_BTree(t):
  if not isinstance(t, RB_BTree):
    raise ValueError("input must be an RB_BTree")
    
  # assert max height of the tree
  assert t.height <= 2*log(len(t)+1,2)
  
  # assert black heights
  _assert_black_height(t.left, t.right)
  
  # red node test
  for n in t.ltor():
    if n.color == RED:
      assert (n.left is None) or (n.left.color == BLACK)
      assert (n.right is None) or (n.right.color == BLACK)
    
class RevBTree:
  def __init__(self, btree):
    if not isinstance(btree, BTree):
      raise ValueError("btree must be a derived type of BTree")
    self.BTree = btree
  
  @property
  def left(self):
    return RevBTree(self._btree.right)
  
  @property
  def right(self):
    return RevBTree(self._btree.left)
    
  @property
  def BTree(self):
    return self.BTree