# Product Allocation System

## Overview

The Product Allocation System is designed to streamline the allocation of products to clients, manage ungating statuses, handle preorders, and generate pallets for shipping. The system integrates with external data sources (Google Sheets for the buying portal, AutoFBA panel, and ungating software) to ensure real-time data synchronization.

## Project Structure

product_allocation_system/
│
├── app/
│   ├── init.py
│   ├── models.py
│   ├── routes.py
│   ├── utils.py
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   └── js/
│   │       ├── main.js
│   │       └── allocation.js
│   ├── templates/
│   │   ├── index.html
│   │   ├── asins.html
│   │   ├── clients.html
│   │   ├── stores.html
│   │   ├── ungating.html
│   │   ├── preorders.html
│   │   ├── pallets.html
│   │   ├── cart_generator.html
├── config.py
├── requirements.txt
└── run.py

## Setup Instructions

### 1. Environment Setup

- Install the necessary packages:

```sh
pip install -r requirements.txt

	•	Create the database in MySQL:
CREATE DATABASE product_allocation_db;

2. Configuration

	•	Update the config.py file with the appropriate database credentials.
import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/product_allocation_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

3. Initialize the Database

	•	Run the following commands to set up the database schema:
flask shell

from app import create_app
from app.models import db

app = create_app()
with app.app_context():
    db.create_all()

4. Running the Application

	•	Start the Flask application:
python run.py

	Open your browser and navigate to http://localhost:5000 to access the Product Allocation System.

Components and Functionality

Data Integration and Synchronization

	•	Google Sheets: Continuous polling to fetch ASIN data.
	•	AutoFBA Panel: Real-time synchronization to fetch client names, balances, and store details.
	•	Ungating Software: Real-time synchronization to fetch ungating statuses.

User Interface (UI)

	•	ASIN Management: Add, edit, delete ASINs.
	•	Client Management: Add, edit, delete clients.
	•	Store Management: Add, edit, delete stores.
	•	Ungating Management: Update and view ungating statuses.
	•	Preorder Management: Manage preorders and update statuses.
	•	Pallet Management: Generate, view, and manage pallets.
	•	Cart Generator: Generate a cart for a client.

Backend Logic and Algorithms

	•	Pallet Generator Algorithm: Prioritizes products, ensures ungating requirements, optimizes shipping costs.
	•	Shipping Cost Calculation: Calculates based on ASIN min/max shipping prices.
	•	Insufficient Balance Handling: Suggests transferring products to a mutual store and notifies the admin.
	•	Ungating Status Check: Checks and handles ungating status.

Notifications and Alerts

	•	System Notifications: Notifications for successful allocation, insufficient balance, ungating status updates, and pre-order arrivals.
	•	Delivery: Email notifications to allocation@profitzon.net and system alerts on the dashboard.

Backup and Recovery

	•	Data Backup: Daily backups of the database.
	•	Recovery: Automated scripts to restore from the latest backup in case of data loss.
	•	Error Handling and Logging: Detailed logging and error handling mechanisms.

API Endpoints

Generate Pallets

	•	POST /generate_pallets

Request body:

{
  "clientName": "Client A",
  "clientID": "1",
  "storeID": "1"
}

etch ASIN Data

	•	GET /api/asins

Fetch Client Data

	•	GET /api/clients

Fetch Store Data

	•	GET /api/stores

Fetch Ungating Status Data

	•	GET /api/ungating

Fetch Preorder Data

	•	GET /api/preorders

Fetch Pallet Data

	•	GET /api/pallets

Example Workflow

	1.	Initialize the system: Set up the environment, configure the database, and start the application.
	2.	Data synchronization: Ensure real-time synchronization of data from Google Sheets, AutoFBA panel, and ungating software.
	3.	Manage entities: Use the UI to manage ASINs, clients, stores, ungating statuses, preorders, and pallets.
	4.	Generate pallets: Use the Cart Generator to create and manage pallets, ensuring efficient allocation based on the client’s balance and shipping cost optimization.

SOP for Using the System

1. Accessing the System

	1.	Open your web browser and navigate to http://localhost:5000.
	2.	Log in with your credentials.

2. Managing ASINs

	1.	Click on the “ASINs” tab in the navigation menu.
	2.	To add a new ASIN, click “Add ASIN” and fill out the form with the following details:
	•	ASIN Code
	•	Min Shipping Price
	•	Max Shipping Price
	•	Item Weight
	•	Package Dimensions (in inches)
	•	Quantity Purchased
	•	Unit Cost
	•	Remaining Quantity
	•	Date Added
	3.	To edit an existing ASIN, click the “Edit” button next to the ASIN you want to update.
	4.	To delete an ASIN, click the “Delete” button next to the ASIN you want to remove.

3. Managing Clients

	1.	Click on the “Clients” tab in the navigation menu.
	2.	To add a new client, click “Add Client” and fill out the form with the following details:
	•	Client Name
	•	Balance
	•	Priority (Low, Medium, High)
	3.	To edit an existing client, click the “Edit” button next to the client you want to update.
	4.	To delete a client, click the “Delete” button next to the client you want to remove.

4. Managing Stores

	1.	Click on the “Stores” tab in the navigation menu.
	2.	To add a new store, click “Add Store” and fill out the form with the following details:
	•	Client ID
	•	Store Name
	•	Store Status (Active, Suspended)
	3.	To edit an existing store, click the “Edit” button next to the store you want to update.
	4.	To delete a store, click the “Delete” button next to the store you want to remove.

5. Managing Ungating Statuses

	1.	Click on the “Ungating Status” tab in the navigation menu.
	2.	To update the ungating status, click the “Edit” button next to the ASIN you want to update and select the appropriate status (Yes, No, No - Invoice Needed).

6. Managing Pre-orders

	1.	Click on the “Pre-orders” tab in the navigation menu.
	2.	To add a new pre-order, click “Add Pre-order” and fill out the form with the following details:
	•	ASIN Code
	•	Client ID
	•	Pre-order Quantity
	•	Pre-order Amount
	•	Remaining Balance Due
	•	Expected Arrival Date
	•	Pre-order Status
	3.	To edit an existing pre-order, click the “Edit” button next to the pre-order you want to update.
	4.	To delete a pre-order, click the “Delete” button next to the pre-order you want to remove.

7. Generating Pallets

	1.	Click on the “Cart Generator” tab in the navigation menu.
	2.	Select the client for whom you want to generate a pallet:
	•	Enter the Client Name.
	•	Enter the Client ID.
	•	Enter the Store ID.
	3.	Click the “Generate Cart” button.
	4.	The system will generate a cart based on the available ASINs and the client’s balance, optimizing for the lowest possible shipping cost within the specified range.
	5.	Mutual Store Allocation:
	•	If a client’s balance is insufficient to generate a standalone pallet or there are not enough ungated products, the system will allocate those products to a mutual store.
	•	The mutual store will consolidate products from multiple clients, ensuring efficient use of shipping resources.
	6.	Review the generated cart in the table below the form. Ensure that the allocation meets the client’s needs and balance constraints.

8. Managing Pallets

	1.	Click on the “Pallets” tab in the navigation menu.
	2.	Review the list of generated pallets. Each pallet will include details such as:
	•	Pallet ID
	•	Client ID
	•	Store ID
	•	ASIN Code
	•	Quantity
	•	Shipping Cost per Unit
	•	Total Shipping Cost
	•	Total Volume
	•	Total Weight
	•	Date Shipped
	•	Destination
	3.	To mark a pallet as shipped, click the “Edit” button next to the pallet and enter the shipment date.

9. Notifications and Alerts

	1.	Monitor the system for any notifications and alerts regarding:
	•	Successful allocations
	•	Insufficient balance
	•	Ungating status updates
	•	Pre-order arrivals
	2.	Address any issues promptly and update the relevant records.

Conclusion

This documentation provides a comprehensive overview of the Product Allocation System, including setup instructions, key components, backend logic, user interface, and deployment steps. By following these instructions, your developer should be able to set up, deploy, and manage the system effectively.

Final Implementation Notes

	1.	Data Integration: Ensure real-time synchronization with Google Sheets, AutoFBA panel, and ungating software.
	2.	Mutual Store Logic: Implement logic to allocate products to a mutual store when a client’s balance is insufficient or there are not enough ungated products.
	3.	Admin User: Initially, set up one admin user with full access. Future versions can include role-based access control.
	4.	Error Handling: Implement detailed error handling and logging mechanisms to track and resolve issues.
	5.	Backup and Recovery: Set up daily data backups and recovery scripts.



