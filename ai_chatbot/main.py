import os
from openai import OpenAI
from dotenv import load_dotenv

from utils import ask_chatbot

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def main():
    print("Shams Customer Support Chatbot")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Chatbot: Thank you for contacting TechNova. Goodbye!")
            break

        reply = ask_chatbot(client, user_input)
        print("Chatbot:", reply)
        print()


if __name__ == "__main__":
    main()