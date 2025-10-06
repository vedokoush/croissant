import requests

def latest_quilt(mc_version: str) -> str:
    url = f"https://meta.quiltmc.org/v3/versions/loader/{mc_version}"
    r = requests.get(url)
    r.raise_for_status()
    data = r.json()
    if not data:
        raise ValueError(f"Not found Quilt for {mc_version}")
    return data[0]["loader"]["version"]