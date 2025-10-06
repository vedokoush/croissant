import requests

def get_paper_latest(mc_version):
    url = f"https://api.papermc.io/v2/projects/paper/versions/{mc_version}"
    data = requests.get(url).json()
    latest_build = max(data["builds"])
    return latest_build

def get_paper_url(mc_version):
    build = get_paper_latest(mc_version)
    return f"https://api.papermc.io/v2/projects/paper/versions/{mc_version}/builds/{build}/downloads/paper-{mc_version}-{build}.jar"

# print(get_paper_url("1.21.1"))
