from data import COMPANY_INFO


def ask_chatbot(client, user_message: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=[
            {"role": "system", "content": COMPANY_INFO},
            {"role": "user", "content": user_message}
        ],
        temperature=0.5
    )

    return response.choices[0].message.content