import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")

import pytest
from Trees import AvlTree
from Trees import BaseTree

def degenerateCase_insertDescendingOrder(t, n):
  tree = t()
  for i in range(0,n):
    tree.insert(n-i,n-i)

def degenerateCase_insertOutInOrder(t, n):
  tree = t()
  for i in range(0,n):
    idx = (i%2)*n + (1-2*(i%2))*i
    tree.insert(idx,idx)

def degenerateCase_insertAscendingOrder(t, n):
  tree = t()
  for i in range(0,n):
    tree.insert(i,i)
    
def test_bas_degenerateCaseAscOrder(benchmark):
  benchmark(degenerateCase_insertAscendingOrder, t=BaseTree, n=1000)
  
def test_bas_degenerateCaseDescOrder(benchmark):
  benchmark(degenerateCase_insertDescendingOrder, t=BaseTree, n=1000)
  
def test_bas_degenerateCaseOutInOrder(benchmark):
  benchmark(degenerateCase_insertDescendingOrder, t=BaseTree, n=1000)
    
def test_avl_degenerateCaseAscOrder(benchmark):
  benchmark(degenerateCase_insertAscendingOrder, t=AvlTree, n=1000)
  
def test_avl_degenerateCaseDescOrder(benchmark):
  benchmark(degenerateCase_insertDescendingOrder, t=AvlTree, n=1000)
  
def test_avl_degenerateCaseOutInOrder(benchmark):
  benchmark(degenerateCase_insertDescendingOrder, t=AvlTree, n=1000)