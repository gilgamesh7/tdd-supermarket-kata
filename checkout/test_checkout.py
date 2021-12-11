import pytest

from checkout import Checkout


# REFACTOR - not needed afterfirst test
# def test_assert_true():
#     assert True


# REFACTOR - not needed after methods start getting used
# can create instance of checkout class
# def test_InstantiateCheckoutClass():
#     checkout = Checkout()

# REFACTOR - Add Fixture
# Can add item price
# def test_CanAddItemPrice():
#     checkout = Checkout()
#     checkout.add_item_price("Item1",20.5)

# # can add item
# def test_CanAddItem():
#     checkout = Checkout()
#     checkout.add_item("Item1")

@pytest.fixture()
def checkout()-> Checkout:
    checkout = Checkout()

    return checkout

# REFACTORED - as these 2 areimplemented in test_CanCalculateCurrentTotal
# # Can add item price
# def test_CanAddItemPrice(checkout):
#     checkout.add_item_price("Item1",20.5)

# # can add item
# def test_CanAddItem(checkout):
#     checkout.add_item("Item1")

# can calculate current total
def test_CanCalculateCurrentTotal(checkout):
    checkout.add_item_price("Item1",20.5)
    checkout.add_item("Item1")

    assert checkout.calculate_current_total() == 20.5




