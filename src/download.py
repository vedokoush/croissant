import requests
from pathlib import Path
from apis.latest_forge import latest_forge
from apis.latest_fabric import latest_fabric
# from apis.latest_neoforge import latest_neoforge
# from apis.latest_quilt import latest_quilt


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


def downloader(version: str, modloader: str, modloaderver: str, folder: str):
    folder = Path(folder)

    if modloader == "vanilla":
        url = f"https://launcher.mojang.com/v1/objects/{version}/server.jar"
        path = folder / "server.jar"
        file = "server.jar"
        return install(url, path, file)

    elif modloader == "forge":
        if modloaderver == "latest":
            modloaderver = latest_forge(version)
        url = (
            f"https://maven.minecraftforge.net/net/minecraftforge/forge/"
            f"{version}-{modloaderver}/forge-{version}-{modloaderver}-installer.jar"
        )
        file_name = f"forge-{version}-{modloaderver}-installer.jar"
        path = folder / file_name
        return install(url, path, file_name)

    elif modloader == "fabric":
        if modloaderver == "latest":
            modloaderver = latest_fabric(version)
        url = (
            f"https://meta.fabricmc.net/v2/versions/loader/"
            f"{version}/{modloaderver}/1.0.0/server/jar"
        )
        file_name = f"fabric-{version}-{modloaderver}.jar"
        path = folder / file_name
        return install(url, path, file_name)

    # elif modloader == "neoforge":
    #     if modloaderver == "latest":
    #         modloaderver = latest_neoforge(version)
    #     url = (
    #         f"https://maven.neoforged.net/releases/net/neoforged/neoforge/"
    #         f"{modloaderver}/neoforge-{modloaderver}-installer.jar"
    #     )
    #     file_name = f"neoforge-{modloaderver}-installer.jar"
    #     path = folder / file_name
    #     return install(url, path, file_name)

    # elif modloader == "quilt":
    #     if modloaderver == "latest":
    #         modloaderver = latest_quilt(version)
    #     url = (
    #         f"https://meta.quiltmc.org/v3/versions/loader/"
    #         f"{version}/{modloaderver}/1.0.0/server/jar"
    #     )
    #     file_name = f"quilt-{version}-{modloaderver}.jar"
    #     path = folder / file_name
    #     return install(url, path, file_name)

    else:
        print(f"Unknown modloader: {modloader}")


# https://maven.minecraftforge.net/net/minecraftforge/forge/1.21.9-59.0.1/forge-1.21.9-59.0.1-installer.jar