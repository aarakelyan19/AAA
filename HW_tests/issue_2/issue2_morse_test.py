import pytest

from morse_issue1 import decode

@pytest.mark.parametrize('s,exp', [
    ('.... . .-.. .-.. ---', 'HELLO'),
    ('.... ..', 'HI'),
    ('.... . -.--', 'HEY')
    ])

def test_decode(s, exp):
    assert decode(s) == exp
