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