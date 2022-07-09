import requests
from datetime import datetime

USERNAME = "user"
TOKEN = "token"
GRAPH_ID = "graph"

pixela_endpoint = "https://pixe.la/v1/users"

params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=params)
# response.raise_for_status()
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Graph",
    "unit": "hours",
    "type": "float",
    "color": "kuro",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(graph_endpoint, json=graph_config, headers=headers)
# response.raise_for_status()
# print(response.text)

date = datetime.today().strftime("%Y%m%d")
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"

pixel_params = {
    "date": date,
    "quantity": "2",
}


response = requests.put(pixel_endpoint, json=pixel_params, headers=headers)
response.raise_for_status()
print(response.text)
