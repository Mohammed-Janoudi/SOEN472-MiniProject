# Student Support AI - main chat loop

from assistant import SupportAssistant

KNOWLEDGE_BASE_PATH = "knowledge_base.csv"


def main():
    print("Welcome to Student Support AI")
    print("Type 'quit' to exit.\n")

    # assistant = SupportAssistant(KNOWLEDGE_BASE_PATH)
    history = []

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        if not user_input:
            continue

        # TODO: check sentiment, print it, escalate if needed, then print the answer
        pass


if __name__ == "__main__":
    main()
