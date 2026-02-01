HIGH_RISK = {"run_shell", "open_url"}
def requires_approval(tool_name: str) -> bool:
    return tool_name in HIGH_RISK
