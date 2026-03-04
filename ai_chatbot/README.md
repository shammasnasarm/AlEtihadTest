# AI Chatbot

A terminal-based customer support chatbot for **Shams Info Tech**, powered by the OpenAI Chat Completions API (`gpt-4.1-nano`). Type a message to get a reply, type `exit` to quit.

---

## Project Structure

    ai_chatbot/
    │
    ├── main.py
    ├── utils.py
    ├── data.py
    ├── requirements.txt
    └── .env.template

---

## Setup & Run

```bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create a .env file with your OpenAI API key
cp .env.template .env
# Fill OPENAI_API_KEY in .env

# 4. Run
python main.py
```

---

## Usage

```
Shams Customer Support Chatbot
Type 'exit' to quit.

You: What services do you offer?
Chatbot: We provide IT services and solutions including Python, Django, FastAPI, AWS ...

You: exit
Chatbot: Thank you for contacting TechNova. Goodbye!
```

---

## How it works

- System prompt is loaded from `data.py` (`COMPANY_INFO`) — contains company details, tech stack, contact info, and business hours
- Each user message is sent to `gpt-4.1-nano` with the system prompt as context
- Response is printed to the terminal
- Conversation is stateless — each message is a fresh API call

---

> **Note:**  
> A paid OpenAI account is required to access the models used by this chatbot.  
> This project is provided as-is and has not been tested end-to-end due to model access limitations.  
> To the best of my knowledge and research, the code should otherwise work as described.