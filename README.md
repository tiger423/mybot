# MyBot

MyBot is a **local AI agent framework** built on the OpenAI Responses API.  
It is designed to safely interact with **local files, shell commands, and a sandboxed browser** using a **Planner ¡÷ Executor** architecture.

This project focuses on **correctness, safety, and debuggability**, not just demos.

---

## ? Features

- ? OpenAI **Responses API** (`gpt-5.2`)
- ?? **Planner ¡÷ Executor** agent architecture
- ?? Human approval gates for plans and risky tools
- ?? Local file access (`read_file`, `write_file`)
- ??? Shell command execution (`run_shell`)
- ?? Sandboxed browser automation via **Playwright**
- ?? Windows-safe (encoding + Playwright lifecycle handled)
- ?? Restart-safe (no random crashes)

---

## ?? Agent Architecture (High Level)

MyBot separates **decision making** from **execution**:

- **Planner**
  - Thinks only
  - Produces a structured JSON plan
  - No tools allowed

- **Executor**
  - Executes the approved plan
  - Uses tools strictly listed in the plan
  - Enforces safety checks

This mirrors production agent designs (AutoGPT, LangGraph, Devin-style agents).


flowchart TD
    START([Start MyBot]) --> INPUT[User enters request]

    INPUT --> PLAN_LLM[Planner LLM]
    PLAN_LLM --> PLAN_JSON{Valid JSON Plan?}

    PLAN_JSON -->|No| PLAN_ERROR[Return planning error]
    PLAN_JSON -->|Yes| SHOW_PLAN[Show plan to user]

    SHOW_PLAN --> PLAN_APPROVAL{User approves plan?}
    PLAN_APPROVAL -->|No| STOP_PLAN[Stop: Plan rejected]
    PLAN_APPROVAL -->|Yes| EXEC_LLM[Executor LLM]

    EXEC_LLM --> TOOL_CALL{Tool call requested?}

    TOOL_CALL -->|No| FINAL[Return final response]

    TOOL_CALL -->|Yes| TOOL_ALLOWED{Tool in tools_needed?}
    TOOL_ALLOWED -->|No| BLOCKED[Blocked: Tool not approved]

    TOOL_ALLOWED -->|Yes| TOOL_RISK{High-risk tool?}
    TOOL_RISK -->|Yes| TOOL_APPROVAL{User approves tool?}
    TOOL_RISK -->|No| RUN_TOOL[Run tool]

    TOOL_APPROVAL -->|No| STOP_TOOL[Stop: Tool denied]
    TOOL_APPROVAL -->|Yes| RUN_TOOL

    RUN_TOOL --> TOOL_RESULT[Tool result]
    TOOL_RESULT --> EXEC_LLM

    EXEC_LLM --> FINAL
    FINAL --> INPUT







---

+---------+
|  User   |
+----+----+
     |
     v
+-------------+
|   Planner   |   (LLM, no tools)
+------+------+
       |
       v
+------------------+
| Human Approval   |
+------+-----------+
       |
       v
+-------------+
|  Executor   |   (LLM, tools allowed)
+------+------+
       |
       v
+-------------------+
| Tool Dispatcher   |
+---+----+----+-----+
    |    |    |
    v    v    v
 read  write  shell  browser
 file  file   cmd    (Playwright)

       |
       v
+----------------+
| Final Response |
+----------------+


## ?? Supported Tools

| Tool        | Description |
|------------|-------------|
| `read_file` | Read local files (UTF-8 / Big5 / CP950 safe) |
| `write_file` | Write local files |
| `run_shell` | Execute shell commands |
| `open_url` | Open websites in a Playwright sandbox |

High-risk tools require explicit approval.

---

## ?? Installation

### Requirements
- Python 3.10+
- Playwright
- OpenAI API key

### Clean install (recommended)

```bash
pip uninstall mybot -y
pip cache purge

unzip mybot_final_clean.zip
cd mybot_final_clean

pip install -e .
playwright install chromium



