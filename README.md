# Codify 🤖

> Natural language → production-ready Android UI code in seconds.

Codify is an AI-powered app that turns plain-English UI descriptions into complete Android XML layouts and Kotlin activity code using the Anthropic Claude API. It’s built as a practical tool for speeding up mobile UI prototyping and reducing hand-written boilerplate.

---

## What it does

You can type prompts such as:

- "a login screen with email and password"
- "a modern settings page with cards and toggles"
- "a product listing screen with search and filters"

Codify responds with:

- a complete `activity_main.xml` layout
- matching `MainActivity.kt` code
- structured output that is easy to copy into an Android project

---

## Tech stack

- Backend: Python, Flask
- AI: Anthropic Claude API
- Frontend: HTML, CSS, JavaScript
- Pattern: Prompt engineering + structured response parsing

---

## Features

- Converts natural-language UI descriptions into Android XML
- Generates Kotlin activity logic for common screen patterns
- Displays parsed output side-by-side for easy review
- Built for rapid prototyping and iteration
- Designed for developer workflows that need quick mockups

---

## Quick start

### 1. Clone the repo

```bash
git clone https://github.com/Jayneel467/Codify.git
cd Codify
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Anthropic API key

```bash
export ANTHROPIC_API_KEY="your_api_key_here"
```

### 5. Run the app

```bash
python app.py
```

Open `http://localhost:5001` in your browser.

---

## Project structure

```text
Codify/
├── app.py
├── templates/
│   └── index.html
├── requirements.txt
├── README.md
└── .env.example
```

---

## How it works

1. The user enters a UI description in plain English.
2. The Flask backend sends a structured prompt to Claude.
3. The model returns XML and Kotlin code in clearly separated blocks.
4. The backend parses the output and renders it in the UI.
5. The developer can copy and paste the generated code directly into Android Studio.

The main challenge here is structured generation — ensuring the model returns format-stable code that can be reliably parsed.

---

## Roadmap

- syntax highlighting in generated code blocks
- download as a zip with full Android project structure
- multi-screen flow generation
- Jetpack Compose support
- multi-turn refinement / chat-based editing

---

## Author

Jayneel Girnara

Penn State CS • building product-minded AI tools
