Explanation for the Developer

System Overview

The Product Allocation System is designed to streamline the allocation of products to clients, manage ungating statuses, handle preorders, and generate pallets for shipping. The system integrates with external data sources (Google Sheets for the buying portal, AutoFBA panel, and ungating software) to ensure real-time data synchronization.

Components and Functionality

	1.	Data Integration and Synchronization
	•	Google Sheets: Continuous polling to fetch ASIN data, including ASIN code, item weight, quantity purchased, unit cost, remaining quantity, date added, min/max shipping prices, and package dimensions.
	•	AutoFBA Panel: Real-time synchronization to fetch client names, balances, and store details.
	•	Ungating Software: Real-time synchronization to fetch ungating statuses (Yes, No, No, Invoice Needed).
2.	User Interface (UI) (continued)
	•	Ungating Management: Allows users to update and view ungating statuses. Displays ungating details including ASIN code, store ID, and ungating status.
	•	Preorder Management: Allows users to manage preorders and update statuses. Displays preorder details including ASIN code, client ID, preorder quantity, preorder amount, remaining balance due, expected arrival date, and preorder status.
	•	Pallet Management: Allows users to generate, view, and manage pallets. Displays pallet details including pallet ID, client ID, store ID, ASIN code, quantity, shipping cost per unit, total shipping cost, total volume, total weight, date shipped, and destination.
	•	Cart Generator: Interface for generating a cart for a client. Users can select a client, store, and specify the amount to allocate. Generates a cart based on available ASINs and client balance.
	3.	Backend Logic and Algorithms
	•	Pallet Generator Algorithm: Prioritizes products that have been in inventory the longest, ensures products meet ungating status requirements, and optimizes shipping costs within the min/max range while striving to choose the lowest price possible.
	•	Shipping Cost Calculation: Calculates based on ASIN min/max shipping prices, striving to keep shipping costs as close to the minimum as possible.
	•	Insufficient Balance Handling: Suggests transferring products to a mutual store if the client’s balance is insufficient and notifies the admin to request more balance from the client.
	•	Ungating Status Check: Checks ungating status for each ASIN before allocation and handles manual ungating actions if needed. Notifies the admin for ungating actions required.
	4.	Notifications and Alerts
	•	System Notifications: Includes notifications for successful allocation, insufficient balance, ungating status updates, and pre-order arrivals. Notifications are delivered via email to allocation@profitzon.net and as system alerts on the dashboard.
	5.	Backup and Recovery
	•	Data Backup: Daily backups of the database.
	•	Recovery: Automated scripts to restore from the latest backup in case of data loss.
	•	Error Handling and Logging: Detailed logging and error handling mechanisms with a dedicated dashboard for viewing logs and system health.


Steps to Set Up and Deploy the System

	1.	Set Up the Environment
	•	Install the necessary packages:
 pip install -r requirements.txt

	1.		•	Create the database in MySQL:
 CREATE DATABASE product_allocation_db;

 	2.	Configure the Application
	•	Update the config.py file with the appropriate database credentials.
	3.	Initialize the Database
	•	Run the following commands to set up the database schema:

 flask shell

 from app import create_app
from app.models import db

app = create_app()
with app.app_context():
    db.create_all()


 Run the Application
	•	Start the Flask application:

 python run.py

 	5.	Access the Application
	•	Open your browser and navigate to http://localhost:5000 to access the Product Allocation System.
	6.	Testing and Validation
	•	Perform unit tests, integration tests, and end-to-end tests to ensure the system meets all functional and non-functional requirements.


Example API Requests

Generate Pallets

To generate pallets, a POST request is sent to /generate_pallets with the client and store information:

{
  "clientName": "Client A",
  "clientID": "1",
  "storeID": "1"
}

Fetch ASIN Data

To fetch ASIN data, a GET request is sent to /api/asins.

Conclusion

This documentation provides a comprehensive overview of the Product Allocation System, including the project structure, key components, backend logic, user interface, and deployment steps. By following these instructions, your developer should be able to set up, deploy, and manage the system effectively.

Feel free to reach out if you need further clarifications or assistance.
