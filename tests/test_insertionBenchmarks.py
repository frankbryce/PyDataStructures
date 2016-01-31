import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")

import pytest
from SearchTrees import AvlTree
from SearchTrees import BaseTree

import random

# always the same for repeatability
random.seed(0x1C2C6D66)

def insertRandomOrder(t, n):
  tree = t()
  for i in range(0,n):
    tree[random.randint(0, 0x7FFFFFFF)] = i

def insertDescendingOrder(t, n):
  tree = t()
  for i in range(0,n):
    tree[n-i] = i

def insertOutInOrder(t, n):
  tree = t()
  for i in range(0,n):
    idx = (i%2)*n + (1-2*(i%2))*i
    tree[idx] = i

def insertAscendingOrder(t, n):
  tree = t()
  for i in range(0,n):
    tree[i] = i

types = [BaseTree, AvlTree]
sizes = [100,300,1000]
cases = [insertAscendingOrder, insertDescendingOrder, insertOutInOrder, insertRandomOrder]

@pytest.mark.parametrize('t', types)
@pytest.mark.parametrize('n', sizes)
@pytest.mark.parametrize('case', cases, ids=list(map(lambda f: f.__name__, cases)))
@pytest.mark.benchmark(group="insert-cases")
def test_benchmark(benchmark, case, t, n):
  benchmark(case, t, n)

