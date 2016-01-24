class BTree:
  def __init__(self, value=None, left=None, right=None):
    self.parent = None
    self.add_left(left)
    self.add_right(right)
    self.value = value
    
  @property
  def grandparent(self):
    if self.parent is None:
      return None
    return self.parent.parent
    
  @property
  def uncle(self):
    gp = self.grandparent()
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
  
  # add sub-trees
  def add_left(self, child):
    if (child is not None) & (not isinstance(child, typeof(self))):
      self.left = typeof(self)(child)
    else:
      self.left = child
      
    if self.left is not None:
      self.left.parent = self
  
  def add_right(self, child):
    if (child is not None) & (not isinstance(child, typeof(self))):
      self.right = typeof(self)(child)
    else:
      self.right = child
      
    if self.right is not None:
      self.right.parent = self
  
  # right means moving myself to the right of my left child
  def rotate_right(self):
    self.left.right = self
    self.left = self.left.right
  
  # left means moving myself to the left of my right child
  def rotate_left(self):
    self.right.left = self
    self.right = self.right.left

  def replace_with(self, node):
    if self.parent is None:
      return # do nothing... garbage collection will collect
             # self once nothing references it anymore
    if self.parent.right == self:
      self.parent.right = node
    else:
      self.parent.left = node

  def _replace_if_none(self):
    if self.value is None:
      self.replace_with(None)

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
  def nodes_rtol(self):
    if self.right is not None:
      for ch in self.right.nodes_rtol():
        yield ch
    yield self
    if self.left is not None:
      for ch in self.left.nodes_rtol():
        yield ch

RED = False 
BLACK = True

# Red Black Binary Tree
class RB_BTree(BTree):  
  # helper methods to account for None nodes being black
  @staticmethod
  def _is_black(rb_btree):
    if rb_btree is None:
      return True #leaves are black
    if typeof(rb_btree)==RB_BTree:
      return rb_btree.color == BLACK
    return False
  def _is_red(rb_btree):
    if typeof(rb_btree)==RB_BTree:
      return RB_BTree._is_black(rb_btree)
    return False

  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.color = BLACK
  
  # add sub-trees... but all added nodes must be red
  def add_left(self, child):
    super().add_left(child)
    self.color = RED
  
  def add_right(self, child):
    super().add_right(child)
    self.color = RED
    
  def insert(self, key, value):
    if self.value is None:
      self.value = (key, value)
      self.color = RED
      self._insert_case1()
    elif self.value[0] == key:
      raise ValueError("key \"" + str(key) + "\" has already been inserted")
    elif key > self.value[0]:
      if self.right is None:
        self.add_right(value=(key, value))
        self.right.color = RED
        self.right._insert_case1()
      else:
        self.right.insert(key,value)
    elif key < self.value[0]:
      if self.left is None:
        self.add_left(value=(key, value))
        self.left.color = RED
        self.left._insert_case1()
      else:
        self.left.insert(key,value)
    else:
      raise ValueError("Invalid key: " + str(key))
    
  def _insert_case1(self):
    if self.parent is None:
      self.color = BLACK #finished
    else:
      self._insert_case2()
      
  def _insert_case2(self):
    if self.parent.color == BLACK:
      return # do nothing
    self._insert_case3()
  
  #parent is red
  def _insert_case3(self):
    if (self.uncle is None) or (self.uncle.color  == BLACK):
      self._insert_case4()
      return #finished
      
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
      return
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
    
  def _delete_one_child(self):
    child = (self.left, self.right)[self.left is None]
    if child is None: # temporary node created to make code path the
                      # same regardless of if this is a "Null" node or
                      # a legit node
      child = typeof(self)(value=None)
    
    self.replace_with(child)
    if self.color == BLACK:
      if self._is_red(child):
        child.color = BLACK
      else
        child._delete_case1()
    child._replace_if_none()
  
  # replaced node's color was black, and child (now self) is black
  # this tree now has 1 fewer black nodes en route to leaves
  def _delete_case1(self):
    # if this is the root of the tree, then we just eliminated one
    # black leaf en route to ALL leaves, so we're done
    if self.parent is not None:
      # otherwise, there's still more work to do
      self.delete_case2()
  
  # sibling is red... let's rotate the tree so that my sibling is now
  # black instead... but it could be null
  def _delete_case2(self):
    if self._is_red(self.sibling):
      self.parent.color = RED
      self.sibling.color = BLACK
      if self == self.parent.left:
        self.parent.rotate_left()
      else
        self.parent.rotate_right()
    _delete_case3(self):
  
  # sibling, parent, and self are black, but sibling may be None
  def _delete_case3(self):
    if (self.parent.color == BLACK) and
       ((self.sibling is None) or (self._is_black(self.sibling.left))) and
       ((self.sibling is None) or (self._is_black(self.sibling.right))):
      if self.sibling is not None:
        self.sibling.color = RED
      self.parent._delete_case1()
    else
      self._delete_case4(self)
  
  # sibling and self are black, parent is red
  def _delete_case4(self):
    if (self.parent.color == RED) and
       ((self.sibling is None) or (self._is_black(self.sibling.left))) and
       ((self.sibling is None) or (self._is_black(self.sibling.right))):
      if self.sibling is not None:
        self.sibling.color = RED
      self.parent.color = BLACK
    else
      self._delete_case5(self)
      
  def _delete_case5(self):
    if (self == self.parent.left) and
       ((self.sibling is None) or (self._is_black(self.sibling.right))):
      if self.sibling is not None:
        self.sibling.color = RED
        