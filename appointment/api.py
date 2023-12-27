import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()


def _is_valid(phone_number):
    api_key = os.getenv("VERIFY_NUM_KEY")

    """ for checking the validity of the number"""

    url = f"https://phonevalidation.abstractapi.com/v1/?api_key={api_key}&phone={phone_number}"
    response = requests.get(url)
    incoming_response = json.loads(response.content)
    validity = incoming_response.get("valid", False)
    return validity



