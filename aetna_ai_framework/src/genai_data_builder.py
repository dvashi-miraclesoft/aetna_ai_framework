import json

def generate_synthetic_patient_data(prompt_request):
    """
    Simulates sending a prompt to a GenAI model (like Gemini or ChatGPT)
    to generate synthetic, HIPAA-compliant test data.
    """
    print(f"Sending prompt to GenAI: '{prompt_request}'\n")
    
    # In a real environment, this is where you call the GCP/OpenAI API.
    # We are simulating the AI's JSON response for the framework.
    mock_ai_response = """
    [
        {"patient_id": "A101", "condition": "Type 2 Diabetes", "is_hipaa_safe": true},
        {"patient_id": "A102", "condition": "Hypertension", "is_hipaa_safe": true},
        {"patient_id": "A103", "condition": "Asthma", "is_hipaa_safe": true}
    ]
    """
    return json.loads(mock_ai_response)

def run_test_data_generation():
    # 1. The QA Engineer designs a Prompt for the AI
    ai_prompt = (
        "Generate 3 synthetic patient records for Aetna healthcare portal testing. "
        "Do NOT include real names, SSNs, or actual PII to maintain HIPAA compliance. "
        "Return strictly as a JSON array."
    )
    
    # 2. The AI generates the data
    test_data = generate_synthetic_patient_data(ai_prompt)
    
    # 3. We validate the AI's output before feeding it to our Pytest/Selenium scripts
    print("--- GenAI Output Validation ---")
    for record in test_data:
        assert record["is_hipaa_safe"] is True, "AI generated non-compliant data!"
        print(f"Successfully generated secure test record for: {record['condition']}")

if __name__ == "__main__":
    run_test_data_generation()