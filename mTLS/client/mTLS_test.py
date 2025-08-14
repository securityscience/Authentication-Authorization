import requests

url = "https://localhost/api"

response = requests.get(
    url,
    cert=("client.crt",
          "client.key"),
    verify="rootCA.crt"
)

print("Status:", response.status_code)
print("Body:", response.text)