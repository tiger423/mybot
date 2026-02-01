# MyBot Architecture

## Core Design
MyBot uses a Planner ¡÷ Executor architecture.

### Planner
- No tools
- Produces JSON plan
- Determines intent

### Executor
- Executes approved plan
- Enforces tool allow-list
- Requests human approval for risky actions

### Why this matters
This prevents:
- tool hallucinations
- unsafe execution
- nondeterministic behavior

This is the same architecture used in production agents.
