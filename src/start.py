import subprocess

def startServer(folder, name):
    subprocess.run(["./run.sh"], cwd=folder)