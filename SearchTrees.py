from Trees import BinaryTree

class BaseTree:
  def __init__(self):
    self.root = None
    
  def __len__(self):
    if self.root is None:
      return 0
    return len(self.root)
    
  def __setitem__(self, key, value):
    if self.root is None:
      self.root = BinaryTree(value=(key,value))
      return
      
    node = self.root
    while True:
      if key > node.value[0]:
        if node.right is None:
          node.add_right(BinaryTree(value=(key,value)))
          return
        node = node.right
      elif key < node.value[0]:
        if node.left is None:
          node.add_left(BinaryTree(value=(key,value)))
          return
        node = node.left
      else:
        raise ValueError("Same key inserted twice: " + str(key))
    
  def _srch_node(self, key):
    if self.root == None:
      return None
    node = self.root
    while (node is not None) and (node.value[0] != key):
      if key > node.value[0]:
        node = node.right
      elif key < node.value[0]:
        node = node.left
    return node
    
  def __getitem__(self, key):
    node = self._srch_node(key)
    if (node is None) or (node.value is None):
      raise KeyError(key)
    return node.value[1]
  
  def __delitem__(self, key):
    node = self._srch_node(key)
    if node is None:
      return
      
    while not node.is_leaf():
      if node.left is None:
        nxtNode = next(node.right.ltor())
      else:
        nxtNode = next(node.left.rtol())
      node.swap_val(nxtNode)
      node = nxtNode
      
    if self.root == node:
      self.root = None
    elif node.parent.left == node:
      node.parent.left = None
    else:
      node.parent.right = None
    
class AvlTree:
  def __init__(self):
    self.root = None
    
  def __len__(self):
    if self.root is None:
      return 0
    return len(self.root)
  
  # adj is the change in height node's subtree with the changes
  # that the node tree undergoes in this method
  def _rebal(self, node):
    adj=0
    if node.balance < -1 or node.balance > 1:
      if node.balance == -2:
        if node.right.balance==1:
          if node.right.left.balance==-1:
            node.right.rotate_right()
            node.right.right.balance=0
            node.right.balance=-2
          elif node.right.left.balance==0:
            node.right.rotate_right()
            node.right.right.balance=0
            node.right.balance=-1
          else: #node.right.left.balance==1
            node.right.rotate_right()
            node.right.right.balance=-1
            node.right.balance=-1
          if node.right.balance==-1:
            node.balance=0
          else: #node.right.balance==-2
            node.balance=1
          node.right.balance=0
          adj=-1
          node.rotate_left()
        elif node.right.balance==0:
          node.balance=-1
          node.right.balance=1
          adj=0
          node.rotate_left()
        else: # node.right.balance==-1
          node.balance=0
          node.right.balance=0
          adj=-1
          node.rotate_left()
      else: # node.balance==2
        if node.left.balance==-1:
          if node.left.right.balance==1:
            node.left.rotate_left()
            node.left.left.balance=0
            node.left.balance=2
          elif node.left.right.balance==0:
            node.left.rotate_left()
            node.left.left.balance=0
            node.left.balance=1
          else: #node.left.right.balance==1
            node.left.rotate_left()
            node.left.left.balance=1
            node.left.balance=1
          if node.left.balance==1:
            node.balance=0
          else: #node.left.balance==2
            node.balance=-1
          node.left.balance=0
          adj=-1
          node.rotate_right()
        elif node.left.balance==0:
          node.balance=1
          node.left.balance=-1
          adj=0
          node.rotate_right()
        else: # node.left.balance==1
          node.balance=0
          node.left.balance=0
          adj=-1
          node.rotate_right()
        
      # set root if it was affected
      if self.root == node:
        self.root = node.parent
      # node.parent is now where node used to be
      node = node.parent
    return node, adj
  
  # adj is the change in height that node noticed in
  # its (prior to this call's) alterations
  def _rebal_recurse(self, node, adj):
    # assume node is already at correct balance... but not parent
    # and work our way up the tree
    parent = node.parent
    # if parent is None then return
    if parent is None:
      return
    
    if parent.left == node:
      bal = parent.balance
      parent.balance += adj
      if (adj==1) and (bal==-1):
        adj=0
      elif (adj==-1) and (bal!=1):
        adj=0
    else:
      bal = parent.balance
      parent.balance -= adj
      if (adj==1) and (bal==1):
        adj=0
      elif (adj==-1) and (bal!=-1):
        adj=0
    
    # after adjusting from child's adjustment,
    # fix our balance if something changed
    parent, adj2 = self._rebal(parent)
    
    # call self._rebal(parent, adjustment in parent's height)
    self._rebal_recurse(parent, adj+adj2)
  
  def __setitem__(self, key, value):
    if self.root is None:
      self.root = BinaryTree(value=(key,value))
      self.root.balance=0
      return
      
    node = self.root
    while True:
      if key > node.value[0]:
        if node.right is None:
          ch = BinaryTree(value=(key,value))
          ch.balance=0
          node.add_right(ch)
          node.balance -= 1
          self._rebal_recurse(node, 1 if node.left is None else 0)
          return
        node = node.right
      elif key < node.value[0]:
        if node.left is None:
          ch = BinaryTree(value=(key,value))
          ch.balance=0
          node.add_left(ch)
          node.balance += 1
          self._rebal_recurse(node, 1 if node.right is None else 0)
          return
        node = node.left
      else:
        raise ValueError("Same key inserted twice: " + str(key))
        
  def _srch_node(self, key):
    if self.root == None:
      return None
    node = self.root
    while (node is not None) and (node.value[0] != key):
      if key > node.value[0]:
        node = node.right
      elif key < node.value[0]:
        node = node.left
    return node
    
  def __getitem__(self, key):
    node = self._srch_node(key)
    if (node is None) or (node.value is None):
      raise KeyError(key)
    return node.value[1]
  
  def __delitem__(self, key):
    node = self._srch_node(key)
    if node is None:
      return
      
    while not node.is_leaf():
      if node.left is None:
        nxtNode = next(node.right.ltor())
      else:
        nxtNode = next(node.left.rtol())
      node.swap_val(nxtNode)
      node = nxtNode
      
    if self.root == node:
      self.root = None
      return
    elif node.parent.left == node:
      node.parent.left = None
      node.parent.balance -= 1
      if node.parent.is_leaf():
        adj=-1
      else:
        adj=0
    else:
      node.parent.right = None
      node.parent.balance += 1
      if node.parent.is_leaf():
        adj=-1
      else:
        adj=0
    nodeparent, adj2 = self._rebal(node.parent)
    self._rebal_recurse(nodeparent, adj+adj2)

RED = False 
BLACK = True

# Red Black Binary Tree
class RB_BTree(BinaryTree):
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
    
  def __setitem__(self, key, value):
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
        self.right[key] = value
    elif key < self.value[0]:
      if self.left is None:
        self.add_left((key, value))
        self.left._insert_case1()
      else:
        self.left[key] = value
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
    
  def __getitem__(self, key):
    node = self._srch_node(key)
    if (node is None) or (node.value is None):
      return None
    return node.value[1]
    
  def __delitem__(self, key):
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
  