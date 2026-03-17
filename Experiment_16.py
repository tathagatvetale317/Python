import re
phone = input("Enter phone number: ")
email = input("Enter email ID: ")

# Simple patterns
phone_pattern = "^[0-9]{10}$" # Exactly 10 digits
email_pattern = "^[^@]+@[^@]+\.[^@]+$" # Basic email format

# Check phone number
if re.match(phone_pattern, phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")

# Check email
if re.match(email_pattern, email):
    print("Valid Email ID")
else:
    print("Invalid Email ID")
