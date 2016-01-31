import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")

import pytest
from SearchTrees import BaseTree
from SearchTrees import AvlTree  

from random import shuffle

def _validate_base(d):
  if d.root is None:
    return
  last = None
  for node in d.root.ltor():
    # assert ordering
    if last is None:
      last = node.value[0]
    else:
      assert last < node.value[0]
      last = node.value[0]
      
    # assert parents make sense
    if node != d.root:
      assert node==node.parent.left or node==node.parent.right
      
def _validate_avl(d):
  if d.root is None:
    return
  last = None
  for node in d.root.ltor():
    # assert ordering
    if last is None:
      last = node.value[0]
    else:
      assert last < node.value[0]
      last = node.value[0]
      
    # assert d is keeping itself balanced
    assert node.balance<=1 and node.balance>=-1
    if node.left is not None:
      lht = node.left.height
    else:
      lht = 0
    if node.right is not None:
      rht = node.right.height
    else:
      rht = 0
    assert lht-rht==node.balance
    
    # assert parents make sense
    if node != d.root:
      assert node==node.parent.left or node==node.parent.right
 
types = [{"ctor": dict, "check": (lambda t: None)},
         {"ctor": BaseTree, "check": _validate_base},
         {"ctor": AvlTree,  "check": _validate_avl }]
sizes = [1,3,10,30,100]
   
@pytest.mark.parametrize("t", types, ids=list(map(lambda t: t["ctor"], types)))
@pytest.mark.parametrize("n", sizes)
def test_insertDeleteInOrderTest(t, n):
  d = t["ctor"]()
  for i in range(n):
    d[str(i)+"k"] = i
    t["check"](d)
    assert len(d) == i+1
  for i in range(n):
    del d[str(i)+"k"]
    t["check"](d)
    assert len(d) == n-(i+1)
  for i in range(n):
    with pytest.raises(KeyError):
      d["k"+str(i)]
   
@pytest.mark.parametrize("t", types, ids=list(map(lambda t: t["ctor"], types)))
@pytest.mark.parametrize("n", sizes)
def test_insertDeleteRevOrderTest(t, n):
  d = t["ctor"]()
  for i in range(n):
    d[str(n-i)+"k"] = i
    t["check"](d)
    assert len(d) == i+1
  for i in range(n):
    del d[str(n-i)+"k"]
    t["check"](d)
    assert len(d) == n-(i+1)
  for i in range(n):
    with pytest.raises(KeyError):
      d["k"+str(n-i)]
   
@pytest.mark.parametrize("t", types, ids=list(map(lambda t: t["ctor"], types)))
@pytest.mark.parametrize("n", sizes)
def test_insertDeleteRandomOrderTest(t, n):
  d = t["ctor"]()
  vals = list(range(n))
  shuffle(vals)
  for i in range(n):
    d[str(vals[i])+"k"] = i
    t["check"](d)
    assert len(d) == i+1
  for i in range(n):
    del d[str(vals[i])+"k"]
    t["check"](d)
    assert len(d) == n-(i+1)
  for i in range(n):
    with pytest.raises(KeyError):
      d["k"+str(vals[i])]

@pytest.mark.parametrize("t", types, ids=list(map(lambda t: t["ctor"], types)))
@pytest.mark.parametrize("n", sizes)
def test_manyInsertsReturnsCorrectValues(t, n):
  d = t["ctor"]()
  for i in range(n):
    d["k"+str(i)] = i
  for i in range(n):
    assert d["k"+str(i)] == i
    
@pytest.mark.parametrize("t", types, ids=list(map(lambda t: t["ctor"], types)))
@pytest.mark.parametrize("n", sizes)
def test_manyInsertsRandomOrderReturnsCorrectValues(t, n):
  d = t["ctor"]()
  vals = list(range(n))
  shuffle(vals)
  for i in range(n):
    d["k"+str(vals[i])] = i
  for i in range(n):
    assert d["k"+str(vals[i])] == i

@pytest.mark.parametrize("t", types, ids=list(map(lambda t: t["ctor"], types)))
@pytest.mark.parametrize("n", sizes)
def test_manyInsertsReturnsCorrectValuesOutOfOrder(t, n):
  d = t["ctor"]()
  for i in range(n):
    d["k"+str(i)] = i
  
  #reverse search
  for i in range(n)[::-1]:
    assert d["k"+str(i)] == i

@pytest.mark.parametrize("t", types, ids=list(map(lambda t: t["ctor"], types)))
@pytest.mark.parametrize("n", sizes)
def test_InsertsAndSomeDeletesReturnsRemainingValues(t, n):
  d = t["ctor"]()
  for i in range(n):
    d["k"+str(i)] = i
  # delete every other
  for i in range(n)[::2]:
    del d["k"+str(i)]
  # make sure deletions are gone
  for i in range(n)[::2]:
    with pytest.raises(KeyError):
      d["k"+str(i)]
  # make sure the rest are still there
  for i in range(n)[1::2]:
    assert d["k"+str(i)] == i
    
@pytest.mark.parametrize("t", types, ids=list(map(lambda t: t["ctor"], types)))
@pytest.mark.parametrize("n", sizes)
def test_InsertsAndSomeDeletesRandomOrderReturnsRemainingValues(t, n):
  d = t["ctor"]()
  vals = list(range(n))
  shuffle(vals)
  for i in range(n):
    d["k"+str(vals[i])] = i
  # delete every other
  for i in range(n)[::2]:
    del d["k"+str(vals[i])]
  # make sure deletions are gone
  for i in range(n)[::2]:
    with pytest.raises(KeyError):
      d["k"+str(vals[i])]
  # make sure the rest are still there
  for i in range(n)[1::2]:
    assert d["k"+str(vals[i])] == i

  