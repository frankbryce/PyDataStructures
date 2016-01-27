import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")

import pytest
from Trees import BTree
from Trees import RevBTree

def test_RevBTree_len():
  rTree = RevBTree(BTree())
  assert len(rTree.Tree)==1
  
def test_iterInReverse():
  tree = BTree(1,left=BTree(2,left=BTree(3),right=BTree(4)),right=BTree(5,left=BTree(6),right=BTree(7)))
  rtree = RevBTree(tree)
  
  list1 = list(tree.ltor())
  list2 = list(rtree.rtol())
  assert len(list1)==len(list2)
  for i in range(0,len(list1)):
    assert list1[i].value==list2[i].value