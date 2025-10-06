import subprocess
import os

def start_forge_server(folder):
    subprocess.run(["./run.sh"], cwd=folder)

def start_fabric_server(folder):
    jar_files = [f for f in os.listdir(folder) if f.endswith(".jar")]
    if not jar_files:
        print("Cant find jar file")
        return
    jar_file = jar_files[0]
    subprocess.run(["java", "-Xms1G", "-Xmx4G", "-jar", jar_file, "nogui"],cwd=folder)