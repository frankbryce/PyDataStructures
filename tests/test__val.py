import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")

import pytest
from Trees import _val

def test_ValIsComparableByKey():
  v1 = _val(1,2)
  v2 = _val(2,1)
  assert v1 < v2
  assert v1 <= v2
  assert v1 != v2
  assert not (v1 == v2)
  assert not (v1 >= v2)
  assert not (v1 > v2)

def test_ValIsComparableByKey2():
  v1 = _val(1,2)
  v2 = _val(1,3)
  assert not(v1 < v2)
  assert not (v1 > v2)
  assert v1 == v2
  assert v1 >= v2
  assert v1 <= v2
  assert not (v1 != v2)

def test_ValIsComparableByKey3():
  v1 = _val(2,2)
  v2 = _val(1,1)
  assert not (v1 < v2)
  assert not (v1 <= v2)
  assert v1 != v2
  assert not (v1 == v2)
  assert v1 >= v2
  assert v1 > v2