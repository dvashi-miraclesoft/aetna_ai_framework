from sklearn.metrics import f1_score

def calculate_f1_score(expected: list, predicted: list) -> float:
    """
    Calculates the F1-score for Conversational AI intents.
    Uses 'macro' averaging to treat all intents (like check_claims and find_doctor) equally.
    """
    # scikit-learn does the heavy mathematical lifting for us
    score = f1_score(expected, predicted, average='macro')
    return float(score)