import requests

url = "http://127.0.0.1:8000/api/v1/cell/upgrade/"

cell_upgrades = []
cell_upgrade = {"current": "단세포",
                "next": "다세포"}
cell_upgrades.append(cell_upgrade)
cell_upgrade = {"current": "다세포",
                "next": "플랑크톤"}
cell_upgrades.append(cell_upgrade)

for cell_upgrade in cell_upgrades:
    response = requests.post(url, data=cell_upgrade)
    result = response.json()
    result.pop("id")
    assert result == cell_upgrade

