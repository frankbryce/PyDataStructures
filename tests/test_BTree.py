import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")

import pytest
from Trees import BTree

def test_NotNone():
  tree = BTree()
  assert tree is not None

def test_SettingValueInInitIsStoredInTree():
  tree = BTree(value=5)
  assert tree.value == 5

def test_SettingLeftTreeSetsValue():
  tree = BTree(left=BTree())
  assert tree.left is not None

def test_SettingRightTreeSetsValue():
  tree = BTree(right=BTree())
  assert tree.right is not None

def test_SettingLeftTreeToBTreeDoesNotFails():
  tree = BTree(left=15)
  assert tree.left.value == 15

def test_SettingRightTreeToBTreeDoesNotFails():
  tree = BTree(right="BTree")
  assert tree.right.value is "BTree"

def test_SettingLeftTreeToNoneDoesNotRaise():
  tree = BTree(left=None)
  assert tree is not None

def test_SettingRightTreeToNoneDoesNotRaise():
  tree = BTree(right=None)
  assert tree is not None
  
def test_BlankTreeHasLen1():
  tree = BTree()
  assert len(tree)==1
  
def test_TreeWithLeftChildHasLen2():
  tree = BTree(left=BTree())
  assert len(tree)==2
  
def test_TreeWithRightChildHasLen2():
  tree = BTree(right=BTree())
  assert len(tree)==2
  
def test_TreeRotationWithTwoElements():
  tree = BTree(right=BTree())
  tree2 = tree.rotate_left()
  assert len(tree2)==2
  
def test_addChildWorks():
  tree = BTree()
  ltree = BTree(left=BTree(), right=BTree(left=BTree()))
  rtree = BTree(left=BTree(left=BTree()), right=BTree(left=BTree(),right=BTree()))
  
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
  tree = BTree(right=BTree())
  assert len(tree)==2
  
def test_CompoundTreeHasCorrectLength():
  tree = BTree(
    left=BTree(
      left=BTree(),
      right=BTree(
        left=BTree(),
        right=BTree(
          right=BTree()
        )
      )
    ),
    right=BTree(
      left=BTree(),
      right=BTree(
        right=BTree()
      )
    )
  )
  assert len(tree)==11
  
def test_CompoundTreeHasCorrectHeight():
  tree = BTree(
    left=BTree(
      left=BTree(),
      right=BTree(
        left=BTree(),
        right=BTree(
          right=BTree()
        )
      )
    ),
    right=BTree(
      left=BTree(),
      right=BTree(
        right=BTree()
      )
    )
  )
  assert tree.height==5
  
def test_LeftRotationWorksWith2Nodes():
  root = BTree()
  right = BTree()
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
  root = BTree()
  left = BTree()
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
  root = BTree()
  left = BTree()
  right = BTree()
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
  root = BTree()
  left = BTree()
  right = BTree()
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
  root = BTree()
  left = BTree()
  right = BTree()
  rightleft = BTree()
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
  root = BTree()
  left = BTree()
  right = BTree()
  leftright = BTree()
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
  
