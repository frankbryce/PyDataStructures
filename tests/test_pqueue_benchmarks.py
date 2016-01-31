import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")

import pytest
from PQueues import Heap

from random import shuffle

@pytest.mark.parametrize('n', [5,10,25,50])
def test_enqueueDequeuePriority(n):
  heap = Heap()
  expectedOrder = list(range(n))
  shuffle(expectedOrder)
  for i in range(n):
    heap.enqueue(i, n-expectedOrder.index(i))
  for i in expectedOrder:
    heap.dequeue()==i
 
@pytest.mark.parametrize('n', [5,10,25,50])
def test_enqueuePriority(n):
  heap = Heap()
  idxs = list(range(n))
  shuffle(idxs)
  for i in range(n):
    heap.enqueue(i, idxs[i])