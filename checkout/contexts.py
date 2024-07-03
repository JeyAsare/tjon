from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def checkout_contents(request):
    bag_items = []
    total = Decimal(0)
    product_count = 0
    bag = request.session.get('bag', {})
    delivery_cost = Decimal(settings.DELIVERY_FOR_ORDER)
    free_delivery_delta = 0
    bundle_discount = Decimal(0)

    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        if isinstance(item_data, int):
            quantity = item_data
            size = None
        elif isinstance(item_data, dict):
            quantity = item_data.get('quantity', 0)
            size = item_data.get('size', None)
        else:
            continue

        product_count += quantity
        total += quantity * product.price

        if not product.size:  # Apply discount only if product does not have a size
            bundle_discount += quantity * (product.price * Decimal(settings.BUNDLE_DISCOUNT_PERCENTAGE / 100))

        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'size': size,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery_cost = 0
        free_delivery_delta = 0

    grand_total = total - bundle_discount + delivery_cost
    if grand_total < 0:
        grand_total = 0  # Ensure grand_total is never negative


    context = {
        'bag_items': bag_items,
        'total': total,
        'bundle_discount': bundle_discount,
        'product_count': product_count,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'delivery_cost': delivery_cost,
        'grand_total': grand_total,
    }

    return context