import requests

def latest_forge(mc_version: str) -> str:
    url = "https://files.minecraftforge.net/net/minecraftforge/forge/promotions_slim.json"
    r = requests.get(url)
    r.raise_for_status()
    data = r.json()
    promos = data["promos"]

    key = f"{mc_version}-latest"
    if key not in promos:
        raise ValueError(f"Not found!")
    return promos[key]

