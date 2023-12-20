import os
from dotenv import load_dotenv
import requests

url = os.getenv("IP_ADDRESS_BASE_URL")


def get_address(user_ip):
    ip_url = f"{url}{user_ip}"
    response = requests.get(ip_url)
    details = response.json()
    country = details.get("country", "")
    city = details.get("city", "")
    address = f"{country} {city}"
    print(address)
    return address