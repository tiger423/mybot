import subprocess
from pathlib import Path

def read_file(path: str):
    p = Path(path)
    if not p.exists():
        return f"ERROR: File not found: {path}"
    try:
        return p.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        pass
    for enc in ("cp950", "big5", "gbk", "latin1"):
        try:
            return p.read_text(encoding=enc)
        except UnicodeDecodeError:
            continue
    return p.read_bytes().decode(errors="replace")

def write_file(path: str, content: str):
    Path(path).write_text(content, encoding="utf-8")
    return f"Wrote to {path}"

def run_shell(command: str):
    try:
        return subprocess.check_output(command, shell=True, text=True)
    except Exception as e:
        return f"ERROR: {e}"
