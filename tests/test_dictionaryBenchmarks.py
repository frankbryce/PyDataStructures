import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")

import pytest
from SearchTrees import AvlTree
from SearchTrees import BaseTree

import random

from pdb import set_trace

def benchmark_this(test):
  def wrapper(benchmark, t, n):
    benchmark(test, None, t, n)
  return wrapper

types = [BaseTree, AvlTree, dict]
sizes = [100,300,1000]

@pytest.mark.parametrize('t', types)
@pytest.mark.parametrize('n', sizes)
@benchmark_this
def test_insertRandomOrder(benchmark, t, n):
  random.seed(0x1C2C6D66)
  d = t()
  for i in range(n):
    d[random.randint(0, 0x7FFFFFFF)] = i

@pytest.mark.parametrize('t', types)
@pytest.mark.parametrize('n', sizes)
@benchmark_this
def test_insertDescendingOrder(benchmark, t, n):
  d = t()
  for i in range(n):
    d[n-i] = i

@pytest.mark.parametrize('t', types)
@pytest.mark.parametrize('n', sizes)
@benchmark_this
def test_insertOutInOrder(benchmark, t, n):
  d = t()
  for i in range(n):
    idx = (i%2)*n + (1-2*(i%2))*i
    d[idx] = i

@pytest.mark.parametrize('t', types)
@pytest.mark.parametrize('n', sizes)
@benchmark_this
def test_insertAscendingOrder(benchmark, t, n):
  d = t()
  for i in range(n):
    d[i] = i

@pytest.mark.parametrize('t', types)
@pytest.mark.parametrize('n', sizes)
@benchmark_this
def test_insertDeleteRandomOrder(benchmark, t, n):
  random.seed(0x1C2C6D66)
  d = t()
  vals=[]
  for i in range(n):
    vals.append(random.randint(0,0x7FFFFFFF))
  for i in range(n):
    d[vals[i]] = i
  for i in range(n):
    del d[vals[i]]

@pytest.mark.parametrize('t', types)
@pytest.mark.parametrize('n', sizes)
@benchmark_this
def test_insertDeleteDescendingOrder(benchmark, t, n):
  d = t()
  for i in range(n):
    d[n-i] = i
  for i in range(n):
    del d[n-i]

@pytest.mark.parametrize('t', types)
@pytest.mark.parametrize('n', sizes)
@benchmark_this
def test_insertDeleteOutInOrder(benchmark, t, n):
  d = t()
  vals = []
  for i in range(n):
    vals.append((i%2)*n + (1-2*(i%2))*i)
  for i in range(n):
    d[vals[i]] = i
  for i in range(n):
    del d[vals[i]]

@pytest.mark.parametrize('t', types)
@pytest.mark.parametrize('n', sizes)
@benchmark_this
def test_insertDeleteAscendingOrder(benchmark, t, n):
  d = t()
  for i in range(n):
    d[i] = i
  for i in range(n):
    del d[i]