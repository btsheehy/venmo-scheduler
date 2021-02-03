from venmo_api import Client
import os
import ast
import re

access_token = os.getenv("access_token")
payee_id = os.getenv("payee_id")
payment_note = os.getenv("payment_note")
payment_amount = ast.literal_eval(
    re.sub("[^0-9.]", "", os.getenv("payment amount")))
funding_source_id = os.getenv("funding_source_id")

venmo = Client(
    access_token=access_token)

venmo.payment.send_money(payment_amount, payment_note, payee_id,
                         funding_source_id=funding_source_id)
