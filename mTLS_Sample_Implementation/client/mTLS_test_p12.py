import requests
from requests_pkcs12 import Pkcs12Adapter

session = requests.Session()
session.mount("https://", Pkcs12Adapter(
    pkcs12_filename="client.p12",
    pkcs12_password="Test1234"
))

r = session.get(
    "https://localhost/api",
    verify="rootCA.crt",
    timeout=10
)

print(f"Status: {r.status_code}")
print(f"Body: {r.text}")