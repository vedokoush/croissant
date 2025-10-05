import requests

def latest_fabric(mc_version: str) -> str:
    url = f"https://meta.fabricmc.net/v2/versions/loader/{mc_version}/"
    r = requests.get(url)
    r.raise_for_status()
    data = r.json()

    if not data:
        raise ValueError(f"Not found {mc_version}")

    latest_loader = data[0]["loader"]["version"]
    return latest_loader

