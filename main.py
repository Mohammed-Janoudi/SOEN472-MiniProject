# Student Support AI - main chat loop

from assistant import SupportAssistant

KNOWLEDGE_BASE_PATH = "knowledge_base.csv"


def main():
    print("Welcome to Student Support AI")
    print("Type 'quit' to exit.\n")

    assistant = SupportAssistant(KNOWLEDGE_BASE_PATH)
    history = []

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        if not user_input:
            continue

        label, score = assistant.analyze_sentiment(user_input)
        print(f"Sentiment: {label} ({score:.2f})")

        if assistant.should_escalate(label, score):
            print("Recommended escalation: Contact human advisor.")

        answer = assistant.semantic_search(user_input)
        print(f"Answer: {answer}\n")

        history.append({"user": user_input, "sentiment": label, "answer": answer})


if __name__ == "__main__":
    main()
