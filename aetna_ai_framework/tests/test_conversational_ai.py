import pytest

# Mock NLU (Natural Language Understanding) Engine
def get_bot_intent(user_input):
    """Simulates a chatbot's ability to categorize user speech."""
    intents = {
        "where is my doctor": "FIND_PROVIDER",
        "check my claim status": "CHECK_CLAIMS",
        "i need a new id card": "ORDER_REPLACEMENT"
    }
    # Return the intent or 'FALLBACK' if it doesn't match
    return intents.get(user_input.lower(), "FALLBACK")

@pytest.mark.parametrize("user_speech, expected_intent", [
    ("Where is my doctor", "FIND_PROVIDER"),
    ("check my claim status", "CHECK_CLAIMS"),
    ("I want to buy a pizza", "FALLBACK") # Testing the 'Unknown' path
])
def test_chatbot_intent_mapping(user_speech, expected_intent):
    """Verifies the bot correctly maps speech to healthcare intents."""
    actual_intent = get_bot_intent(user_speech)
    assert actual_intent == expected_intent, f"Bot misidentified '{user_speech}'!"