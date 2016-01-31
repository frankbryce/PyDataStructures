import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")

import pytest
from Trees import BinaryTree
from Trees import RevBTree

def test_RevBTree_len():
  rTree = RevBTree(BinaryTree())
  assert len(rTree.Tree)==1
  
def test_iterInReverse():
  tree = BinaryTree(1,left=BinaryTree(2,left=BinaryTree(3),right=BinaryTree(4)),right=BinaryTree(5,left=BinaryTree(6),right=BinaryTree(7)))
  rtree = RevBTree(tree)
  
  list1 = list(tree.ltor())
  list2 = list(rtree.rtol())
  assert len(list1)==len(list2)
  for i in range(0,len(list1)):
    assert list1[i].value==list2[i].value