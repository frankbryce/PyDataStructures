import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")

import pytest
from Trees import BinTree
from Trees import RevBTree

def test_RevBTree_len():
  rTree = RevBTree(BinTree())
  assert len(rTree.Tree)==1
  
def test_iterInReverse():
  tree = BinTree(1,left=BinTree(2,left=BinTree(3),right=BinTree(4)),right=BinTree(5,left=BinTree(6),right=BinTree(7)))
  rtree = RevBTree(tree)
  
  list1 = list(tree.ltor())
  list2 = list(rtree.rtol())
  assert len(list1)==len(list2)
  for i in range(0,len(list1)):
    assert list1[i].value==list2[i].value