import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")

import pytest
from SearchTrees import AvlTree
from SearchTrees import BaseTree

import random

# always the same for repeatability
random.seed(0x1C2C6D66)

def insertDeleteRandomOrder(t, n):
  tree = t()
  vals=[]
  for i in range(0,n):
    vals.append(random.randint(0,0x7FFFFFFF))
  for i in range(0,n):
    tree[vals[i]] = i
  for i in range(0,n):
    del tree[vals[i]]

def insertDeleteDescendingOrder(t, n):
  tree = t()
  for i in range(0,n):
    tree[n-i] = i
  for i in range(0,n):
    del tree[n-i]

def insertDeleteOutInOrder(t, n):
  tree = t()
  vals = []
  for i in range(0,n):
    vals.append((i%2)*n + (1-2*(i%2))*i)
  for i in range(0,n):
    tree[vals[i]] = i
  for i in range(0,n):
    del tree[vals[i]]

def insertDeleteAscendingOrder(t, n):
  tree = t()
  for i in range(0,n):
    tree[i] = i
  for i in range(0,n):
    del tree[i]

types = [BaseTree, AvlTree]
sizes = [100,300,1000]
cases = [insertDeleteAscendingOrder, insertDeleteDescendingOrder, insertDeleteOutInOrder, insertDeleteRandomOrder]

@pytest.mark.parametrize('t', types)
@pytest.mark.parametrize('n', sizes)
@pytest.mark.parametrize('case', cases, ids=list(map(lambda f: f.__name__, cases)))
@pytest.mark.benchmark(group="insertDelete-cases")
def test_benchmark(benchmark, case, t, n):
  benchmark(case, t, n)
