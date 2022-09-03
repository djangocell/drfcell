import requests

url = "http://127.0.0.1:8000/api/v1/cell/"

cells = []
cell = {"name": "단세포",
        "damage": 5,
        "upgrade_resource": 10}
cells.append(cell)

cell = {"name": "다세포",
        "damage": 10,
        "upgrade_resource": 20}
cells.append(cell)

cell = {"name": "플랑크톤",
        "damage": 20,
        "upgrade_resource": 40}
cells.append(cell)



for cell in cells:
    response = requests.post(url, data=cell)
    result = response.json()
    assert result == cell

