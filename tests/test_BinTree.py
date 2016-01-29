import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")

import pytest
from Trees import BinTree

def test_NotNone():
  tree = BinTree()
  assert tree is not None

def test_SettingValueInInitIsStoredInTree():
  tree = BinTree(value=5)
  assert tree.value == 5

def test_SettingLeftTreeSetsValue():
  tree = BinTree(left=BinTree())
  assert tree.left is not None

def test_SettingRightTreeSetsValue():
  tree = BinTree(right=BinTree())
  assert tree.right is not None

def test_SettingLeftTreeToBTreeDoesNotFails():
  tree = BinTree(left=15)
  assert tree.left.value == 15

def test_SettingRightTreeToBTreeDoesNotFails():
  tree = BinTree(right="BinTree")
  assert tree.right.value is "BinTree"

def test_SettingLeftTreeToNoneDoesNotRaise():
  tree = BinTree(left=None)
  assert tree is not None

def test_SettingRightTreeToNoneDoesNotRaise():
  tree = BinTree(right=None)
  assert tree is not None
  
def test_BlankTreeHasLen1():
  tree = BinTree()
  assert len(tree)==1
  
def test_TreeWithLeftChildHasLen2():
  tree = BinTree(left=BinTree())
  assert len(tree)==2
  
def test_TreeWithRightChildHasLen2():
  tree = BinTree(right=BinTree())
  assert len(tree)==2
  
def test_TreeRotationWithTwoElements():
  tree = BinTree(right=BinTree())
  tree2 = tree.rotate_left()
  assert len(tree2)==2
  
def test_addChildWorks():
  tree = BinTree()
  ltree = BinTree(left=BinTree(), right=BinTree(left=BinTree()))
  rtree = BinTree(left=BinTree(left=BinTree()), right=BinTree(left=BinTree(),right=BinTree()))
  
  tree_len = len(tree)
  ltree_len = len(ltree)
  rtree_len = len(rtree)
  assert len(tree)==1
  assert len(ltree)==4
  assert len(rtree)==6
  tree.add_left(ltree)
  assert len(tree)==tree_len + ltree_len
  tree.add_right(rtree)
  assert len(tree)==tree_len + ltree_len + rtree_len
  
  
def test_TreeWithRightChildHasLen2():
  tree = BinTree(right=BinTree())
  assert len(tree)==2
  
def test_CompoundTreeHasCorrectLength():
  tree = BinTree(
    left=BinTree(
      left=BinTree(),
      right=BinTree(
        left=BinTree(),
        right=BinTree(
          right=BinTree()
        )
      )
    ),
    right=BinTree(
      left=BinTree(),
      right=BinTree(
        right=BinTree()
      )
    )
  )
  assert len(tree)==11
  
def test_CompoundTreeHasCorrectHeight():
  tree = BinTree(
    left=BinTree(
      left=BinTree(),
      right=BinTree(
        left=BinTree(),
        right=BinTree(
          right=BinTree()
        )
      )
    ),
    right=BinTree(
      left=BinTree(),
      right=BinTree(
        right=BinTree()
      )
    )
  )
  assert tree.height==5
  
def test_LeftRotationWorksWith2Nodes():
  root = BinTree()
  right = BinTree()
  root.add_right(right)
  newRoot = root.rotate_left()
  assert newRoot == right
  assert newRoot.left == root
  assert newRoot.parent == None
  assert newRoot.right == None
  assert root.parent == newRoot
  assert root.left == None
  assert root.right == None
  
def test_RightRotationWorksWith2Nodes():
  root = BinTree()
  left = BinTree()
  root.add_left(left)
  newRoot = root.rotate_right()
  assert newRoot == left
  assert newRoot.right == root
  assert newRoot.parent == None
  assert newRoot.left == None
  assert root.parent == newRoot
  assert root.left == None
  assert root.right == None
  
def test_LeftRotationWorksWith3Nodes():
  root = BinTree()
  left = BinTree()
  right = BinTree()
  root.add_left(left)
  root.add_right(right)
  newRoot = root.rotate_left()
  assert newRoot == right
  assert newRoot.left == root
  assert newRoot.parent == None
  assert newRoot.right == None
  assert root.parent == newRoot
  assert root.left == left
  assert root.right == None
  assert left.parent == root
  assert left.left == None
  assert left.right == None
  
def test_RightRotationWorksWith3Nodes():
  root = BinTree()
  left = BinTree()
  right = BinTree()
  root.add_left(left)
  root.add_right(right)
  newRoot = root.rotate_right()
  assert newRoot == left
  assert newRoot.right == root
  assert newRoot.parent == None
  assert newRoot.left == None
  assert root.parent == newRoot
  assert root.left == None
  assert root.right == right
  assert right.parent == root
  assert right.left == None
  assert right.right == None
  
