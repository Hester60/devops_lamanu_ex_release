import main

def test_calc():
    """Verify output of calc()"""
    output = main.calc(1, 1)
    assert output == 2