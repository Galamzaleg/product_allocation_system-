from flask import Blueprint, render_template, request, jsonify
from .models import db, ASIN, Client, Store, UngatingStatus, Preorder, Pallet
from .utils import generate_pallets

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/asins')
def asins():
    return render_template('asins.html')

@main.route('/clients')
def clients():
    return render_template('clients.html')

@main.route('/stores')
def stores():
    return render_template('stores.html')

@main.route('/ungating')
def ungating():
    return render_template('ungating.html')

@main.route('/preorders')
def preorders():
    return render_template('preorders.html')

@main.route('/pallets')
def pallets():
    return render_template('pallets.html')

@main.route('/cart_generator')
def cart_generator():
    return render_template('cart_generator.html')

@main.route('/generate_pallets', methods=['POST'])
def generate_pallets_route():
    result = generate_pallets(request.json['clientID'], request.json['storeID'])
    return jsonify(result)

@main.route('/api/asins')
def get_asins():
    asins = ASIN.query.all()
    asins_list = [{
        'asin_code': asin.asin_code,
        'min_shipping_price': asin.min_shipping_price,
        'max_shipping_price': asin.max_shipping_price,
        'item_weight': asin.item_weight,
        'package_dimensions': asin.package_dimensions,
        'quantity_purchased': asin.quantity_purchased,
        'unit_cost': asin.unit_cost,
        'remaining_quantity': asin.remaining_quantity,
        'date_added': asin.date_added.strftime('%Y-%m-%d')
    } for asin in asins]
    return jsonify(asins_list)

@main.route('/api/clients')
def get_clients():
    clients = Client.query.all()
    clients_list = [{
        'client_name': client.client_name,
        'balance': client.balance,
        'priority': client.priority,
        'last_pallet_date': client.last_pallet_date.strftime('%Y-%m-%d') if client.last_pallet_date else None,
        'total_allocated_amount': client.total_allocated_amount
    } for client in clients]
    return jsonify(clients_list)

@main.route('/api/stores')
def get_stores():
    stores = Store.query.all()
    stores_list = [{
        'client_id': store.client_id,
        'store_name': store.store_name,
        'store_status': store.store_status
    } for store in stores]
    return jsonify(stores_list)

@main.route('/api/ungating')
def get_ungating():
    ungating_statuses = UngatingStatus.query.all()
    ungating_list = [{
        'store_id': ungating.store_id,
        'asin_code': ungating.asin_code,
        'ungated_status': ungating.ungated_status
    } for ungating in ungating_statuses]
    return jsonify(ungating_list)

@main.route('/api/preorders')
def get_preorders():
    preorders = Preorder.query.all()
    preorders_list = [{
        'asin_code': preorder.asin_code,
        'client_id': preorder.client_id,
        'pre_order_quantity': preorder.pre_order_quantity,
        'pre_order_amount': preorder.pre_order_amount,
        'remaining_balance_due': preorder.remaining_balance_due,
        'expected_arrival_date': preorder.expected_arrival_date.strftime('%Y-%m-%d'),
        'pre_order_status': preorder.pre_order_status
    } for preorder in preorders]
    return jsonify(preorders_list)

@main.route('/api/pallets')
def get_pallets():
    pallets = Pallet.query.all()
    pallets_list = [{
        'pallet_id': pallet.pallet_id,
        'client_id': pallet.client_id,
        'store_id': pallet.store_id,
        'asin_code': pallet.asin_code,
        'quantity': pallet.quantity,
        'shipping_cost_per_unit': pallet.shipping_cost_per_unit,
        'total_shipping_cost': pallet.total_shipping_cost,
        'total_volume': pallet.total_volume,
        'total_weight': pallet.total_weight,
        'date_shipped': pallet.date_shipped.strftime('%Y-%m-%d') if pallet.date_shipped else None,
        'destination': pallet.destination
    } for pallet in pallets]
    return jsonify(pallets_list)

