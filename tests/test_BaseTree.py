import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")

import pytest
from Trees import BaseTree
from Trees import validate_RB_BTree as validate

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

def inOrderTest(n):
  tree = BaseTree()
  for i in range(0,n):
    tree.insert("k"+str(i),i)
    assert len(tree) == i+1
    validate(tree)
  for i in range(0,n):
    tree.delete("k"+str(i))
    assert len(tree) == n-(i+1)
    validate(tree)
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
  for i in range(1, 1001):
    tree.insert("k"+str(i), i)
    
  # delete every other
  for i in range(1, 1001)[::2]:
    tree.delete("k"+str(i))
    
  # make sure deletions are gone
  for i in range(1, 1001)[::2]:
    assert tree.search("k"+str(i)) == None
    
  # make sure the rest are still there
  for i in range(1, 1001)[1::2]:
    assert tree.search("k"+str(i)) == i
