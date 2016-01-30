import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")

import pytest
from Trees import BaseTree

def test_insertThenSearchReturnsValue():
  tree = BaseTree()
  tree.insert("k5", 5)
  assert tree.search("k5") == 5

def test_insertThenDeleteThenSearchReturnsNone():
  tree = BaseTree()
  tree.insert("k5", 5)
  tree.delete("k5")
  assert tree.search("k5") == None

def test_insert3TimesThenDelete3TimesThenSearchReturnsNone():
  tree = BaseTree()
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
      last = node.value.key
    else:
      assert last < node.value.key
      last = node.value.key
      
    # assert parents make sense
    if node != tree.root:
      assert node==node.parent.left or node==node.parent.right
  
def inOrderTest(n):
  tree = BaseTree()
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
  tree = BaseTree()
  for i in range(1, 11):
    tree.insert("k"+str(i), i)
  for i in range(1, 11):
    assert tree.search("k"+str(i)) == i

def test_manyInsertsReturnsCorrectValuesOutOfOrder():
  tree = BaseTree()
  for i in range(1, 11):
    tree.insert("k"+str(i), i)
  
  #reverse search
  for i in range(1, 11)[::-1]:
    assert tree.search("k"+str(i)) == i

def test_manyInsertsAndSomeDeletesReturnsRemainingValues():
  tree = BaseTree()
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
  tree = BaseTree()
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
  tree = BaseTree()
  for i in range(0,n):
    tree.insert(i,i)

def degenerateCase_insertDescendingOrder(n):
  tree = BaseTree()
  for i in range(0,n):
    tree.insert(n-i,n-i)

def degenerateCase_insertOutInOrder(n):
  tree = BaseTree()
  for i in range(0,n):
    idx = (i%2)*n + (1-2*(i%2))*i
    tree.insert(idx,idx)

def degenerateCase_insertAscendingOrder(n):
  tree = BaseTree()
  for i in range(0,n):
    tree.insert(i,i)
    
def test_degenerateCaseAscOrder(benchmark):
  benchmark(degenerateCase_insertAscendingOrder, n=1000)
  
def test_degenerateCaseDescOrder(benchmark):
  benchmark(degenerateCase_insertDescendingOrder, n=1000)
  
def test_degenerateCaseOutInOrder(benchmark):
  benchmark(degenerateCase_insertDescendingOrder, n=1000)
  