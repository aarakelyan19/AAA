import pytest
from one_hot_encoder import fit_transform


def test_tf_equal(self):
    actual = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
    expected = [('Moscow', [0, 0, 1]), ('New York', [0, 1, 0]), ('Moscow', [0, 0, 1]), ('London', [1, 0, 0])]

    assert expected == actual
       
def test_tf_notequal(self):
    actual = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
    expected = [('Moscow', [0, 0, 1]), ('New York', [0, 1, 0]), ('London', [1, 0, 0])]

    assert expected != actual

def test_empty(self):
    actual = list(fit_transform(''))
    expected = [('', [1])]

    assert expected == actual

def test_NotIn(self):
    actual = fit_transform(['a', 'b'])
        
    assert actual not in 'jgj'
        
        
        
if __name__ == '__main__':
   pytest.main()
