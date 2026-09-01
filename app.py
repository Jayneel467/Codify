from flask import Flask, request, jsonify, render_template
import anthropic
import os
import re

app = Flask(__name__, template_folder='.')

_client = None


def get_client():
    """Lazily create the Anthropic client.

    Reads the key from the ANTHROPIC_API_KEY environment variable
    automatically. Creating it lazily (instead of at import time) means the
    module can still be imported -- e.g. for tests -- even if the key isn't
    set, and a missing key only surfaces as a clear error on an actual
    request instead of crashing app startup.
    """
    global _client
    if _client is None:
        _client = anthropic.Anthropic()
    return _client


SYSTEM_PROMPT = """You are Codify, an expert Android developer assistant.
When given a description of an Android screen or component, you MUST respond with EXACTLY this format and nothing else:

===XML===
<the complete Android XML layout code here>
===KOTLIN===
<the complete Kotlin Activity or Fragment code here>
===END===

Rules:
- XML should be a complete, valid Android layout file using ConstraintLayout or LinearLayout
- Kotlin should be a complete Activity class with all imports, view bindings, and basic logic
- Use Material Design components (MaterialButton, TextInputLayout, etc.)
- Keep code clean, well-commented, and production-ready
- Do not include any explanation outside the delimiters
"""


def parse_response(text):
    print(f"Raw Claude response:\n{text}\n")

    xml_match = re.search(r'===XML===\s*(.*?)\s*===KOTLIN===', text, re.DOTALL | re.IGNORECASE)
    kotlin_match = re.search(r'===KOTLIN===\s*(.*?)\s*(?:===END===|$)', text, re.DOTALL | re.IGNORECASE)

    if xml_match and kotlin_match:
        xml_code = xml_match.group(1).strip()
        kotlin_code = kotlin_match.group(1).strip()
    else:
        xml_fallback = re.search(r'```(?:xml)?\n?(.*?)\n?```', text, re.DOTALL | re.IGNORECASE)
        kotlin_fallback = re.search(r'```kotlin\n?(.*?)\n?```', text, re.DOTALL | re.IGNORECASE)
        xml_code = xml_fallback.group(1).strip() if xml_fallback else f"<!-- Could not parse XML -->\n<!--\n{text}\n-->"
        kotlin_code = kotlin_fallback.group(1).strip() if kotlin_fallback else f"// Could not parse Kotlin\n/*\n{text}\n*/"

    xml_code = re.sub(r'^```(?:xml)?\n?(.*?)\n?```$', r'\1', xml_code, flags=re.DOTALL).strip()
    kotlin_code = re.sub(r'^```(?:kotlin)?\n?(.*?)\n?```$', r'\1', kotlin_code, flags=re.DOTALL).strip()

    return xml_code, kotlin_code


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    user_prompt = data.get("prompt", "").strip()

    if not user_prompt:
        return jsonify({"error": "Please enter a description."}), 400

    try:
        message = get_client().messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=2048,
            system=SYSTEM_PROMPT,
            messages=[
                {"role": "user", "content": f"Generate Android code for: {user_prompt}"}
            ]
        )

        response_text = message.content[0].text
        xml_code, kotlin_code = parse_response(response_text)
        return jsonify({"xml": xml_code, "kotlin": kotlin_code})

    except anthropic.AuthenticationError:
        return jsonify({"error": "Invalid API key. Check your ANTHROPIC_API_KEY environment variable."}), 401
    except anthropic.RateLimitError:
        return jsonify({"error": "Rate limit hit. Please wait a moment and try again."}), 429
    except anthropic.AnthropicError as e:
        # Covers cases like a missing ANTHROPIC_API_KEY, which raises here
        # rather than as an AuthenticationError.
        return jsonify({"error": f"Anthropic client error: {e}"}), 500
    except Exception as e:
        print(f"Unexpected error: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    debug_mode = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    app.run(debug=debug_mode, port=int(os.environ.get("PORT", 5001)))
