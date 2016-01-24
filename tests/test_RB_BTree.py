import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")

import pytest
from Trees import RB_BTree

def test_insertThenSearchReturnsValue():
  tree = RB_BTree()
  tree.insert("k5", 5)
  assert tree.search("k5") == 5

def test_insertThenDeleteThenSearchReturnsNone():
  tree = RB_BTree()
  tree.insert("k5", 5)
  tree.delete("k5")
  assert tree.search("k5") == None

def test_manyInsertsReturnsCorrectValues():
  tree = RB_BTree()
  for i in range(1, 11):
    tree.insert("k"+str(i), i)
  for i in range(1, 11):
    assert tree.search("k"+str(i)) == i

def test_manyInsertsReturnsCorrectValuesOutOfOrder():
  tree = RB_BTree()
  for i in range(1, 11):
    tree.insert("k"+str(i), i)
  
  #reverse search
  for i in range(1, 11)[::-1]:
    assert tree.search("k"+str(i)) == i

def test_manyInsertsAndSomeDeletesReturnsRemainingValues():
  tree = RB_BTree()
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
  tree = RB_BTree()
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
    
def test_lworSimpleCases():
  tree = RB_BTree()
  assert tree.left is None
  assert tree.left == tree.lwor
  tree = RB_BTree(left=RB_BTree())
  assert tree.left == tree.lwor
  tree = RB_BTree(left=RB_BTree(left=RB_BTree(left=RB_BTree(), right=RB_BTree())))
  assert tree.left == tree.lwor
    
def test_lworLessSimpleCase():
  tree = RB_BTree(
    left=RB_BTree(
      left=RB_BTree(),
      right=RB_BTree(
        left=RB_BTree(),
        right=RB_BTree(
          right=RB_BTree()
        )
      )
    ),
    right=RB_BTree(
      left=RB_BTree(),
      right=RB_BTree(
        right=RB_BTree()
      )
    )
  )
  assert len(tree.left) == len(tree.lwor)
  ltor1 = list(tree.left.ltor())
  ltor2 = list(tree.lwor.ltor())
  for i in range(0,len(ltor1)):
    assert ltor1[i] == ltor2[i]