def test_LeftRotationWorksWith4Nodes():
  root = BinTree()
  left = BinTree()
  right = BinTree()
  rightleft = BinTree()
  root.add_left(left)
  root.add_right(right)
  right.add_left(rightleft)
  newRoot = root.rotate_left()
  assert newRoot == right
  assert newRoot.left == root
  assert newRoot.parent == None
  assert newRoot.right == None
  assert root.parent == newRoot
  assert root.left == left
  assert root.right == rightleft
  assert left.parent == root
  assert left.left == None
  assert left.right == None
  assert rightleft.parent == root
  assert rightleft.left == None
  assert rightleft.right == None
  
def test_RightRotationWorksWith4Nodes():
  root = BinTree()
  left = BinTree()
  right = BinTree()
  leftright = BinTree()
  root.add_left(left)
  root.add_right(right)
  left.add_right(leftright)
  newRoot = root.rotate_right()
  assert newRoot == left
  assert newRoot.left == None
  assert newRoot.parent == None
  assert newRoot.right == root
  assert root.parent == newRoot
  assert root.left == leftright
  assert root.right == right
  assert right.parent == root
  assert right.left == None
  assert right.right == None
  assert leftright.parent == root
  assert leftright.left == None
  assert leftright.right == None
  
def test_swap3nodesrightright():
  tree = BinTree(value=1,right=BinTree(value=2,right=BinTree(value=3)))
  tree.swap(tree.right)
  tree = tree.root
  tree.right.swap(tree.right.right)
  assert tree.right.value == 3
  assert tree.right.parent.value == 2
  assert tree.right.right.value == 1
  assert tree.right.right.parent.value == 3
  assert tree.left is None
  
def test_swap3nodesleaves():
  tree = BinTree(value=2,left=BinTree(value=1),right=BinTree(value=3))
  tree.left.swap(tree.right)
  assert tree.right.value == 1
  assert tree.left.value == 3
  assert tree.right.parent.value == 2
  assert tree.left.parent.value == 2
  
def test_swap3nodesrootandright():
  tree = BinTree(value=2,left=BinTree(value=1),right=BinTree(value=3))
  tree.swap(tree.right)
  tree = tree.root
  assert tree.right.value == 2
  assert tree.left.value == 1
  assert tree.right.parent.value == 3
  assert tree.left.parent.value == 3
  
def test_swap3nodesrootandleft():
  tree = BinTree(value=2,left=BinTree(value=1),right=BinTree(value=3))
  tree.swap(tree.left)
  tree = tree.root
  assert tree.right.value == 3
  assert tree.left.value == 2
  assert tree.right.parent.value == 1
  assert tree.left.parent.value == 1
  
def test_swap11nodes():
  tree = BinTree(value=6,
    left=BinTree(value=3,
      left=BinTree(value=7, left=BinTree(value=1)),
      right=BinTree(value=4, right=BinTree(value=5))
    ),
    right=BinTree(value=9,
      left=BinTree(value=2, right=BinTree(value=8)),
      right=BinTree(value=11, left=BinTree(value=10))
    )
  )
  
  tree.left.left.swap(tree.right.left)
  i=1
  for n in tree.ltor():
    assert n.value == i
    assert n.root == tree
    i += 1
    
  tree.right.left.swap(tree.left.left)
  tree.right.right.swap(tree.left.left)
  tree.right.right.swap(tree.right.left)
  tree.right.right.swap(tree.left.left)
  i=1
  for n in tree.ltor():
    assert n.value == i
    assert n.root == tree
    i += 1
    
  tree.right.left.swap(tree.left.left)
  tree.left.right.right.swap(tree.left.left)
  tree.left.right.right.swap(tree.right.left)
  tree.left.right.right.swap(tree.left.left)
  i=1
  for n in tree.ltor():
    assert n.value == i
    assert n.root == tree
    i += 1
    
  tree.right.left.swap(tree.left.left)
  tree.right.right.left.swap(tree.left.left)
  tree.right.right.left.swap(tree.right.left)
  tree.right.right.left.swap(tree.left.left)
  i=1
  for n in tree.ltor():
    assert n.value == i
    assert n.root == tree
    i += 1
    
  tree.right.left.swap(tree.left.left)
  tree.right.left.right.swap(tree.left.left)
  tree.right.left.right.swap(tree.right.left)
  tree.right.left.right.swap(tree.left.left)
  i=1
  for n in tree.ltor():
    assert n.value == i
    assert n.root == tree
    i += 1