import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")

import pytest
from PQueues import Heap

import random
from random import shuffle

def enqueueDequeuePriority(n):
  random.seed(0x1C2C6D66)
  heap = Heap()
  idxs = list(range(n))
  shuffle(idxs)
  for i in range(n):
    heap.enqueue(i, idxs[1])
  for i in range(n):
    heap.dequeue()
 
def enqueuePriority(n):
  random.seed(0x1C2C6D66)
  heap = Heap()
  idxs = list(range(n))
  shuffle(idxs)
  for i in range(n):
    heap.enqueue(i, idxs[i])
    
@pytest.mark.parametrize('n', [5,10,25,50])
def test_enqueueDequeuePriority(benchmark, n):
  benchmark(enqueueDequeuePriority,n)
 
@pytest.mark.parametrize('n', [5,10,25,50])
def test_enqueuePriority(benchmark, n):
  benchmark(enqueuePriority,n)