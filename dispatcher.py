from mybot_core.tools import read_file, write_file, run_shell
from mybot_core.browser import open_url

_TOOL_MAP = {
    "read_file": read_file,
    "write_file": write_file,
    "run_shell": run_shell,
    "open_url": open_url,
}

def dispatch(name, args):
    return _TOOL_MAP[name](**args)
