Product Allocation System

Overview

The Product Allocation System is designed to streamline the allocation of products to clients, manage ungating statuses, handle preorders, and generate pallets for shipping. The system integrates with external data sources (Google Sheets for the buying portal, AutoFBA panel, and ungating software) to ensure real-time data synchronization.


Project Structure
product_allocation_system/
│
├── app/
│   ├── __init__.py
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


Setup Instructions

1. Environment Setup
sh
	•	Install the necessary packages:

pip install -r requirements.txt

	•	Create the database in MySQL:
 sql
 CREATE DATABASE product_allocation_db;

 2. Configuration

	•	Update the config.py file with the appropriate database credentials.
python
import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/product_allocation_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

3. Initialize the Database

	•	Run the following commands to set up the database schema:
    sh
   flask shell
   python
   from app import create_app
from app.models import db

app = create_app()
with app.app_context():
    db.create_all()

    4. Running the Application

	•	Start the Flask application:
 sh
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
json
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

Conclusion

This documentation provides a comprehensive overview of the Product Allocation System, including setup instructions, key components, backend logic, user interface, and deployment steps. By following these instructions, you should be able to set up, deploy, and manage the system effectively.

Feel free to reach out if you need further clarifications or assistance.


חדםמ
