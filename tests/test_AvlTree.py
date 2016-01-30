import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")

import pytest
from Trees import AvlTree

def test_insertThenSearchReturnsValue():
  tree = AvlTree()
  tree.insert("k5", 5)
  assert tree.search("k5") == 5

def test_insertThenDeleteThenSearchReturnsNone():
  tree = AvlTree()
  tree.insert("k5", 5)
  tree.delete("k5")
  assert tree.search("k5") == None

def test_insert3TimesThenDelete3TimesThenSearchReturnsNone():
  tree = AvlTree()
  tree.insert("k7", 7)
  tree.insert("k6", 6)
  tree.insert("k5", 5)
  tree.delete("k6")
  tree.delete("k5")
  tree.delete("k7")
  assert tree.search("k5") == None
  assert tree.search("k6") == None
  assert tree.search("k7") == None
  
def _validate(tree):
  if tree.root is None:
    return
  last = None
  for node in tree.root.ltor():
    # assert ordering
    if last is None:
      last = node.value[0]
    else:
      assert last < node.value[0]
      last = node.value[0]
      
    # assert tree is keeping itself balanced
    assert node.balance<=1 and node.balance>=-1
    if node.left is not None:
      lht = node.left.height
    else:
      lht = 0
    if node.right is not None:
      rht = node.right.height
    else:
      rht = 0
    assert lht-rht<=1 or rht-lht<=1
    
    # assert parents make sense
    if node != tree.root:
      assert node==node.parent.left or node==node.parent.right
  
def inOrderTest(n):
  tree = AvlTree()
  for i in range(0,n):
    tree.insert("k"+str(i),i)
    _validate(tree)
    assert len(tree) == i+1
  for i in range(0,n):
    tree.delete("k"+str(i))
    _validate(tree)
    assert len(tree) == n-(i+1)
  for i in range(0,n):
    assert tree.search("k"+str(i)) == None
  
def test_insert3TimesThenDelete3TimesInOrderThenSearchReturnsNone():
  inOrderTest(3)

def test_insert5TimesThenDelete5TimesInOrderThenSearchReturnsNone():
  inOrderTest(5)

def test_insert7TimesThenDelete7TimesInOrderThenSearchReturnsNone():
  inOrderTest(7)

def test_insert9TimesThenDelete9TimesInOrderThenSearchReturnsNone():
  inOrderTest(9)

def test_insert11TimesThenDelete11TimesInOrderThenSearchReturnsNone():
  inOrderTest(11)

def test_manyInsertsReturnsCorrectValues():
  tree = AvlTree()
  for i in range(1, 11):
    tree.insert("k"+str(i), i)
  for i in range(1, 11):
    assert tree.search("k"+str(i)) == i

def test_manyInsertsReturnsCorrectValuesOutOfOrder():
  tree = AvlTree()
  for i in range(1, 11):
    tree.insert("k"+str(i), i)
  
  #reverse search
  for i in range(1, 11)[::-1]:
    assert tree.search("k"+str(i)) == i

def test_manyInsertsAndSomeDeletesReturnsRemainingValues():
  tree = AvlTree()
  for i in range(1, 11):
    tree.insert("k"+str(i), i)
    
  # delete every other
  for i in range(1, 11)[::2]:
    tree.delete("k"+str(i))
    
  # make sure deletions are gone
  for i in range(1, 11)[::2]:
    assert tree.search("k"+str(i)) == None
    
  # make sure the rest are still there
  for i in range(1, 11)[1::2]:
    assert tree.search("k"+str(i)) == i

def test_manyInsertsAndSomeDeletesReturnsRemainingValuesLargeData():
  tree = AvlTree()
  for i in range(1, 101):
    tree.insert("k"+str(i), i)
    _validate(tree)
    
  # delete every other
  for i in range(1, 101)[::2]:
    tree.delete("k"+str(i))
    _validate(tree)
    
  # make sure deletions are gone
  for i in range(1, 101)[::2]:
    assert tree.search("k"+str(i)) == None
    
  # make sure the rest are still there
  for i in range(1, 101)[1::2]:
    assert tree.search("k"+str(i)) == i

def degenerateCase_insertAscendingOrder(n):
  tree = AvlTree()
  for i in range(0,n):
    tree.insert(i,i)
  