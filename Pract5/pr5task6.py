from hypothesis import given, strategies as st


def add(x, y):
    return x + y


@given(x=st.integers(), y=st.integers(), z=st.integers())
def test_add(x, y, z):
    assert add(x, y) == add(y, x)
    assert add(x, add(y, z)) == add(add(x, y), z)


# Вернуть наиболее часто встречающийся элемент
def mode(data):
    return max(data, key=data.count)


@given(data=st.lists(st.integers(), min_size=1))
def test_mode(data):
    res = mode(data)
    assert res in data
    assert all(data.count(res) >= data.count(x) for x in data)


test_add()
test_mode()