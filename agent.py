import json
from mybot_core.llm import call_llm
from mybot_core.dispatcher import dispatch
from mybot_core.safety import requires_approval
from mybot_core.planner_prompt import PLANNER_PROMPT
from mybot_core.executor_prompt import EXECUTOR_PROMPT

def run_turn(messages):
    user_message = messages[-1]["content"]

    planner_messages = [
        {"role": "system", "content": PLANNER_PROMPT},
        {"role": "user", "content": user_message},
    ]
    planner_response = call_llm(planner_messages)
    plan = json.loads(planner_response.output_text)

    print("\n📋 Proposed Plan:")
    print(json.dumps(plan, indent=2, ensure_ascii=False))

    if input("Approve this plan? (yes/no): ").strip().lower() != "yes":
        return "Plan rejected."

    executor_messages = [
        {"role": "system", "content": EXECUTOR_PROMPT},
        {"role": "system", "content": f"Approved plan:\n{json.dumps(plan, ensure_ascii=False)}"},
        {"role": "user", "content": user_message},
    ]

    response = call_llm(executor_messages)

    for item in response.output:
        if getattr(item, "type", None) == "function_call":
            tool = item.name
            args = json.loads(item.arguments or "{}")

            if tool not in plan.get("tools_needed", []):
                return f"Blocked: tool '{tool}' not approved."

            print(f"\n🛠️ Tool request: {tool}")
            print(f"Args: {args}")

            if requires_approval(tool):
                if input("Approve tool execution? (yes/no): ").strip().lower() != "yes":
                    return "Tool execution denied."

            result = dispatch(tool, args)
            executor_messages.append(
                {"role": "system", "content": f"Tool {tool} result:\n{result}"}
            )
            followup = call_llm(executor_messages)
            return followup.output_text

    return response.output_text
