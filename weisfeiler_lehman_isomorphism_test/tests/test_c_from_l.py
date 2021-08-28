from typing import Type

from numpy import negative
import pytest
from src.model.WL import WL
from igraph import *

def test_function_with_empty_input_parameters():
    wl = WL()
    with pytest.raises(TypeError):
        wl.c_from_l() is None

def test_all_empty():
    wl  = WL()
    with pytest.raises(TypeError):
        wl.c_from_l(None, None) is None

def test_empty_vectors():
    wl = WL()
    assert wl.c_from_l([], []) == -1

def test_empty_one_vector():
    wl = WL()
    with pytest.raises(TypeError):
        wl.c_from_l([], None) is None
    assert wl.c_from_l(None, []) == -1

def test_empty_previous_max():
    wl = WL()
    neighbors = [1,2,3]
    assert wl.c_from_l(None, neighbors) == -1
    with pytest.raises(TypeError):
        assert wl.c_from_l([], neighbors) is None

def test_empty_neighbors():
    wl = WL()
    previous_max = [1,2,3]
    with pytest.raises(TypeError):
        wl.c_from_l(previous_max, None) is None
    assert wl.c_from_l(previous_max, []) == -1
