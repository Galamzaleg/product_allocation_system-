from .models import db, ASIN, Client, Store, UngatingStatus, Preorder, Pallet
import datetime
import uuid

def generate_pallets():
    max_volume = 138240  # cubic inches
    max_weight = 2200  # lbs
    full_truck_load_cost = 1000  # USD

    pallets = []
    current_pallet = create_empty_pallet()

    asins = ASIN.query.filter(ASIN.remaining_quantity > 0).all()

    for asin in asins:
        volume = asin.package_dimensions
        weight = asin.item_weight

        if current_pallet['total_volume'] + volume > max_volume or current_pallet['total_weight'] + weight > max_weight:
            pallets.append(current_pallet)
            current_pallet = create_empty_pallet()

        current_pallet['items'].append(asin)
        current_pallet['total_volume'] += volume
        current_pallet['total_weight'] += weight
        current_pallet['total_cost'] += asin.unit_cost

    if current_pallet['items']:
        pallets.append(current_pallet)

    save_pallets(pallets)
    return {'status': 'success', 'message': 'Pallets generated successfully.'}

def create_empty_pallet():
    return {
        'items': [],
        'total_volume': 0,
        'total_weight': 0,
        'total_cost': 0
    }

def save_pallets(pallets):
    for pallet in pallets:
        pallet_id = generate_pallet_id()
        for item in pallet['items']:
            new_pallet = Pallet(
                pallet_id=pallet_id,
                client_id=item.client_id,
                store_id=item.store_id,
                asin_code=item.asin_code,
                quantity=item.remaining_quantity,
                shipping_cost_per_unit=item.min_shipping_price,  # or any other logic to calculate shipping cost
                total_shipping_cost=item.remaining_quantity * item.min_shipping_price,
                total_volume=item.package_dimensions,
                total_weight=item.item_weight,
                date_shipped=None,
                destination='Client Store'  # or 'Mutual Store' based on logic
            )
            db.session.add(new_pallet)
            item.remaining_quantity -= new_pallet.quantity

        db.session.commit()

def generate_pallet_id():
    return str(uuid.uuid4())
