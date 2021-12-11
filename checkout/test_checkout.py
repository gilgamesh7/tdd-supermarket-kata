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

# Refactored - As additem price is repeated
# @pytest.fixture()
# def checkout()-> Checkout:
#     checkout = Checkout()

#     return checkout

# REFACTORED - as these 2 areimplemented in test_CanCalculateCurrentTotal
# # Can add item price
# def test_CanAddItemPrice(checkout):
#     checkout.add_item_price("Item1",20.5)

# # can add item
# def test_CanAddItem(checkout):
#     checkout.add_item("Item1")

# REFACTORED - add item is now part of fixture
# # can calculate current total
# def test_CanCalculateCurrentTotal(checkout):
#     checkout.add_item_price("Item1",20.5)
#     checkout.add_item("Item1")

#     assert checkout.calculate_current_total() == 20.5

# # can add multiple items and getcurrent total
# def test_CanAddMultipleItemsAndCalculateCorrectTotal(checkout):
#     checkout.add_item_price("Item1",20.5)
#     checkout.add_item_price("Item2",30.5)
#     checkout.add_item("Item1")
#     checkout.add_item("Item2")

#     assert checkout.calculate_current_total() == 51
# # can calculate current total
# def test_CanCalculateCurrentTotal(checkout):
#     checkout.add_item_price("Item1",20.5)
#     checkout.add_item("Item1")

#     assert checkout.calculate_current_total() == 20.5

@pytest.fixture()
def checkout()-> Checkout:
    checkout = Checkout()
    checkout.add_item_price("Item1",20.5)
    checkout.add_item_price("Item2",30.5)

    return checkout

# can calculate current total
def test_CanCalculateCurrentTotal(checkout):
    checkout.add_item("Item1")

    assert checkout.calculate_current_total() == 20.5

# can add multiple items and getcurrent total
def test_CanAddMultipleItemsAndCalculateCorrectTotal(checkout):
    checkout.add_item("Item1")
    checkout.add_item("Item2")

    assert checkout.calculate_current_total() == 51

# REFACTORING - part of can apply discounts
# can add discount rules
# @pytest.mark.skip
# def test_CanAddDiscountRules(checkout):
#     checkout.add_discount("Item1", 3, 2.5)

# @pytest.mark.skip
def test_CanApplyDiscounts(checkout):
    checkout.add_discount("Item1", 3, 10.4)
    checkout.add_item("Item1")
    checkout.add_item("Item1")
    checkout.add_item("Item1")

    assert checkout.calculate_current_total() == 10.4

def test_ThrowExceptionForItemWithNoPrice(checkout):
    with pytest.raises(Exception):
        checkout.add_item("Item3")

