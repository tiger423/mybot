from mybot_core.agent import run_turn

def main():
    messages = [
        {"role": "system", "content": "You are MyBot, a helpful local AI assistant."}
    ]
    print("Welcome to MyBot! Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            break

        messages.append({"role": "user", "content": user_input})
        reply = run_turn(messages)
        print("\nMyBot:", reply, "\n")
        messages.append({"role": "assistant", "content": reply})
