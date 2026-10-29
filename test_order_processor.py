import pytest
from order_processor import process_customer_order

def test_empty_cart():
    res = process_customer_order([], "gold", "SAVE10", "CA")
    assert res["status"] == "empty_cart" and res["total"] == 0.0

def test_gold_tier_with_valid_coupon():
    res = process_customer_order([{"price": 100.0, "quantity": 1}], "gold", "SAVE10", "CA")
    assert res["total"] == 85.78

def test_coupon_below_minimum_spend_ignored():
    res = process_customer_order([{"price": 40.0, "quantity": 1}], "none", "SAVE10", "NY")
    assert res["subtotal"] == 40.0

def test_fallback_state_tax_rate():
    res = process_customer_order([{"price": 100.0, "quantity": 1}], "none", "", "FL")
    assert res["tax"] == 5.0

def test_free_shipping_over_threshold():
    res = process_customer_order([{"price": 200.0, "quantity": 1}], "none", "", "TX")
    assert res["shipping"] == 0.0
