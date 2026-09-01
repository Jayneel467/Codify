"""Tests for app.py.

These tests don't call the Anthropic API -- parse_response is pure text
processing, and the /generate route is tested only for its validation path
(empty prompt), so no ANTHROPIC_API_KEY is needed to run this suite.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, parse_response  # noqa: E402


def test_parse_response_well_formed():
    text = (
        "===XML===\n<TextView />\n===KOTLIN===\nclass Main : Activity()\n===END==="
    )
    xml_code, kotlin_code = parse_response(text)
    assert xml_code == "<TextView />"
    assert kotlin_code == "class Main : Activity()"


def test_parse_response_falls_back_to_markdown_fences():
    text = "Here you go:\n```xml\n<TextView />\n```\n```kotlin\nclass Main\n```"
    xml_code, kotlin_code = parse_response(text)
    assert xml_code == "<TextView />"
    assert kotlin_code == "class Main"


def test_parse_response_unparseable_text_does_not_raise():
    xml_code, kotlin_code = parse_response("not in the expected format at all")
    assert "Could not parse XML" in xml_code
    assert "Could not parse Kotlin" in kotlin_code


def test_generate_rejects_empty_prompt():
    client = app.test_client()
    response = client.post("/generate", json={"prompt": "   "})
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_index_route_serves_ui():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
