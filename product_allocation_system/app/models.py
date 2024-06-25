from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ASIN(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    asin_code = db.Column(db.String(20), unique=True, nullable=False)
    min_shipping_price = db.Column(db.Float, nullable=False, default=0.10)
    max_shipping_price = db.Column(db.Float, nullable=False)
    item_weight = db.Column(db.Float, nullable=False)
    package_dimensions = db.Column(db.Float, nullable=False)
    quantity_purchased = db.Column(db.Integer, nullable=False)
    unit_cost = db.Column(db.Float, nullable=False)
    remaining_quantity = db.Column(db.Integer, nullable=False)
    date_added = db.Column(db.Date, nullable=False)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(255), unique=True, nullable=False)
    balance = db.Column(db.Float, nullable=False)
    priority = db.Column(db.String(20), nullable=False, default="Low")
    last_pallet_date = db.Column(db.Date, nullable=True)
    total_allocated_amount = db.Column(db.Float, nullable=False, default=0.0)

class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    store_name = db.Column(db.String(255), nullable=False)
    store_status = db.Column(db.String(20), nullable=False)

class UngatingStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'), nullable=False)
    asin_code = db.Column(db.String(20), nullable=False)
    ungated_status = db.Column(db.String(50), nullable=False)

class Preorder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    asin_code = db.Column(db.String(20), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    pre_order_quantity = db.Column(db.Integer, nullable=False)
    pre_order_amount = db.Column(db.Float, nullable=False)
    remaining_balance_due = db.Column(db.Float, nullable=False)
    expected_arrival_date = db.Column(db.Date, nullable=False)
    pre_order_status = db.Column(db.String(20), nullable=False)

class Pallet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pallet_id = db.Column(db.String(20), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'), nullable=False)
    asin_code = db.Column(db.String(20), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    shipping_cost_per_unit = db.Column(db.Float, nullable=False)
    total_shipping_cost = db.Column(db.Float, nullable=False)
    total_volume = db.Column(db.Float, nullable=False)
    total_weight = db.Column(db.Float, nullable=False)
    date_shipped = db.Column(db.Date, nullable=True)
    destination = db.Column(db.String(20), nullable=False)
