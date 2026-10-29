def calculate_subtotal(cart_items):
    return sum(i.get("price", 0.0) * i.get("quantity", 0) for i in cart_items if i.get("quantity", 0) > 0)

def get_tier_discount(member_tier):
    return {"gold": 0.20, "silver": 0.10, "bronze": 0.05}.get(member_tier, 0.0)

def get_coupon_discount(subtotal_after_tier, coupon_code):
    if coupon_code == "SAVE10" and subtotal_after_tier >= 50.0: return 10.0
    if coupon_code == "SUPER20" and subtotal_after_tier >= 100.0: return 20.0
    return 0.0

def calculate_tax(amount, state_code):
    rates = {"CA": 0.0825, "NY": 0.08875, "TX": 0.0625}
    return round(amount * rates.get(state_code, 0.05), 2)

def calculate_shipping(amount, state_code):
    if amount >= 150.0: return 0.0
    return 10.0 if state_code == "CA" else 15.0

def process_customer_order(cart_items, member_tier, coupon_code, state_code):
    subtotal = calculate_subtotal(cart_items)
    if subtotal == 0:
        return {"total": 0.0, "status": "empty_cart", "tax": 0.0, "shipping": 0.0}
    
    discounted_subtotal = subtotal * (1.0 - get_tier_discount(member_tier))
    post_coupon_total = max(0.0, discounted_subtotal - get_coupon_discount(discounted_subtotal, coupon_code))
    
    tax_amount = calculate_tax(post_coupon_total, state_code)
    shipping_fee = calculate_shipping(post_coupon_total, state_code)
    
    return {
        "total": round(post_coupon_total + tax_amount + shipping_fee, 2),
        "subtotal": round(subtotal, 2),
        "tax": tax_amount,
        "shipping": shipping_fee,
        "status": "processed"
    }
