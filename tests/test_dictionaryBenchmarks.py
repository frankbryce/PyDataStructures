import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")

import pytest
from SearchTrees import AvlTree
from SearchTrees import BaseTree

import random

class TestBenchInsert:
  def insertRandomOrder(t, n):
    random.seed(0x1C2C6D66)
    d = t()
    for i in range(0,n):
      d[random.randint(0, 0x7FFFFFFF)] = i

  def insertDescendingOrder(t, n):
    d = t()
    for i in range(0,n):
      d[n-i] = i

  def insertOutInOrder(t, n):
    d = t()
    for i in range(0,n):
      idx = (i%2)*n + (1-2*(i%2))*i
      d[idx] = i

  def insertAscendingOrder(t, n):
    d = t()
    for i in range(0,n):
      d[i] = i

  types = [BaseTree, AvlTree, dict]
  sizes = [100,300,1000]
  cases = [insertAscendingOrder, insertDescendingOrder, insertOutInOrder, insertRandomOrder]

  @pytest.mark.parametrize('t', types)
  @pytest.mark.parametrize('n', sizes)
  @pytest.mark.parametrize('case', cases, ids=list(map(lambda f: f.__name__, cases)))
  @pytest.mark.benchmark(group="insert-cases")
  def test_benchmark(self, benchmark, case, t, n):
    benchmark(case, t, n)

class TestBenchInsertDelete:
  def insertDeleteRandomOrder(t, n):
    random.seed(0x1C2C6D66)
    d = t()
    vals=[]
    for i in range(0,n):
      vals.append(random.randint(0,0x7FFFFFFF))
    for i in range(0,n):
      d[vals[i]] = i
    for i in range(0,n):
      del d[vals[i]]

  def insertDeleteDescendingOrder(t, n):
    d = t()
    for i in range(0,n):
      d[n-i] = i
    for i in range(0,n):
      del d[n-i]

  def insertDeleteOutInOrder(t, n):
    d = t()
    vals = []
    for i in range(0,n):
      vals.append((i%2)*n + (1-2*(i%2))*i)
    for i in range(0,n):
      d[vals[i]] = i
    for i in range(0,n):
      del d[vals[i]]

  def insertDeleteAscendingOrder(t, n):
    d = t()
    for i in range(0,n):
      d[i] = i
    for i in range(0,n):
      del d[i]

  types = [BaseTree, AvlTree, dict]
  sizes = [100,300,1000]
  cases = [insertDeleteAscendingOrder, insertDeleteDescendingOrder, insertDeleteOutInOrder, insertDeleteRandomOrder]

  @pytest.mark.parametrize('t', types)
  @pytest.mark.parametrize('n', sizes)
  @pytest.mark.parametrize('case', cases, ids=list(map(lambda f: f.__name__, cases)))
  @pytest.mark.benchmark(group="insertDelete-cases")
  def test_benchmark(self, benchmark, case, t, n):
    benchmark(case, t, n)