import pytest
from src.model.WL import WL
from igraph import *

def test_function_with_empty_input_parameters():
    wl = WL()
    with pytest.raises(TypeError):
        wl.weisfeiler_lehman_isomorphism_test() is None

def test_passing_empty_graph():
    g = Graph()
    wl = WL()
    with pytest.raises(TypeError):
        wl.weisfeiler_lehman_isomorphism_test(g) is None

def test_passing_empty_parameters():
    wl = WL()
    g = Graph()
    assert wl.weisfeiler_lehman_isomorphism_test(None, None) == -1
    assert wl.weisfeiler_lehman_isomorphism_test(g, None) == -1
    assert wl.weisfeiler_lehman_isomorphism_test(None, g) == -1

