from hypothesis import given, strategies


@given(n=strategies.integers(min_value=0, max_value=5))
def test_example(n):
    assert n <= 5


def test_import():
    from qcsim import Circuit
    from qcsim import Simulator
