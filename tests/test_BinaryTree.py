import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")

import pytest
from Trees import BinaryTree

def test_NotNone():
  tree = BinaryTree()
  assert tree is not None

def test_SettingValueInInitIsStoredInTree():
  tree = BinaryTree(value=5)
  assert tree.value == 5

def test_SettingLeftTreeSetsValue():
  tree = BinaryTree(left=BinaryTree())
  assert tree.left is not None

def test_SettingRightTreeSetsValue():
  tree = BinaryTree(right=BinaryTree())
  assert tree.right is not None

def test_SettingLeftTreeToBTreeDoesNotFails():
  tree = BinaryTree(left=15)
  assert tree.left.value == 15

def test_SettingRightTreeToBTreeDoesNotFails():
  tree = BinaryTree(right="BinaryTree")
  assert tree.right.value is "BinaryTree"

def test_SettingLeftTreeToNoneDoesNotRaise():
  tree = BinaryTree(left=None)
  assert tree is not None

def test_SettingRightTreeToNoneDoesNotRaise():
  tree = BinaryTree(right=None)
  assert tree is not None
  
def test_BlankTreeHasLen1():
  tree = BinaryTree()
  assert len(tree)==1
  
def test_TreeWithLeftChildHasLen2():
  tree = BinaryTree(left=BinaryTree())
  assert len(tree)==2
  
def test_TreeWithRightChildHasLen2():
  tree = BinaryTree(right=BinaryTree())
  assert len(tree)==2
  
def test_TreeRotationWithTwoElements():
  tree = BinaryTree(right=BinaryTree())
  tree2 = tree.rotate_left()
  assert len(tree2)==2
  
def test_addChildWorks():
  tree = BinaryTree()
  ltree = BinaryTree(left=BinaryTree(), right=BinaryTree(left=BinaryTree()))
  rtree = BinaryTree(left=BinaryTree(left=BinaryTree()), right=BinaryTree(left=BinaryTree(),right=BinaryTree()))
  
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
  tree = BinaryTree(right=BinaryTree())
  assert len(tree)==2
  
def test_CompoundTreeHasCorrectLength():
  tree = BinaryTree(
    left=BinaryTree(
      left=BinaryTree(),
      right=BinaryTree(
        left=BinaryTree(),
        right=BinaryTree(
          right=BinaryTree()
        )
      )
    ),
    right=BinaryTree(
      left=BinaryTree(),
      right=BinaryTree(
        right=BinaryTree()
      )
    )
  )
  assert len(tree)==11
  
def test_CompoundTreeHasCorrectHeight():
  tree = BinaryTree(
    left=BinaryTree(
      left=BinaryTree(),
      right=BinaryTree(
        left=BinaryTree(),
        right=BinaryTree(
          right=BinaryTree()
        )
      )
    ),
    right=BinaryTree(
      left=BinaryTree(),
      right=BinaryTree(
        right=BinaryTree()
      )
    )
  )
  assert tree.height==5
  
def test_LeftRotationWorksWith2Nodes():
  root = BinaryTree()
  right = BinaryTree()
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
  root = BinaryTree()
  left = BinaryTree()
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
  root = BinaryTree()
  left = BinaryTree()
  right = BinaryTree()
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
  root = BinaryTree()
  left = BinaryTree()
  right = BinaryTree()
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
  root = BinaryTree()
  left = BinaryTree()
  right = BinaryTree()
  rightleft = BinaryTree()
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
  root = BinaryTree()
  left = BinaryTree()
  right = BinaryTree()
  leftright = BinaryTree()
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
  tree = BinaryTree(value=1,right=BinaryTree(value=2,right=BinaryTree(value=3)))
  tree.swap(tree.right)
  tree = tree.root
  tree.right.swap(tree.right.right)
  assert tree.right.value == 3
  assert tree.right.parent.value == 2
  assert tree.right.right.value == 1
  assert tree.right.right.parent.value == 3
  assert tree.left is None
  
def test_swap3nodesleaves():
  tree = BinaryTree(value=2,left=BinaryTree(value=1),right=BinaryTree(value=3))
  tree.left.swap(tree.right)
  assert tree.right.value == 1
  assert tree.left.value == 3
  assert tree.right.parent.value == 2
  assert tree.left.parent.value == 2
  
def test_swap3nodesrootandright():
  tree = BinaryTree(value=2,left=BinaryTree(value=1),right=BinaryTree(value=3))
  tree.swap(tree.right)
  tree = tree.root
  assert tree.right.value == 2
  assert tree.left.value == 1
  assert tree.right.parent.value == 3
  assert tree.left.parent.value == 3
  
def test_swap3nodesrootandleft():
  tree = BinaryTree(value=2,left=BinaryTree(value=1),right=BinaryTree(value=3))
  tree.swap(tree.left)
  tree = tree.root
  assert tree.right.value == 3
  assert tree.left.value == 2
  assert tree.right.parent.value == 1
  assert tree.left.parent.value == 1
  
def test_swap11nodes():
  tree = BinaryTree(value=6,
    left=BinaryTree(value=3,
      left=BinaryTree(value=7, left=BinaryTree(value=1)),
      right=BinaryTree(value=4, right=BinaryTree(value=5))
    ),
    right=BinaryTree(value=9,
      left=BinaryTree(value=2, right=BinaryTree(value=8)),
      right=BinaryTree(value=11, left=BinaryTree(value=10))
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