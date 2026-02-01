TOOLS_SCHEMA = [
    {"type": "function", "name": "read_file", "description": "Read local file",
     "parameters": {"type": "object", "properties": {"path": {"type": "string"}}, "required": ["path"]}},
    {"type": "function", "name": "write_file", "description": "Write local file",
     "parameters": {"type": "object", "properties": {"path": {"type": "string"}, "content": {"type": "string"}}, "required": ["path", "content"]}},
    {"type": "function", "name": "run_shell", "description": "Run shell command",
     "parameters": {"type": "object", "properties": {"command": {"type": "string"}}, "required": ["command"]}},
    {"type": "function", "name": "open_url", "description": "Open website",
     "parameters": {"type": "object", "properties": {"url": {"type": "string"}}, "required": ["url"]}}
]
