import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")

import pytest
from PQueues import Heap

from random import shuffle

def test_enqueueDequeue():
  heap = Heap()
  heap.enqueue(1)
  assert heap.dequeue()==1

def test_enqueue2Dequeue2():
  heap = Heap()
  heap.enqueue(1)
  heap.enqueue(2)
  assert heap.dequeue()==1
  assert heap.dequeue()==2

def test_enqueue2Dequeue2Priority():
  heap = Heap()
  heap.enqueue(1)
  heap.enqueue(2,1)
  assert heap.dequeue()==2
  assert heap.dequeue()==1
 
def _validate(pq):
  for i in range(len(pq.items)):
    if pq.lidx(i)<len(pq.items):
      assert pq.items[pq.lidx(i)][1] <= pq.items[i][1]
    if pq.ridx(i)<len(pq.items):
      assert pq.items[pq.ridx(i)][1] <= pq.items[i][1]
 
@pytest.mark.parametrize('n', [5,10,25,50])
def test_enqueueDequeuePriority(n):
  heap = Heap()
  expectedOrder = list(range(n))
  shuffle(expectedOrder)
  for i in range(n):
    heap.enqueue(i, n-expectedOrder.index(i))
    _validate(heap)
  for i in expectedOrder:
    assert heap.peek()==i
    assert heap.dequeue()==i
    _validate(heap)
 
@pytest.mark.parametrize('n', [5,10,25,50])
def test_enqueuePriority(n):
  heap = Heap()
  idxs = list(range(n))
  shuffle(idxs)
  for i in range(n):
    heap.enqueue(i, idxs[i])
    _validate(heap)