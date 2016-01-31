import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")

import pytest
from PQueues import Heap
from PQueues import ListPQueue

from random import seed, shuffle
 
def _validate_llist(pq):
  node = pq.head
  last_priority = None
  while node is not None:
    if last_priority is not None:
      assert node.priority <= last_priority
    last_priority = node.priority
    node = node.next

def _validate_heap(pq):
  for i in range(len(pq.items)):
    if pq.lidx(i)<len(pq.items):
      assert pq.items[pq.lidx(i)][1] <= pq.items[i][1]
    if pq.ridx(i)<len(pq.items):
      assert pq.items[pq.ridx(i)][1] <= pq.items[i][1]

types = [{"ctor": ListPQueue, "check": _validate_llist },
         {"ctor": Heap,  "check": _validate_heap }]
sizes = [1,3,10,30,100]

@pytest.mark.parametrize("t", types, ids=list(map(lambda t: t["ctor"], types)))
def test_enqueueDequeue(t):
  pq = t["ctor"]()
  pq.enqueue(1)
  assert pq.dequeue()==1

@pytest.mark.parametrize("t", types, ids=list(map(lambda t: t["ctor"], types)))
def test_enqueue2Dequeue2(t):
  pq = t["ctor"]()
  pq.enqueue(1)
  pq.enqueue(2)
  assert pq.dequeue()==1
  assert pq.dequeue()==2

@pytest.mark.parametrize("t", types, ids=list(map(lambda t: t["ctor"], types)))
def test_enqueue2Dequeue2Priority(t):
  pq = t["ctor"]()
  pq.enqueue(1)
  pq.enqueue(2,1)
  assert pq.dequeue()==2
  assert pq.dequeue()==1
 
@pytest.mark.parametrize("t", types, ids=list(map(lambda t: t["ctor"], types)))
@pytest.mark.parametrize('n', sizes)
def test_enqueueDequeuePriority(t, n):
  seed(0x1C2C6D66)
  pq = t["ctor"]()
  expectedOrder = list(range(n))
  shuffle(expectedOrder)
  for i in range(n):
    pq.enqueue(i, n-expectedOrder.index(i))
    t["check"](pq)
  for i in expectedOrder:
    assert pq.peek()==i
    assert pq.dequeue()==i
    t["check"](pq)

@pytest.mark.parametrize("t", types, ids=list(map(lambda t: t["ctor"], types)))
@pytest.mark.parametrize('n', sizes)
def test_enqueuePriority(t, n):
  seed(0x1C2C6D66)
  pq = t["ctor"]()
  idxs = list(range(n))
  shuffle(idxs)
  for i in range(n):
    pq.enqueue(i, idxs[i])
    t["check"](pq)