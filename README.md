# Codify 🤖

> **Natural language → Production-ready Android code, instantly.**

Codify is an AI-powered code generation tool that converts plain English descriptions into complete Android XML layouts and Kotlin Activity code using the Anthropic Claude API.

---

## 🎥 Demo

Type: *"a login screen with email and password"*

Get back:
- ✅ A complete `activity_main.xml` with Material Design components
- ✅ A complete `MainActivity.kt` with view bindings and logic

---

## 🛠 Tech Stack

- **Backend:** Python, Flask
- **AI:** Anthropic Claude (claude-haiku-4-5)
- **Frontend:** Vanilla JS, HTML/CSS
- **Pattern:** Prompt engineering with structured output parsing

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/Jayneel467/codify.git
cd codify
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set your Anthropic API key
```bash
export ANTHROPIC_API_KEY="your_api_key_here"
```
Get a free key at [Anthropic Console](https://console.anthropic.com/).

### 5. Run the app
```bash
python app.py
```

Visit `http://localhost:5001` in your browser.

---

## 📁 Project Structure

```
codify/
├── app.py               # Flask backend + Claude API calls
├── templates/
│   └── index.html       # Frontend UI
├── requirements.txt
└── README.md
```

---

## 💡 How It Works

1. User types a description of an Android screen
2. Flask backend sends a structured prompt to Claude
3. Claude returns XML and Kotlin code inside strict delimiters (`===XML===`, `===KOTLIN===`, `===END===`)
4. Backend parses the response and extracts both code blocks
5. Frontend renders them side-by-side with copy buttons

The key engineering challenge is **prompt engineering** — getting the LLM to reliably return structured, parseable output every time. A fallback parser also handles markdown code blocks in case Claude doesn't follow the delimiters exactly.

---

## 🗺 Roadmap

- [ ] Syntax highlighting in the UI
- [ ] Download as `.zip` with full Android project structure
- [ ] Multi-screen app generation with navigation graph
- [ ] Support for Jetpack Compose output
- [ ] Conversation history (multi-turn refinement)

---

## 👤 Author

**Jayneel Girnara** — [linkedin.com/in/jayneelgirnara](https://linkedin.com/in/jayneelgirnara)

Penn State CS | Building AI-powered developer tools
