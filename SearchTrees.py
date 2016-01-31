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
        node.value = (key,value)
        return
    
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
        node.value = (key,value)
        return
        
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
  