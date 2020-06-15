# Shopping Cart Application

# Business Problem

The local corner grocery store has hired you as a technology consultant to help modernize their checkout system.

Currently, when managing inventory, store employees affix a price tag sticker on each grocery item in stock. And when a customer visits the checkout counter with their selected items, a checkout clerk uses a calculator to add product prices, calculate tax, and calculate the total amount due.

Instead, the store owner describes a desired checkout process which involves the checkout clerk scanning each product's barcode to automatically lookup prices, perform tax and total calculations, and print a customer receipt. To facilitate this process, the store owner has authorized the purchase of a few inexpensive barcode scanners, as well as checkout computers capable of running Python applications.

The store owner says it would be "acceptable but not preferable" to manage the inventory of products via the application's source code, that it would be "better" to manage the inventory of products via a local CSV file stored on the checkout computer, and that it would be "ideal" to be able to manage the inventory of products via a centralized Google Sheet spreadsheet document.

The store owner also says it would be "nice to have" a feature which prompts the checkout clerk or the customer to input the customer's email address in order to send them a receipt via email.

# Setup & Implementation

When running this application, be sure to install the following modules into your python environment in order to properly use the Google Sheets API and the Sendgrid email generator:

pip install gspread oauth2client
pip install sendgrid==6.0.5

# Running the Application

The system will prompt the user to enter the product ID numbers for the items the customer is purchasing one-by-one.

If the clerk enters the wrong UPC, the system will prompt the clerk to re-enter the appropriate number.

At the end of the transaction, a receipt will display on screen for the clerk and customer's review, at which point the clerk will be prompted to ask the customer if they would like an receipt emailed to them. If the customer does, the clerk will be prompted to enter their email address.