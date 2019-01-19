from autodeploy import main


def test_compute_product_non_zero():
    assert(main.compute_division(4, 2) == 2)


def test_compute_division_fraction():
    assert(main.compute_division(2, 4) == 0.5)


def test_compute_division_zero_denomintor():
    assert(main.compute_division(2, 0) == float('inf'))


def test_compute_division_zero_numerator():
    assert(main.compute_division(0, 2) == 0)
