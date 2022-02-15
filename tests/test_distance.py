# tests/test_distance.py
from mlproject.distance import haversine


def test_result_of_haversine():
    assert haversine(48.865070, 2.380009, 48.235070,
                     2.393409) == 70.00789153218594


def test_type_of_haversine():
    assert type(haversine(48.865070, 2.380009, 48.235070,
                          2.393409)) == float
