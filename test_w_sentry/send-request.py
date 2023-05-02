import requests
import json
proxy_server = {
        "http": "http://test-webhook-sentry:9090",
    }
headers = {
    "Content-type": "application/json",
    #"X-WhSentry-TLS": "true",
}
json_data = {"data": "testing"}
url = "http://webhook-client:8081/webhook/testing/"
response = requests.post(
    url,
    proxies=proxy_server,
    data=json.dumps(json_data),
    timeout=(3, 3),
    stream=True,
    headers=headers,
    allow_redirects=False,
)
print(f"Response content: {response.content}")
print(f"Response sent, status received: {response.status_code}")