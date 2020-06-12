# shopping_cart.py
import datetime

import gspread
from oauth2client.service_account import ServiceAccountCredentials

import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


AUTH_SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets", 
    "https://www.googleapis.com/auth/drive.file" 
]
creds = ServiceAccountCredentials.from_json_keyfile_name('google_api_credentials.json', AUTH_SCOPE)
client = gspread.authorize(creds)

# Find a workbook by name and open a sheet
os.environ["GOOGLE_SHEET_ID"] = "1ItN7Cc2Yn4K90cMIsxi2P045Gzw0y2JHB_EkV4mXXpI"
DOCUMENT_ID = os.environ.get("GOOGLE_SHEET_ID", "OOPS")
SHEET_NAME = os.environ.get("Shopping Cart Project - Datastore", "products")
doc = client.open_by_key(DOCUMENT_ID)
sheet = doc.worksheet(SHEET_NAME)

# Pull Google Sheet values into the application
products = sheet.get_all_records()

def to_usd(my_price):
    return f"${my_price:,.2f}"
  
subtotal_price = 0
UPCs = []

while True:
    UPC = input("Please input the product number: ")
    if UPC == "Done":
        break
    else:
        UPCs.append(UPC)

print("------------------------------------------")
print("             Mr Mango Grocery             ")
print("             59 Lafayette Ave             ")
print("         Brooklyn, New York 11217         ")
print("              (929) 250-2000              ")
print("                OPEN 24 HRS               ")
print("------------------------------------------")

now = datetime.datetime.now()
print("   Checked out at:", now.strftime("%m/%d/%Y  %I:%M%p"))
print("------------------------------------------")
print("Purchased Items:")
print(" ")

for UPC in UPCs:
    matching_products = [p for p in products if str(p["id"]) == str(UPC)]
    matching_product = matching_products[0]
    subtotal_price = subtotal_price + matching_product["price"]
    matching_product_price = to_usd(matching_product["price"])
    matching_prouduct_count = len(matching_product)
    print("  ..." + matching_product["name"] + " " + str(matching_product_price))

tax = subtotal_price * .0875
total_price = subtotal_price + tax

subtotal_price = to_usd(subtotal_price)
tax = to_usd(tax)
total_price = to_usd(total_price)

UPC_total = len(UPCs)

print(" ")
print("     " + "Subtotal: " + "    " + str(subtotal_price))
print("     " + "Tax: " + "         " + str(tax))
print("     " + "Total: " + "       " + str(total_price))
print("     " + "Items Sold: " + "  " + str(UPC_total))
print(" ")
print("------------------------------------------")
print("          THANKS, SEE YOU AGAIN!          ")
print("------------------------------------------")
print(" ")

# Send receipt to an email
load_dotenv()

# Building the Email
email_consent = input("Does the customer want their receipt emailed (Y/N): ")

if email_consent == "Y" or "y":
    customer_email = input("Customer's email address: ")
    print(" ")
    print("------------------------------------------")
    print(" ")
    subject = "Your Receipt from Mr. Mango"
    html_content = "Hello World"

    message = Mail(
        from_email=os.environ.get("my_email"),
        to_emails=customer_email,
        subject=subject,
        html_content=html_content)

    # Building the ability to send the email
    sendgrid_client = SendGridAPIClient(os.environ.get("sendgrid_api_key"))

    try:
        response = sendgrid_client.send(message)
        print(response.status_code) #> if 202 prints then SUCCESS
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
else:
    pass
