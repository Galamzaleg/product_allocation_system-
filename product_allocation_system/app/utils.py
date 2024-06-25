from .models import db, ASIN, Client, Store, UngatingStatus, Preorder, Pallet
import datetime
import uuid

def generate_pallets(client_id, store_id):
    max_volume = 138240  # cubic inches
    max_weight = 2200  # lbs
    full_truck_load_cost = 1000  # USD

    pallets = []
    current_pallet = create_empty_pallet()
    mutual_pallet = create_empty_pallet(mutual=True)

    asins = ASIN.query.filter(ASIN.remaining_quantity > 0).all()
    client = Client.query.get(client_id)
    store = Store.query.get(store_id)

    if not client or not store:
        return {'status': 'error', 'message': 'Invalid client or store ID'}

    client_asins = [asin for asin in asins if is_ungated(asin, store)]
    if not client_asins or client.balance <= 0:
        return {'status': 'error', 'message': 'No ungated ASINs or insufficient balance'}

    for asin in client_asins:
        volume = asin.package_dimensions
        weight = asin.item_weight

        if current_pallet['total_volume'] + volume > max_volume or current_pallet['total_weight'] + weight > max_weight:
            pallets.append(current_pallet)
            current_pallet = create_empty_pallet()

        if client.balance < (asin.unit_cost * asin.remaining_quantity + asin.min_shipping_price * asin.remaining_quantity):
            mutual_pallet['items'].append(asin)
            mutual_pallet['total_volume'] += volume
            mutual_pallet['total_weight'] += weight
            mutual_pallet['total_cost'] += asin.unit_cost
        else:
            current_pallet['items'].append(asin)
            current_pallet['total_volume'] += volume
            current_pallet['total_weight'] += weight
            current_pallet['total_cost'] += asin.unit_cost
            client.balance -= (asin.unit_cost * asin.remaining_quantity + asin.min_shipping_price * asin.remaining_quantity)

    if current_pallet['items']:
        pallets.append(current_pallet)

    if mutual_pallet['items']:
        pallets.append(mutual_pallet)

    save_pallets(pallets)
    return {'status': 'success', 'message': 'Pallets generated successfully.'}

def create_empty_pallet(mutual=False):
    return {
        'items': [],
        'total_volume': 0,
        'total_weight': 0,
        'total_cost': 0,
        'destination': 'Mutual Store' if mutual else 'Client Store'
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
                destination=pallet['destination']
            )
            db.session.add(new_pallet)
            item.remaining_quantity -= new_pallet.quantity

        db.session.commit()

def generate_pallet_id():
    return str(uuid.uuid4())

def is_ungated(asin, store):
    ungating_status = UngatingStatus.query.filter_by(asin_code=asin.asin_code, store_id=store.id).first()
    return ungating_status and ungating_status.ungated_status == 'Yes'
