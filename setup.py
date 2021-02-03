from venmo_api import Client
from utils import *


def choose_user(users):
    for user in users:
        print("\nusername: " + user.username)
        print("name: " + (user.first_name or "") + " " + (user.last_name or ""))
        print("display name: " + (user.display_name or ""))
        print("phone: " + (user.phone or ""))
        print("profile picture url: " + (user.profile_picture_url or ""))
        answer = yes_or_no("Is this the correct user?")
        if (answer):
            return user


def choose_payment_method(payment_methods):
    for pm in payment_methods:
        print("\nname: " + pm._json['name'])
        print("last four: " + (pm._json['last_four'] or ""))
        print("type: " + pm._json['type'])
        answer = yes_or_no("Is this the correct payment method?")
        if (answer):
            return pm


username = input("What is your venmo username? ")
password = input("What is your venmo password? ")
access_token = Client.get_access_token(username=username,
                                       password=password)

venmo = Client(access_token=access_token)

payee_username = input(
    "\nWhat's the username of the person you want to schedule a payment to? ")
print("Searching for users...")
users = venmo.user.search_for_users(query=payee_username)
payee = choose_user(users)
if (payee == None):
    print("Could not find correct user. Are you sure you entered the correct username?\n")

print("Fetching payment methods...")
payment_methods = venmo.payment.get_payment_methods()
payment_method = choose_payment_method(payment_methods)
if (payment_method == None):
    print("You didn't select a payment method. Make sure the appropriate method is added to your Venmo account\n")
payment_amount = input("\nHow much is the payment? ")
payment_note = input("What is the payment note? ")

if (None in [access_token, payee, payment_method] or "" in [payment_note, payment_amount]):
    print("\nWARNING: You don't have all the required environment variables. The script will not work without all of them.")

print("\n---------------------------------------------------------------------")
print("Here are the environment variables you will need for the main script:")
print_env("access_token", access_token)
print_env("payee_id", (payee and payee.id))
print_env("payment_note", payment_note)
print_env("payment_amount", payment_amount)
print_env("funding_source_id", (payment_method and payment_method.id))
