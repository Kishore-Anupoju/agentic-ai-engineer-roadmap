from agent import ask_agent
from calculator import calculate

print("=== Gemini Calculator AI Agent ===")
print("Type 'exit' to quit\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Agent: Goodbye!")
        break

    expression = ask_agent(user_input)

    print(f"\nGenerated Expression: {expression}")

    result = calculate(expression)

    print(f"Agent: {result}\n")