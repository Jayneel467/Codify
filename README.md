# Codify 🤖

> **Natural language → Production-ready Android code, instantly.**

Codify is an AI-powered code generation tool that converts plain English descriptions into complete Android XML layouts and Kotlin Activity code using Google's Gemini API.

---

## 🎥 Demo

Type: *"a login screen with email and password"*

Get back:
- ✅ A complete `activity_main.xml` with Material Design components
- ✅ A complete `MainActivity.kt` with view bindings and logic

---

## 🛠 Tech Stack

- **Backend:** Python, Flask
- **AI:** Google Gemini 1.5 Flash (LLM)
- **Frontend:** Vanilla JS, HTML/CSS
- **Pattern:** Prompt engineering with structured output parsing

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/Jayneel467/codify.git
cd codify
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set your Gemini API key
```bash
export GEMINI_API_KEY="your_api_key_here"
```
Get a free key at [Google AI Studio](https://aistudio.google.com/).

### 4. Run the app
```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

---

## 📁 Project Structure

```
codify/
├── app.py               # Flask backend + Gemini API calls
├── templates/
│   └── index.html       # Frontend UI
├── requirements.txt
└── README.md
```

---

## 💡 How It Works

1. User types a description of an Android screen
2. Flask backend sends a structured prompt to Gemini 1.5 Flash
3. Gemini returns XML and Kotlin code inside strict delimiters
4. Backend parses the response and returns both code blocks
5. Frontend renders them side-by-side with copy buttons

The key engineering challenge is **prompt engineering** — getting the LLM to reliably return structured, parseable output every time.

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
