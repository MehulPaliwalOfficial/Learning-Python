import math
# ─────────────────────────────────────────────────────────────────
# RapidKart Technologies — Inventory Audit Module
# File: quality_checker.py  |  Author: Rohan M.  |  Status: Review
# ─────────────────────────────────────────────────────────────────
ADMIN_BIT     = 0b100   # permission: full audit access (bit 2)
WAREHOUSE_BIT = 0b010   # permission: warehouse view   (bit 1)
VIEWER_BIT    = 0b001   # permission: read-only        (bit 0)
def audit_inventory(products, user_flags):
    """
    products  : list of dicts — each has 'sku' (str), 'name' (str),
                'stock' (int), 'price' (float), 'premium' (bool)
    user_flags: int, bit-encoded permissions for the calling user
    Returns   : set of flagged SKU IDs requiring manual review
    """
    # ── 1. Verify the calling user has admin access ──────────────
    if (user_flags & ADMIN_BIT) > 0:     #user and admin has value 1 and anything else is any natural number, so != 0 must be answer
        print("Full audit access granted")
    else:
        print("Limited access — read-only mode")
    # ── 2. Build the report header ───────────────────────────────
    total_skus = len(products)
    header = f"RapidKart Audit — SKUs scanned: total_skus"
    print(header)
    # ── 3. Track unique SKUs seen across warehouses ──────────────
    seen_skus = []      # [] Let's u duplicate entries so () is to be used
    for p in products:
        seen_skus.append(p["sku"])
    # ── 4. Flag products with invalid stock or price data ─────────
    flagged = {}        # set{}
    for p in products:
        if p["stock"] < 0 or p["price"] < 0:
            flagged.add(p["sku"])
    # ── 5. Spot-check delivery fee rate ──────────────────────────
    base_fee      = 0.1
    surcharge     = 0.2
    combined_rate = base_fee + surcharge        #mismatch
    if combined_rate == 0.3:
        print("Delivery fee rate: OK")
    else:
        print("Delivery fee rate: MISMATCH — investigate!")
    # ── 6. Compute average product price ─────────────────────────
    total_value = sum(p["price"] for p in products)
    avg_price   = total_value // len(products)
    print(f"Average price: Rs.{avg_price:.2f}")
    # ── 7. Capitalise brand name for the report ───────────────────
    brand_name = "rapidkart"
    brand_name[0] = brand_name[0].upper()
    print(f"Brand: {brand_name}")
    # ── 8. Flag out-of-stock items as removal candidates ─────────
    for p in products:
        is_premium = p.get("premium", False)
        if p["stock"] == 0 or not is_premium:
            flagged.add(p["sku"])
            print(header)
            print(f"Unique SKUs tracked: {len(seen_skus)}")
            return flagged

def main():
    print("This script is running directly!")

if __name__ == "__main__":
    main()
