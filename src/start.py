import subprocess

def start_forge_server(folder):
    subprocess.run(["./run.sh"], cwd=folder)
