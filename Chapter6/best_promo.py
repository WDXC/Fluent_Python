from Order_other import *
promos = [fidelity_promo, bulk_item_promo, large_order_promo]


def best_promo(order):
    return max(promo(order) for promo in promos)