from pathlib import Path

def write_eula(folder: str):
    eula_path = Path(folder) / "eula.txt"
    content = "eula=true\n"
    eula_path.write_text(content, encoding="utf-8")
    print(f"Created {eula_path}")