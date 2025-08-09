import os
import sys

# Ensure the module path is available when running tests from the tests directory
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import npc_dialogue


def test_nonviolence_not_filtered():
    text = "This game promotes nonviolence and peace"
    assert npc_dialogue.filter_dialogue(text) == text


def test_violence_filtered():
    text = "The battle was full of violence"
    assert "[Filtered:" in npc_dialogue.filter_dialogue(text)


def test_speak_dialogue_no_crash():
    # Function should fail gracefully even if TTS backend is missing
    npc_dialogue.speak_dialogue("Hello there")
