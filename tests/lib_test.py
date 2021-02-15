# tests/lib_test.py
from mlproject.lib import hello_world

def test_length_of_hello_world():
    assert len(hello_world()) != 0

from mlproject.distance import haversine

def test_haversine():
    assert type(haversine(48.865070, 2.380009, 48.865070, 2.380009)) == float