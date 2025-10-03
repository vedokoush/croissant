import subprocess

def installServer(folder, name):
    subprocess.run(["java", "-jar", name, "--installServer"], cwd=folder)
    # subprocess.run(["ls"], cwd=folder)
    # print(name)
