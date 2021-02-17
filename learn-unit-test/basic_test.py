def test_sum_list():
    assert sum([1, 2, 3]) == 6, 'Should be 6'

def test_sum_tuple():
    assert sum((1, 2, 3)) == 6, 'Should be 6'

if __name__ == '__main__':
    test_sum_list()
    test_sum_tuple()
    print('Everything passed')