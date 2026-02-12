import pytest
# We are importing a function that DOES NOT EXIST yet. This is TDD.
from src.evaluator import calculate_f1_score

def test_healthcare_bot_f1_score_meets_threshold():
    # 1. ARRANGE: Define our test data
    # What the user actually wanted:
    expected_intents = ["check_claims", "check_claims", "find_doctor", "find_doctor"]
    
    # What the Aetna Bot actually understood:
    # Notice it got the second one wrong (thought 'find_doctor' instead of 'check_claims')
    predicted_intents = ["check_claims", "find_doctor", "find_doctor", "find_doctor"]
    
    # 2. ACT: Run the evaluation function
    f1 = calculate_f1_score(expected_intents, predicted_intents)
    
    # 3. ASSERT: The company requirement is an 80% F1-Score for production
    assert f1 >= 0.80, f"Bot F1 Score {f1:.2f} is below the 80% production threshold!"