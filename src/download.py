import requests
from pathlib import Path
from apis.latest_forge import latest_ver

def install(url: str, dest: Path, file):
    dest.parent.mkdir(parents=True, exist_ok=True)
    print(f"Downloading {url} ...")

    resp = requests.get(url, stream=True)
    resp.raise_for_status()

    with open(dest, "wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    return file

    # print(f"Downloaded: {dest}")

def downloader(version: str, modloader: str, modloaderver: str, folder: str):
    folder = Path(folder)
    latest_forge_ver = latest_ver(version)

    if modloader == "vanilla":
        url = f"https://launcher.mojang.com/v1/objects/{version}/server.jar"
        path = folder / "server.jar"
        file = "server.jar"
        install(url, path, file)
        return file

    elif modloader == "forge":
        if modloaderver == "latest":
            modloaderver = latest_forge_ver

        url = f"https://maven.minecraftforge.net/net/minecraftforge/forge/{version}-{modloaderver}/forge-{version}-{modloaderver}-installer.jar"
        path = folder / f"forge-{version}-{modloaderver}-installer.jar"
        file = f"forge-{version}-{modloaderver}-installer.jar"
        install(url, path, file)
        return file

    elif modloader == "fabric":
        url = f"https://meta.fabricmc.net/v2/versions/loader/{version}/{modloaderver}/1.0.0/server/jar"
        path = folder / f"fabric-{version}-{modloaderver}.jar"
        file = f"fabric-{version}-{modloaderver}.jar"
        install(url, path, file)
        return file

    else:
        print(f"Unknown modloader: {modloader}")


# https://maven.minecraftforge.net/net/minecraftforge/forge/1.21.9-59.0.1/forge-1.21.9-59.0.1-installer.jar