import subprocess
from pathlib import Path

def install(url: str, dest: Path):
    dest.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["wget", "-O", str(dest), url], check=True)
    print(f"Downloaded: {dest}")

def downloader(version: str, modloader: str, modloader_version: str, folder: str):
    folder = Path(folder)

    if modloader == "vanilla":
        url = f"https://piston-data.mojang.com/v1/objects/{version}/server.jar"
        path = folder / "server.jar"
        install(url, path)

    elif modloader == "forge":
        url = f"https://maven.minecraftforge.net/net/minecraftforge/forge/{version}-{modloader_version}/forge-{version}-{modloader_version}-installer.jar"
        path = folder / f"forge-{version}-{modloader_version}-installer.jar"
        install(url, path)

    elif modloader == "fabric":
        url = f"https://meta.fabricmc.net/v2/versions/loader/{version}/{modloader_version}/1.0.0/server/jar"
        path = folder / f"fabric-{version}-{modloader_version}.jar"
        install(url, path)

    else:
        print(f"Unknown modloader: {modloader}")