# Order Processor Refactoring Task

## Overview
Refactored monolithic `process_customer_order` into modular, single-responsibility functions.

## Components Split Out
- `calculate_subtotal`: Validates and sums cart item totals.
- `get_tier_discount` & `get_coupon_discount`: Handles membership discounts and promotional vouchers.
- `calculate_tax` & `calculate_shipping`: Handles state lookup tables and free-shipping thresholds.
