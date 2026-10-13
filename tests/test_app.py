import os

from app import app, parse_response


def test_parse_response_with_delimited_blocks():
    raw = """===XML===
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"/>
===KOTLIN===
class MainActivity : androidx.appcompat.app.AppCompatActivity() {
    override fun onCreate(savedInstanceState: android.os.Bundle?) {
        super.onCreate(savedInstanceState)
    }
}
===END===
"""

    xml, kotlin = parse_response(raw)

    assert "LinearLayout" in xml
    assert "class MainActivity" in kotlin


def test_parse_response_with_markdown_fallback():
    raw = """```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"/>
```

```kotlin
class MainActivity : androidx.appcompat.app.AppCompatActivity() {}
```
"""

    xml, kotlin = parse_response(raw)

    assert "LinearLayout" in xml
    assert "class MainActivity" in kotlin


def test_generate_missing_prompt_returns_400():
    client = app.test_client()
    response = client.post("/generate", json={})

    assert response.status_code == 400
    assert b"Please enter a description" in response.data


def test_generate_without_api_key_returns_500(monkeypatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    client = app.test_client()
    response = client.post("/generate", json={"prompt": "login screen"})

    assert response.status_code == 500
    assert b"ANTHROPIC_API_KEY" in response.data
