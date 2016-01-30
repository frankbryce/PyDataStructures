import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")

import pytest
from Trees import AvlTree
from Trees import BaseTree

import random

# always the same for repeatability
random.seed(0x1C2C6D66)

def insertRandomOrder(t, n):
  tree = t()
  for i in range(0,n):
    tree.insert(random.randint(0,0x7FFFFFFF),i)

def insertDescendingOrder(t, n):
  tree = t()
  for i in range(0,n):
    tree.insert(n-i,n-i)

def insertOutInOrder(t, n):
  tree = t()
  for i in range(0,n):
    idx = (i%2)*n + (1-2*(i%2))*i
    tree.insert(idx,idx)

def insertAscendingOrder(t, n):
  tree = t()
  for i in range(0,n):
    tree.insert(i,i)

def test_bas_AscOrder2500(benchmark):
  benchmark(insertAscendingOrder, t=BaseTree, n=2500)
def test_bas_DescOrder2500(benchmark):
  benchmark(insertDescendingOrder, t=BaseTree, n=2500)
def test_bas_OutInOrder2500(benchmark):
  benchmark(insertOutInOrder, t=BaseTree, n=2500)
def test_bas_RandomOrder2500(benchmark):
  benchmark(insertRandomOrder, t=BaseTree, n=2500)
def test_bas_AscOrder1000(benchmark):
  benchmark(insertAscendingOrder, t=BaseTree, n=1000)
def test_bas_DescOrder1000(benchmark):
  benchmark(insertDescendingOrder, t=BaseTree, n=1000)
def test_bas_OutInOrder1000(benchmark):
  benchmark(insertOutInOrder, t=BaseTree, n=1000)
def test_bas_RandomOrder1000(benchmark):
  benchmark(insertRandomOrder, t=BaseTree, n=1000)
def test_bas_AscOrder100(benchmark):
  benchmark(insertAscendingOrder, t=BaseTree, n=100)
def test_bas_DescOrder100(benchmark):
  benchmark(insertDescendingOrder, t=BaseTree, n=100)
def test_bas_OutInOrder100(benchmark):
  benchmark(insertOutInOrder, t=BaseTree, n=100)
def test_bas_RandomOrder100(benchmark):
  benchmark(insertRandomOrder, t=BaseTree, n=100)
def test_avl_AscOrder2500(benchmark):
  benchmark(insertAscendingOrder, t=AvlTree, n=2500)
def test_avl_DescOrder2500(benchmark):
  benchmark(insertDescendingOrder, t=AvlTree, n=2500)
def test_avl_OutInOrder2500(benchmark):
  benchmark(insertOutInOrder, t=AvlTree, n=2500)
def test_avl_RandomOrder2500(benchmark):
  benchmark(insertRandomOrder, t=AvlTree, n=2500)
def test_avl_AscOrder1000(benchmark):
  benchmark(insertAscendingOrder, t=AvlTree, n=1000)
def test_avl_DescOrder1000(benchmark):
  benchmark(insertDescendingOrder, t=AvlTree, n=1000)
def test_avl_OutInOrder1000(benchmark):
  benchmark(insertOutInOrder, t=AvlTree, n=1000)
def test_avl_RandomOrder1000(benchmark):
  benchmark(insertRandomOrder, t=AvlTree, n=1000)
def test_avl_AscOrder100(benchmark):
  benchmark(insertAscendingOrder, t=AvlTree, n=100)
def test_avl_DescOrder100(benchmark):
  benchmark(insertDescendingOrder, t=AvlTree, n=100)
def test_avl_OutInOrder100(benchmark):
  benchmark(insertOutInOrder, t=AvlTree, n=100)
def test_avl_RandomOrder100(benchmark):
  benchmark(insertRandomOrder, t=AvlTree, n=100)
