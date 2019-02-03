from autodeploy.app import compute_division, app

test_client = app.test_client()
test_client.testing = True


def test_root():
    response = test_client.get('/')
    assert(response.status_code == 200)
    assert(response.data.decode() == "Hello World!")


# def test_get_division():
#     response = test_client.get('/division?x=5&y=2')
#     assert(response.status_code == 200)
#     assert(response.data.decode() == "2.5")


def test_compute_product_non_zero():
    assert(compute_division(4, 2) == 2)


def test_compute_division_fraction():
    assert(compute_division(2, 4) == 0.5)


def test_compute_division_zero_denomintor():
    assert(compute_division(2, 0) == float('inf'))


def test_compute_division_zero_numerator():
    assert(compute_division(0, 2) == 0)
